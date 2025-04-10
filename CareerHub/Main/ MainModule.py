import pyodbc
from datetime import datetime

from entity.model.Applicant import Applicant
from entity.model.Company import Company
from entity.model.JobApplication import JobApplication
from entity.model.JobListing import JobListingManager, JobListing
from util.DBPropertyUtil import DBPropertyUtil

def main():
    try:
        # Database connection setup
        db = DBPropertyUtil('HP-15EF2XXX', 'CareerHub')  # Ensure DBPropertyUtil is properly configured
        connection = db.connect()  # Ensure the connection is established
        print("Database connection established successfully!")

        # Initialize JobListingManager
        job_manager = JobListingManager()

        # Create job listings (simulating in-memory for this example)
        job1 = JobListing(job_id=12, company_id=1, job_title="Software Engineer",
                          job_description="Develop software solutions", job_location="New York", salary=120000,
                          job_type="Full-time")
        job2 = JobListing(job_id=22, company_id=1, job_title="Data Analyst", job_description="Analyze data and reports",
                          job_location="San Francisco", salary=110000, job_type="Full-time")

        # Add job listings to the manager
        job_manager.add_job(job1)
        job_manager.add_job(job2)

        # Display all job listings
        print("All Job Listings:")
        for job in job_manager.job_listings:
            print(job.get_job_details())

        # Place job listing into the database
        job1.place_job(connection)

        # Update job listing
        job2.job_title = "Senior Data Analyst"  # Update job title
        job2.update_job(connection, job2.job_id)

        # Display updated job listing
        print("\nUpdated Job Listings:")
        for job in job_manager.job_listings:
            print(job.get_job_details())

        # Remove a job
        job_manager.remove_job(22)

        # Display remaining job listings
        print("\nRemaining Job Listings after Removal:")
        for job in job_manager.job_listings:
            print(job.get_job_details())

        # Create a new company
        company_name = "TechCorp"
        location = "San Francisco"
        Company.create_company(connection, company_name, location)

        # Read all companies
        print("\nAll Companies:")
        companies = Company.read_all_companies(connection)
        for company in companies:
            print(company)

        # Read a company by ID
        company_id = 1  # Replace with an actual CompanyID from your database
        company = Company.read_company_by_id(connection, company_id)
        if company:
            print(f"\nCompany with ID {company_id}: {company}")
        else:
            print(f"\nCompany with ID {company_id} not found.")

        # Update a company
        updated_name = "TechCorp Ltd."
        updated_location = "Seattle"
        Company.update_company(connection, company_id, company_name=updated_name, location=updated_location)

        # Example: Delete a company
        Company.delete_company(connection, company_id)

        # Create a new applicant with resume
        print("\nCreating a new applicant...")
        Applicant.create_applicant(connection, "John", "Doe", "john.doe@example.com", "1234567890", "path/to/resume.pdf")

        # Read and display all applicants
        print("\nFetching all applicants...")
        applicants = Applicant.read_all_applicants(connection)
        for applicant in applicants:
            print(applicant)

        # Read a specific applicant by ID
        applicant_id = 1  # Replace with an actual ApplicantID from your database
        print(f"\nFetching applicant with ID {applicant_id}...")
        applicant = Applicant.read_applicant_by_id(connection, applicant_id)
        if applicant:
            print(f"Found Applicant: {applicant}")
        else:
            print(f"Applicant with ID {applicant_id} not found.")

        # Update an applicant's details, including resume
        print(f"\nUpdating applicant with ID {applicant_id}...")
        Applicant.update_applicant(connection, applicant_id, first_name="Jane", last_name="Smith", resume="path/to/updated_resume.pdf")

        # Delete an applicant
        print(f"\nDeleting applicant with ID {applicant_id}...")
        Applicant.delete_applicant(connection, applicant_id)

        # Fetch valid ApplicantID and JobID from the database
        applicant_id = JobApplication.get_valid_applicant_id(connection)
        job_id = JobApplication.get_valid_job_id(connection)

        if not applicant_id or not job_id:
            print("Valid ApplicantID or JobID not found in the database.")
            return

        print(f"Using ApplicantID: {applicant_id}, JobID: {job_id}")

        # Create a new job application
        print("\nCreating a new job application...")
        cover_letter = "This is my cover letter for the job application."
        JobApplication.create_application(connection, job_id, applicant_id, cover_letter, "Applied")

        # Fetch and display all job applications
        print("\nFetching all job applications...")
        applications = JobApplication.read_all_applications(connection)
        for application in applications:
            print(application)

        # Fetch a specific job application by ID
        application_id = 2  # Replace with an actual ApplicationID from your database
        print(f"\nFetching job application with ID {application_id}...")
        application = JobApplication.read_application_by_id(connection, application_id)
        if application:
            print(f"Found Application: {application}")
        else:
            print(f"JobApplication with ID {application_id} not found.")

        # Update a job application's status and cover letter
        print(f"\nUpdating job application with ID {application_id}...")
        new_cover_letter = "Updated cover letter text."
        JobApplication.update_application(connection, application_id, status="Under Review", cover_letter=new_cover_letter)

        # Delete a job application
        print(f"\nDeleting job application with ID {application_id}...")
        JobApplication.delete_application(connection, application_id)

        # Close the connection
        connection.close()
        print("\nDatabase connection closed.")

    except pyodbc.Error as e:
        print(f"Error connecting to database: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
