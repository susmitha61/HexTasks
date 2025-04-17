import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from unittest import mock
from datetime import datetime
from entity.model.JobListing import JobListing
from entity.model.Company import Company
from entity.model.Applicant import Applicant
from entity.model.JobApplication import JobApplication
from dao.IJobBoardService import IJobBoardService
from dao.JobBoardServiceImpl import JobBoardServiceImpl
from execeptions.DatabaseConnectionException import DatabaseConnectionException

class TestCareerHub:
    def test_sample_test(self):
        """Sample test case"""
        assert 1 == 1

    @mock.patch("dao.JobBoardServiceImpl.JobBoardServiceImpl._get_connection")
    def test_insert_job_listing_success(self, mock_get_connection):
        """Test inserting a new job listing successfully"""
        mock_connection = mock_get_connection.return_value
        mock_cursor = mock_connection.cursor.return_value
        job_board_service = JobBoardServiceImpl()
        mock_cursor.execute.return_value = None
        mock_connection.commit.return_value = None
        job = JobListing(company_id=1, job_title="Software Engineer", job_description="Develop software",
                         job_location="Remote", salary=120000, job_type="Full-Time", posted_date=datetime.now())
        result = job_board_service.insert_job_listing(job)
        assert result is True
        mock_cursor.execute.assert_called_once()
        mock_connection.commit.assert_called_once()

    @mock.patch("dao.JobBoardServiceImpl.JobBoardServiceImpl._get_connection")
    def test_insert_job_listing_failure(self, mock_get_connection):
        """Test inserting a new job listing failure due to database error"""
        mock_get_connection.side_effect = DatabaseConnectionException("Database error")
        job_board_service = JobBoardServiceImpl()
        job = JobListing(company_id=1, job_title="Software Engineer", job_description="Develop software",
                         job_location="Remote", salary=120000, job_type="Full-Time", posted_date=datetime.now())
        with pytest.raises(DatabaseConnectionException) as excinfo:
            job_board_service.insert_job_listing(job)
        assert "Failed to insert job listing" in str(excinfo.value)

    @mock.patch("dao.JobBoardServiceImpl.JobBoardServiceImpl._get_connection")
    def test_get_job_listings_success(self, mock_get_connection):
        """Test retrieving all job listings successfully"""
        mock_connection = mock_get_connection.return_value
        mock_cursor = mock_connection.cursor.return_value
        job_board_service = JobBoardServiceImpl()
        mock_cursor.fetchall.return_value = [
            (1, 1, "Software Engineer", "Develop software", "Remote", 120000, "Full-Time", datetime.now()),
            (2, 2, "Data Analyst", "Analyze data", "Hybrid", 90000, "Full-Time", datetime.now()),
        ]
        job_listings = job_board_service.get_job_listings()
        assert len(job_listings) == 2
        assert isinstance(job_listings[0], JobListing)
        assert job_listings[0].job_title == "Software Engineer"
        assert job_listings[1].job_title == "Data Analyst"
        mock_cursor.execute.assert_called_once_with("""
            SELECT JobID, CompanyID, JobTitle, JobDescription, 
                            JobLocation, Salary, JobType, PostedDate 
            FROM Jobs
        """)

    @mock.patch("dao.JobBoardServiceImpl.JobBoardServiceImpl._get_connection")
    def test_get_job_listings_empty(self, mock_get_connection):
        """Test retrieving no job listings when the table is empty"""
        mock_connection = mock_get_connection.return_value
        mock_cursor = mock_connection.cursor.return_value
        job_board_service = JobBoardServiceImpl()
        mock_cursor.fetchall.return_value = []
        job_listings = job_board_service.get_job_listings()
        assert len(job_listings) == 0
        mock_cursor.execute.assert_called_once_with("""
            SELECT JobID, CompanyID, JobTitle, JobDescription, 
                            JobLocation, Salary, JobType, PostedDate 
            FROM Jobs
        """)

if __name__ == '__main__':
    pytest.main(['-v', '--tb=line', __file__])
    print("Application submitted successfully!")
