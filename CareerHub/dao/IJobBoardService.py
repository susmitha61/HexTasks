from abc import ABC, abstractmethod
from entity.model.JobListing import JobListing
from entity.model.Company import Company
from entity.model.Applicant import Applicant
from entity.model.JobApplication import JobApplication

class IJobBoardService(ABC):

    @abstractmethod
    def insert_job_listing(self, job: JobListing):
        pass

    @abstractmethod
    def insert_company(self, company: Company):
        pass

    @abstractmethod
    def insert_applicant(self, applicant: Applicant):
        pass

    @abstractmethod
    def insert_job_application(self, application: JobApplication):
        pass

    @abstractmethod
    def get_job_listings(self):
        pass

    @abstractmethod
    def get_companies(self):
        pass

    @abstractmethod
    def get_applicants(self):
        pass

    @abstractmethod
    def get_applications_for_job(self, jobID: int):
        pass
