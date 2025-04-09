import os
from datetime import datetime
from typing import List

import pyodbc
import re

from dao.IJobBoardService import IJobBoardService
from execeptions.FileUploadException import FileUploadException
from execeptions.SalaryCalculationException import SalaryCalculationException
from execeptions.ApplicationDeadlineException import ApplicationDeadlineException
from execeptions.DatabaseConnectionException import DatabaseConnectionException
from execeptions.InvalidEmailException import InvalidEmailException
from entity.model.JobListing import JobListing
from entity.model.Company import Company
from entity.model.Applicant import Applicant
from entity.model.JobApplication import JobApplication


class JobBoardServiceImpl(IJobBoardService):
    def __init__(self, connection_string: str = None):
        self.connection_string = connection_string or self._get_default_connection_string()

    def _get_default_connection_string(self):
        return (
            "Driver={SQL Server};"
            "Server=localhost;"
            "Database=CareerHub;"
            "Trusted_Connection=yes;"
        )

    def _get_connection(self):
        try:
            conn = pyodbc.connect(self.connection_string)
            return conn
        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Failed to connect to database: {str(e)}")

    def insert_job_listing(self, job: JobListing) -> bool:
        conn = None
        try:
            conn = self._get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO Jobs 
                (CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            params = (
                job.company_id, job.job_title, job.job_description,
                job.job_location, job.salary, job.job_type, job.posted_date
            )

            cursor.execute(query, params)
            conn.commit()
            return True

        except pyodbc.Error as e:
            if conn: conn.rollback()
            raise DatabaseConnectionException(f"Failed to insert job listing: {str(e)}")
        finally:
            if conn: conn.close()

    def insert_company(self, company: Company) -> bool:
        conn = None
        try:
            conn = self._get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO Companies 
                (CompanyName, Location)
                VALUES (?, ?)
            """
            params = (company.company_name, company.location)

            cursor.execute(query, params)
            conn.commit()
            return True

        except pyodbc.Error as e:
            if conn: conn.rollback()
            raise DatabaseConnectionException(f"Failed to insert company: {str(e)}")
        finally:
            if conn: conn.close()

    def insert_applicant(self, applicant: Applicant) -> bool:
        conn = None
        try:
            # Validate email first
            if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", applicant.email):
                raise InvalidEmailException("Invalid email format")

            conn = self._get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO Applicants 
                (FirstName, LastName, Email, Phone, Resume)
                VALUES (?, ?, ?, ?, ?)
            """
            params = (
                applicant.first_name, applicant.last_name,
                applicant.email, applicant.phone, applicant.resume
            )

            cursor.execute(query, params)
            conn.commit()
            return True

        except pyodbc.Error as e:
            if conn: conn.rollback()
            raise DatabaseConnectionException(f"Failed to insert applicant: {str(e)}")
        finally:
            if conn: conn.close()

    def insert_job_application(self, application: JobApplication) -> bool:
        conn = None
        try:
            # Check application deadline
            job_deadline = self._get_job_deadline(application.job_id)
            if datetime.now() > job_deadline:
                raise ApplicationDeadlineException("Application deadline has passed")

            conn = self._get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO Applications 
                (JobID, ApplicantID, ApplicationDate, CoverLetter)
                VALUES (?, ?, ?, ?)
            """
            params = (
                application.job_id, application.applicant_id,
                application.application_date, application.cover_letter
            )

            cursor.execute(query, params)
            conn.commit()
            return True

        except pyodbc.Error as e:
            if conn: conn.rollback()
            raise DatabaseConnectionException(f"Failed to insert job application: {str(e)}")
        finally:
            if conn: conn.close()

    def _get_job_deadline(self, job_id: int) -> datetime:
        """Helper method to get job deadline (assuming 30 days from posting)"""
        conn = None
        try:
            conn = self._get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT PostedDate FROM Jobs WHERE JobID = ?", job_id)
            row = cursor.fetchone()
            if row:
                posted_date = row[0]
                return posted_date.replace(year=posted_date.year + 1)  # Example: 1 year deadline
            return datetime.max  # No deadline if job not found

        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Failed to get job deadline: {str(e)}")
        finally:
            if conn: conn.close()

    def get_job_listings(self) -> List[JobListing]:
        conn = None
        try:
            conn = self._get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT JobID, CompanyID, JobTitle, JobDescription, 
                       JobLocation, Salary, JobType, PostedDate 
                FROM Jobs
            """)

            jobs = []
            for row in cursor:
                jobs.append(JobListing(
                    job_id=row.JobID,
                    company_id=row.CompanyID,
                    job_title=row.JobTitle,
                    job_description=row.JobDescription,
                    job_location=row.JobLocation,
                    salary=row.Salary,
                    job_type=row.JobType,
                    posted_date=row.PostedDate
                ))
            return jobs

        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Failed to get job listings: {str(e)}")
        finally:
            if conn: conn.close()

    def get_companies(self) -> List[Company]:
        conn = None
        try:
            conn = self._get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT CompanyID, CompanyName, Location FROM Companies")

            companies = []
            for row in cursor:
                companies.append(Company(
                    company_id=row.CompanyID,
                    company_name=row.CompanyName,
                    location=row.Location
                ))
            return companies

        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Failed to get companies: {str(e)}")
        finally:
            if conn: conn.close()

    def get_applicants(self) -> List[Applicant]:
        conn = None
        try:
            conn = self._get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT ApplicantID, FirstName, LastName, Email, Phone, Resume 
                FROM Applicants
            """)

            applicants = []
            for row in cursor:
                applicants.append(Applicant(
                    applicant_id=row.ApplicantID,
                    first_name=row.FirstName,
                    last_name=row.LastName,
                    email=row.Email,
                    phone=row.Phone,
                    resume=row.Resume
                ))
            return applicants

        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Failed to get applicants: {str(e)}")
        finally:
            if conn: conn.close()

    def get_applications_for_job(self, job_id: int) -> List[JobApplication]:
        conn = None
        try:
            conn = self._get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT ApplicationID, JobID, ApplicantID, ApplicationDate, CoverLetter
                FROM Applications 
                WHERE JobID = ?
            """, job_id)

            applications = []
            for row in cursor:
                applications.append(JobApplication(
                    application_id=row.ApplicationID,
                    job_id=row.JobID,
                    applicant_id=row.ApplicantID,
                    application_date=row.ApplicationDate,
                    cover_letter=row.CoverLetter
                ))
            return applications

        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Failed to get applications: {str(e)}")
        finally:
            if conn: conn.close()

    def calculate_average_salary(self) -> float:
        try:
            jobs = self.get_job_listings()
            if not jobs:
                raise SalaryCalculationException("No jobs available for calculation")

            total = 0
            count = 0
            for job in jobs:
                if job.salary < 0:
                    raise SalaryCalculationException(f"Invalid salary value: {job.salary}")
                total += job.salary
                count += 1

            return total / count

        except SalaryCalculationException as e:
            raise  # Re-raise our custom exception
        except Exception as e:
            raise SalaryCalculationException(f"Error calculating average salary: {str(e)}")

    def upload_resume(self, file_path: str) -> bool:
        try:
            # Basic file validation
            if not file_path:
                raise FileUploadException("No file path provided")

            if not os.path.exists(file_path):
                raise FileUploadException("File not found")

            max_size = 5 * 1024 * 1024  # 5MB
            if os.path.getsize(file_path) > max_size:
                raise FileUploadException("File size exceeds 5MB limit")

            allowed_extensions = ['.pdf', '.doc', '.docx']
            if not any(file_path.lower().endswith(ext) for ext in allowed_extensions):
                raise FileUploadException("Only PDF, DOC, and DOCX files are allowed")

            # In a real app, you would save the file to storage here
            return True

        except FileUploadException as e:
            raise  # Re-raise our custom exception
        except Exception as e:
            raise FileUploadException(f"Error uploading resume: {str(e)}")