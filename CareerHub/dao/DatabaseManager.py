from dao.JobBoardServiceImpl import JobBoardServiceImpl
from entity.JobListing import JobListing
from entity.Company import Company
from entity.Applicant import Applicant
from entity.JobApplication import JobApplication

class DatabaseManager:
    def __init__(self, connection_string: str):
        self.job_board_service = JobBoardServiceImpl(connection_string)

    def initialize_database(self):
        """
        Initializes the database schema and tables.
        This method can execute SQL scripts to create tables (if necessary).
        For simplicity, this is left as a placeholder. You can add scripts to create necessary tables.
        """
        try:
            connection = self.job_board_service._get_connection()
            cursor = connection.cursor()
            # Example of table creation - you can modify based on your actual schema.
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Jobs (
                    JobID INT PRIMARY KEY,
                    CompanyID INT,
                    JobTitle VARCHAR(255),
                    JobDescription TEXT,
                    JobLocation VARCHAR(255),
                    Salary DECIMAL(10, 2),
                    JobType VARCHAR(50),
                    PostedDate DATETIME
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Companies (
                    CompanyID INT PRIMARY KEY,
                    CompanyName VARCHAR(255),
                    Location VARCHAR(255)
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Applicants (
                    ApplicantID INT PRIMARY KEY,
                    FirstName VARCHAR(255),
                    LastName VARCHAR(255),
                    Email VARCHAR(255),
                    Phone VARCHAR(20),
                    Resume TEXT
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Applications (
                    ApplicationID INT PRIMARY KEY,
                    JobID INT,
                    ApplicantID INT,
                    ApplicationDate DATETIME,
                    CoverLetter TEXT
                );
            """)
            connection.commit()
            connection.close()
        except Exception as e:
            print(f"Error initializing database: {e}")
            raise

    def insert_job_listing(self, job: JobListing):
        self.job_board_service.insert_job_listing(job)

    def insert_company(self, company: Company):
        self.job_board_service.insert_company(company)

    def insert_applicant(self, applicant: Applicant):
        self.job_board_service.insert_applicant(applicant)

    def insert_job_application(self, application: JobApplication):
        self.job_board_service.insert_job_application(application)

    def get_job_listings(self):
        return self.job_board_service.get_job_listings()

    def get_companies(self):
        return self.job_board_service.get_companies()

    def get_applicants(self):
        return self.job_board_service.get_applicants()

    def get_applications_for_job(self, jobID: int):
        return self.job_board_service.get_applications_for_job(jobID)
