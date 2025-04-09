import pyodbc
from datetime import datetime

class JobApplication:
    def __init__(self, application_id=None, job_id=None, applicant_id=None, application_date=None, cover_letter=None, status=None):
        self.__application_id = application_id
        self.__job_id = job_id
        self.__applicant_id = applicant_id
        self.__application_date = application_date if application_date else datetime.now()
        self.__cover_letter = cover_letter
        self.__status = status

    # Getters
    @property
    def application_id(self): return self.__application_id
    @property
    def job_id(self): return self.__job_id
    @property
    def applicant_id(self): return self.__applicant_id
    @property
    def application_date(self): return self.__application_date
    @property
    def cover_letter(self): return self.__cover_letter
    @property
    def status(self): return self.__status

    # Setters
    @application_id.setter
    def application_id(self, value): self.__application_id = value
    @job_id.setter
    def job_id(self, value): self.__job_id = value
    @applicant_id.setter
    def applicant_id(self, value): self.__applicant_id = value
    @application_date.setter
    def application_date(self, value): self.__application_date = value
    @cover_letter.setter
    def cover_letter(self, value): self.__cover_letter = value
    @status.setter
    def status(self, value): self.__status = value

    def __str__(self):
        return f"JobApplication(application_id={self.application_id}, job_id={self.job_id}, applicant_id={self.applicant_id}, status={self.status})"

    # Fetch valid ApplicantID and JobID from database
    @staticmethod
    def get_valid_applicant_id(connection):
        cursor = connection.cursor()
        cursor.execute("SELECT TOP 1 ApplicantID FROM Applicants")
        row = cursor.fetchone()
        return row[0] if row else None

    @staticmethod
    def get_valid_job_id(connection):
        cursor = connection.cursor()
        cursor.execute("SELECT TOP 1 JobID FROM JobListings")
        row = cursor.fetchone()
        return row[0] if row else None

    # CRUD Operations
    @staticmethod
    def create_application(connection, job_id, applicant_id, cover_letter, status=None):
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO Applications (JobID, ApplicantID, CoverLetter, Status)
            VALUES (?, ?, ?, ?)
        """, (job_id, applicant_id, cover_letter, status))
        connection.commit()
        print(f"Job application created with JobID {job_id} and ApplicantID {applicant_id}.")

    @staticmethod
    def read_all_applications(connection):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Applications")
        rows = cursor.fetchall()
        applications = [JobApplication(application_id=row[0], job_id=row[1], applicant_id=row[2], application_date=row[3], cover_letter=row[4], status=row[5]) for row in rows]
        return applications

    @staticmethod
    def read_application_by_id(connection, application_id):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Applications WHERE ApplicationID = ?", (application_id,))
        row = cursor.fetchone()
        if row:
            return JobApplication(application_id=row[0], job_id=row[1], applicant_id=row[2], application_date=row[3], cover_letter=row[4], status=row[5])
        return None

    @staticmethod
    def update_application(connection, application_id, status=None, cover_letter=None):
        cursor = connection.cursor()
        if status:
            cursor.execute("UPDATE Applications SET Status = ? WHERE ApplicationID = ?", (status, application_id))
        if cover_letter:
            cursor.execute("UPDATE Applications SET CoverLetter = ? WHERE ApplicationID = ?", (cover_letter, application_id))
        connection.commit()
        print(f"Job application {application_id} updated.")

    @staticmethod
    def delete_application(connection, application_id):
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Applications WHERE ApplicationID = ?", (application_id,))
        connection.commit()
        print(f"Job application {application_id} deleted.")
