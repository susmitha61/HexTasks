import pyodbc
from datetime import datetime

class JobListing:
    def __init__(self, job_id=None, company_id=None, job_title=None, job_description=None,
                 job_location=None, salary=None, job_type=None, posted_date=None):
        self.__job_id = job_id
        self.__company_id = company_id
        self.__job_title = job_title
        self.__job_description = job_description
        self.__job_location = job_location
        self.__salary = salary
        self.__job_type = job_type
        self.__posted_date = posted_date if posted_date else datetime.now()

    # Getters
    @property
    def job_id(self): return self.__job_id

    @property
    def company_id(self): return self.__company_id

    @property
    def job_title(self): return self.__job_title

    @property
    def job_description(self): return self.__job_description

    @property
    def job_location(self): return self.__job_location

    @property
    def salary(self): return self.__salary

    @property
    def job_type(self): return self.__job_type

    @property
    def posted_date(self): return self.__posted_date

    # Setters
    @job_id.setter
    def job_id(self, value): self.__job_id = value

    @company_id.setter
    def company_id(self, value): self.__company_id = value

    @job_title.setter
    def job_title(self, value): self.__job_title = value

    @job_description.setter
    def job_description(self, value): self.__job_description = value

    @job_location.setter
    def job_location(self, value): self.__job_location = value

    @salary.setter
    def salary(self, value): self.__salary = value

    @job_type.setter
    def job_type(self, value): self.__job_type = value

    @posted_date.setter
    def posted_date(self, value): self.__posted_date = value

    # CRUD Methods

    @staticmethod
    def get_connection():
        connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=YOUR_SERVER;DATABASE=YOUR_DATABASE;Trusted_Connection=yes'
        return pyodbc.connect(connection_string)

    # Create Job Listing
    @staticmethod
    def create_job_listing(connection, company_id, job_title, job_description, job_location, salary, job_type):
        query = """
            INSERT INTO dbo.JobListings (CompanyID, JobTitle, JobDescription, 
                                         JobLocation, Salary, JobType, PostedDate)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor = connection.cursor()
        cursor.execute(query, (company_id, job_title, job_description, job_location, salary, job_type, datetime.now()))
        connection.commit()
        print(f"Job '{job_title}' added successfully.")

    # Read Job Listings
    @staticmethod
    def read_all_job_listings(connection):
        query = "SELECT * FROM dbo.JobListings"
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        
        job_listings = []
        for row in result:
            job_listing = JobListing(job_id=row[0], company_id=row[1], job_title=row[2], job_description=row[3],
                                     job_location=row[4], salary=row[5], job_type=row[6], posted_date=row[7])
            job_listings.append(job_listing)
        return job_listings

    @staticmethod
    def read_job_listing_by_id(connection, job_id):
        query = "SELECT * FROM dbo.JobListings WHERE JobID = ?"
        cursor = connection.cursor()
        cursor.execute(query, (job_id,))
        result = cursor.fetchone()
        
        if result:
            return JobListing(job_id=result[0], company_id=result[1], job_title=result[2], job_description=result[3],
                              job_location=result[4], salary=result[5], job_type=result[6], posted_date=result[7])
        return None

    # Update Job Listing
    @staticmethod
    def update_job_listing(connection, job_id, job_title=None, job_description=None, job_location=None, salary=None, job_type=None):
        query = """
            UPDATE dbo.JobListings 
            SET JobTitle = ?, JobDescription = ?, JobLocation = ?, Salary = ?, JobType = ?
            WHERE JobID = ?
        """
        cursor = connection.cursor()
        cursor.execute(query, (job_title, job_description, job_location, salary, job_type, job_id))
        connection.commit()
        print(f"Job '{job_id}' updated successfully.")

    # Delete Job Listing
    @staticmethod
    def delete_job_listing(connection, job_id):
        query = "DELETE FROM dbo.JobListings WHERE JobID = ?"
        cursor = connection.cursor()
        cursor.execute(query, (job_id,))
        connection.commit()
        print(f"Job '{job_id}' deleted successfully.")

    def get_job_details(self) -> str:
        return (
            f"Job ID: {self.job_id}, "
            f"Company ID: {self.company_id}, "
            f"Title: {self.job_title}, "
            f"Location: {self.job_location}, "
            f"Salary: {self.salary}, "
            f"Type: {self.job_type}, "
            f"Posted on: {self.posted_date}"
        )

    def __str__(self):
        return f"JobListing(job_id={self.job_id}, title='{self.job_title}')"
