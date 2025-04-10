import pyodbc
from datetime import datetime

class JobListing:
    def __init__(self, job_id: int, company_id: int, job_title: str,
                 job_description: str, job_location: str, salary: float,
                 job_type: str, posted_date=None):
        self.__job_id = job_id
        self.__company_id = company_id
        self.__job_title = job_title
        self.__job_description = job_description
        self.__job_location = job_location
        self.__salary = salary
        self.__job_type = job_type
        self.__posted_date = posted_date if posted_date else datetime.now()

    def __str__(self):
        return f"Job ID: {self.job_id}, Title: {self.job_title}, Location: {self.job_location}"

    def place_job(self, db_connector):
        query = """
            INSERT INTO dbo.JobListings (CompanyID, JobTitle, JobDescription, 
                                         JobLocation, Salary, JobType, PostedDate)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        db_connector.execute_query(query, (self.company_id, self.job_title,
                                           self.job_description, self.job_location,
                                           self.salary, self.job_type, self.posted_date))
        print(f"Job '{self.job_title}' added successfully.")

        # Check if the job was added
        check_query = "SELECT * FROM dbo.JobListings WHERE JobTitle = ? AND CompanyID = ?"
        result = db_connector.execute_query(check_query, (self.job_title, self.company_id))
        if result:
            print(f"Job successfully inserted: {result}")
        else:
            print("Job insertion failed!")

    @staticmethod
    def read_jobs(db_connector):
        query = "SELECT * FROM dbo.JobListings"
        return db_connector.fetch_query(query)

    def update_job(self, db_connector, job_id):
        # Update query
        query = """
            UPDATE dbo.JobListings 
            SET JobTitle=?, JobDescription=?, JobLocation=?, Salary=?, JobType=? 
            WHERE JobID=?
        """
        try:
            db_connector.execute_query(query, (self.job_title, self.job_description,
                                               self.job_location, self.salary, self.job_type, job_id))

            print(f"Job '{job_id}' updated successfully.")

            # Verifying the job update with a SELECT query (after commit)
            select_query = "SELECT * FROM dbo.JobListings WHERE JobID = ?"
            result = db_connector.execute_query(select_query, (job_id,))

            if result:
                print(f"Job updated: {result}")
            else:
                print(f"Error updating job '{job_id}'.")

        except Exception as e:
            print(f"Error during job update: {e}")

    def remove_job(self, db_connector, job_id):
        query = "DELETE FROM dbo.JobListings WHERE JobID=?"
        db_connector.execute_query(query, (job_id,))

        # Verify the job is removed
        check_query = "SELECT * FROM dbo.JobListings WHERE JobID = ?"
        result = db_connector.execute_query(check_query, (job_id,))
        if result:
            print(f"Job '{job_id}' not deleted.")
        else:
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

    # Getters
    @property
    def job_id(self):
        return self.__job_id

    @property
    def company_id(self):
        return self.__company_id

    @property
    def job_title(self):
        return self.__job_title

    @property
    def job_description(self):
        return self.__job_description

    @property
    def job_location(self):
        return self.__job_location

    @property
    def salary(self):
        return self.__salary

    @property
    def job_type(self):
        return self.__job_type

    @property
    def posted_date(self):
        return self.__posted_date

# Setters
    @job_id.setter
    def job_id(self, value):
        self.__job_id = value

    @company_id.setter
    def company_id(self, value):
        self.__company_id = value

    @job_title.setter
    def job_title(self, value):
        self.__job_title = value

    @job_description.setter
    def job_description(self, value):
        self.__job_description = value

    @job_location.setter
    def job_location(self, value):
        self.__job_location = value

    @salary.setter
    def salary(self, value):
        self.__salary = value

    @job_type.setter
    def job_type(self, value):
        self.__job_type = value

    @posted_date.setter
    def posted_date(self, value):
        self.__posted_date = value

    def __str__(self):
        return f"JobListing(job_id={self.job_id}, title='{self.job_title}')"



