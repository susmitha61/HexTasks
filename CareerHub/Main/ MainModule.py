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

         print("Adding a new job listing...")
        job_listing = JobListing(
            job_id=None,
            company_id=1,
            job_title="Software Engineer",
            job_description="Develop and maintain software applications.",
            job_location="New York",
             salary=95000.0,
            job_type="Full-time"
           )
        job_listing.create_job_listing(connection, job_listing.company_id, job_listing.job_title,
                                   job_listing.job_description, job_listing.job_location,
                                   job_listing.salary, job_listing.job_type)

          # Read all job listings
          print("\nReading all job listings...")
          job_listings = JobListing.read_all_job_listings(connection)
         for job in job_listings:
              print(job.get_job_details())

          # Read a specific job listing by ID
          job_id_to_read = 1  # Assuming you want to read a job with ID 1
          print(f"\nReading job listing with ID {job_id_to_read}...")
         job_listing = JobListing.read_job_listing_by_id(connection, job_id_to_read)
         if job_listing:
             print(job_listing.get_job_details())
          else:
               print(f"Job with ID {job_id_to_read} not found.")

         # Update an existing job listing
         job_id_to_update = 1  # Assuming you want to update job with ID 1
         print(f"\nUpdating job listing with ID {job_id_to_update}...")
         JobListing.update_job_listing(connection, job_id_to_update, job_title="Senior Software Engineer")

         # Delete a job listing
         job_id_to_delete = 1  # Assuming you want to delete job with ID 1
          print(f"\nDeleting job listing with ID {job_id_to_delete}...")
          JobListing.delete_job_listing(connection, job_id_to_delete)



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
