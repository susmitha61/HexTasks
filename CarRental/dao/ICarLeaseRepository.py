from abc import ABC, abstractmethod


# Abstract class
class ICarLeaseRepository(ABC):

    @abstractmethod
    def add_car(self, car):
        pass

    @abstractmethod
    def add_customer(self, customer):
        pass

    @abstractmethod
    def create_lease(self, customer_id, car_id, start_date, end_date, lease_type):
        pass

    @abstractmethod
    def find_car_by_id(self, car_id):
        pass

    @abstractmethod
    def find_customer_by_id(self, customer_id):
        pass

    @abstractmethod
    def list_active_leases(self):
        pass

    @abstractmethod
    def list_available_cars(self):
        pass

    @abstractmethod
    def list_customers(self):
        pass

    @abstractmethod
    def list_lease_history(self):
        pass

    @abstractmethod
    def list_rented_cars(self):
        pass

    @abstractmethod
    def record_payment(self, lease, amount):
        pass

    @abstractmethod
    def remove_car(self, car_id):
        pass

    @abstractmethod
    def remove_customer(self, customer_id):
        pass

    @abstractmethod
    def return_car(self, lease_id):
        pass

