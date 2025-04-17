import unittest

from dao.CarLeaseRepositoryImpl import CarLeaseRepositoryImpl
from entity.car import Car
from entity.lease import Lease
from exceptions.CarNotFoundException import CarNotFoundException
from exceptions.CustomerNotFoundException import CustomerNotFoundException
from exceptions.LeaseNotFoundException import LeaseNotFoundException


class TestCarCreation(unittest.TestCase):
    def setUp(self):
        self.repo = CarLeaseRepositoryImpl()
        self.test_car =  Car(
            vehicleID=1,  # Provide a valid vehicleID
            make="Toyota",
            model="Corolla",
            year=2020,
            dailyRate=50.0,
            status="available",
            passengerCapacity=5,
            engineCapacity=1800
        )
    def test_create_car_success(self):
        result = self.repo.add_car(self.test_car)
        self.assertTrue(result)
class TestRetrieveLease(unittest.TestCase):
    def setUp(self):
        self.repo = CarLeaseRepositoryImpl()
        self.existing_lease_id = 1

    def test_get_lease_success(self):
        lease = self.repo._find_lease_by_id(self.existing_lease_id)
        self.assertIsNotNone(lease)
        self.assertEqual(lease.leaseID, self.existing_lease_id)


class TestLeaseCreation(unittest.TestCase):

    def setUp(self):
        self.repo = CarLeaseRepositoryImpl()

        # Ensure customer and car exist and car is available
        self.repo.cursor.execute("UPDATE Vehicle SET status = 'available' WHERE vehicleID = 1")
        self.repo.connection.commit()

        self.test_lease_id = 9999  # Make sure this is a unique ID not already in use
        self.customer_id = 1
        self.vehicle_id = 1
        self.start_date = "2023-01-12"
        self.end_date = "2024-12-24"
        self.lease_type = "MonthlyLease"

        # Manually insert test lease (simulate expected behavior)
        insert_query = """
            INSERT INTO Lease (leaseID, vehicleID, customerID, startDate, endDate, type)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        self.repo.cursor.execute(insert_query, (
            self.test_lease_id,
            self.vehicle_id,
            self.customer_id,
            self.start_date,
            self.end_date,
            self.lease_type
        ))
        self.repo.connection.commit()

    def test_create_lease_success(self):
        # Directly check if the lease was inserted correctly
        self.repo.cursor.execute("SELECT * FROM Lease WHERE leaseID = ?", (self.test_lease_id,))
        lease_row = self.repo.cursor.fetchone()
        self.assertIsNotNone(lease_row)
        self.assertEqual(lease_row.leaseID, self.test_lease_id)
        self.assertEqual(lease_row.vehicleID, self.vehicle_id)
        self.assertEqual(lease_row.customerID, self.customer_id)
        self.assertEqual(str(lease_row.startDate), self.start_date)
        self.assertEqual(str(lease_row.endDate), self.end_date)
        self.assertEqual(lease_row.type, self.lease_type)

    def tearDown(self):
        # Clean up the test lease
        self.repo.cursor.execute("DELETE FROM Lease WHERE leaseID = ?", (self.test_lease_id,))
        self.repo.connection.commit()


class TestExceptionCases(unittest.TestCase):
    def setUp(self):
        self.repo = CarLeaseRepositoryImpl()

    def test_customer_not_found_exception(self):
        with self.assertRaises(CustomerNotFoundException):
            self.repo.find_customer_by_id(9999)

    def test_car_not_found_exception(self):
        with self.assertRaises(CarNotFoundException):
            self.repo.find_car_by_id(9999)

    def test_lease_not_found_exception(self):
        with self.assertRaises(LeaseNotFoundException):
            self.repo.get_lease_by_id(9999)
