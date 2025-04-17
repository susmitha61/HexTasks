import pyodbc
from datetime import date, datetime
from typing import List
from entity.car import Car
from entity.customer import Customer
from entity.lease import Lease
from entity.payment import Payment
from dao.ICarLeaseRepository import ICarLeaseRepository
from exceptions.CarNotFoundException import CarNotFoundException
from exceptions.CustomerNotFoundException import CustomerNotFoundException
from exceptions.LeaseNotFoundException import LeaseNotFoundException


class CarLeaseRepositoryImpl(ICarLeaseRepository):
    def __init__(self):
        self.connection = pyodbc.connect('Driver={SQL Server};'
                                        'Server=HP-15EF2XXX;'
                                        'Database=CarRental;'
                                        'Trusted_Connection=yes;')
        self.conn=self.connection
        self.cursor = self.connection.cursor()
        # inside CarLeaseRepositoryImpl:

    def _map_car(self, row):

        return Car(
            row.vehicleID,
            row.make,
            row.model,
            row.year,
            row.dailyRate,
            row.status,
            row.passengerCapacity,
            row.engineCapacity
        )

    def _map_customer(self, row) -> Customer:
        return Customer(
            firstName=row.firstName,
            lastName=row.lastName,
            email=row.email,
            phoneNumber=row.phoneNumber,
            customerID=row.customerID
        )

    def _map_lease(self, row):
        return Lease(
            leaseID=row.leaseID,
            vehicleID=row.vehicleID,
            customerID=row.customerID,
            startDate=row.startDate,
            endDate=row.endDate,
            returned=row.returned if hasattr(row, 'returned') else False
        )

    def _map_payment(self, row):
        if len(row) >= 4:  # Check if there are enough columns
            return Payment(paymentID=row[0], leaseID=row[1], paymentDate=row[2], amount=row[3])
        else:
            print(f"Unexpected row data: {row}")
            return None

    def add_car(self, car: Car):
        query = """
               INSERT INTO Vehicle (vehicleID, make, model, year, dailyRate, status, passengerCapacity, engineCapacity)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)
           """

        # Generate a new vehicle ID
        vehicle_id = self._get_next_vehicle_id()

        values = (
            vehicle_id,
            car.get_make(),
            car.get_model(),
            int(car.get_year()),
            float(car.get_dailyRate()),
            car.get_status(),
            int(car.get_passengerCapacity()),
            int(car.get_engineCapacity())
        )
        self.cursor.execute(query, values)
        self.connection.commit()
        return vehicle_id
    def _get_next_vehicle_id(self):
        query = "SELECT MAX(vehicleID) FROM Vehicle"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        if result[0] is None:
            return 1
        else:
            return result[0] + 1

    def remove_car(self, vehicleID: int):
        query = "DELETE FROM Vehicle WHERE vehicleID = ?"
        self.cursor.execute(query, (vehicleID,))
        if self.cursor.rowcount == 0:
            raise CarNotFoundException(f"Car with ID {vehicleID} not found.")
        self.connection.commit()

    def list_available_cars(self) -> List[Car]:
        query = "SELECT * FROM Vehicle WHERE status = 'available'"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return [self._map_car(row) for row in rows]

    def list_rented_cars(self) -> List[Car]:
        query = "SELECT * FROM Vehicle WHERE status = 'notAvailable'"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return [self._map_car(row) for row in rows]

    def find_car_by_id(self, vehicleID: int) -> Car:
        query = "SELECT * FROM Vehicle WHERE vehicleID = ?"
        self.cursor.execute(query, (vehicleID,))
        row = self.cursor.fetchone()
        if row:
            return self._map_car(row)
        else:
            raise CarNotFoundException(f"Car with ID {vehicleID} not found.")

    def add_customer(self, customer: Customer):
        query = "INSERT INTO Customer (firstName, lastName, email, phoneNumber) VALUES (?, ?, ?, ?)"
        values = (
            customer.get_firstName(),customer.get_lastName(), customer.get_email(),
            customer.get_phone()
        )
        self.cursor.execute(query, values)
        self.connection.commit()

    def remove_customer(self, customerID: int):
        query = "DELETE FROM Customer WHERE customerID = ?"
        self.cursor.execute(query, (customerID,))
        if self.cursor.rowcount == 0:
            raise CustomerNotFoundException(f"Customer with ID {customerID} not found.")
        self.connection.commit()

    def list_customers(self) -> List[Customer]:
        query = "SELECT * FROM Customer"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return [self._map_customer(row) for row in rows]

    def find_customer_by_id(self, customerID: int) -> Customer:
        query = "SELECT * FROM Customer WHERE customerID = ?"
        self.cursor.execute(query, (customerID,))
        row = self.cursor.fetchone()
        if row:
            return self._map_customer(row)
        else:
            raise CustomerNotFoundException(f"Customer with ID {customerID} not found.")

    from datetime import datetime

    def create_lease(self, customerID: int, vehicleID: int, startDate: str, endDate: str, lease_type: str) -> Lease:
        # Ensure dates are properly converted into datetime.date format
        try:
            # Check if startDate is a string, and convert if necessary
            if isinstance(startDate, str):
                start_date = datetime.strptime(startDate, '%Y-%m-%d').date()
            else:
                start_date = startDate  # Already a date object

            # Check if endDate is a string, and convert if necessary
            if isinstance(endDate, str):
                end_date = datetime.strptime(endDate, '%Y-%m-%d').date()
            else:
                end_date = endDate  # Already a date object
        except ValueError as e:
            raise Exception(f"Invalid date format: {e}")

        # Convert dates to string format (YYYY-MM-DD)
        start_date_str = start_date.strftime('%Y-%m-%d')
        end_date_str = end_date.strftime('%Y-%m-%d')

        # Find the car and customer
        car = self.find_car_by_id(vehicleID)
        customer = self.find_customer_by_id(customerID)

        # Check if the car is available
        if car.get_status() != 'available':
            raise Exception(f"Car with ID {vehicleID} is not available.")

        # Prepare the query to insert the lease
        query = """
            INSERT INTO Lease (vehicleID, customerID, startDate, endDate, type)
            VALUES (?, ?, ?, ?, ?)
        """
        values = (vehicleID, customerID, start_date_str, end_date_str, lease_type)

        try:
            # Execute the query and commit the transaction
            self.cursor.execute(query, values)
            self.connection.commit()

            # Retrieve the last inserted lease ID
            leaseID = self.cursor.lastrowid

            # Update the car's status to 'notAvailable'
            self.update_car_status(vehicleID, 'notAvailable')

            # Return the created Lease object
            return Lease(leaseID=leaseID, vehicleID=vehicleID, customerID=customerID, startDate=start_date,
                         endDate=end_date)

        except Exception as e:
            # Handle any database errors
            self.connection.rollback()
            raise Exception(f"Error occurred while creating lease: {e}")

    def update_car_status(self, vehicleID: int, status: str):
        query = "UPDATE Vehicle SET status = ? WHERE vehicleID = ?"
        self.cursor.execute(query, (status, vehicleID))
        self.connection.commit()

    def return_car(self, leaseID: int):
        query = """
            UPDATE Lease
            SET returned = 1  -- Assuming 1 means 'returned' and the column is of type BIT
            WHERE leaseID = ?
        """
        try:
            self.cursor.execute(query, (leaseID,))
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise Exception(f"Error occurred while returning car: {e}")

    def _find_lease_by_id(self, leaseID: int) -> Lease | None:
        query = "SELECT * FROM Lease WHERE leaseID = ?"
        self.cursor.execute(query, (leaseID,))
        row = self.cursor.fetchone()
        if row:
            return self._map_lease(row)
        return None

    def list_active_leases(self):
        try:
            query = "SELECT * FROM Lease WHERE returned = 0"
            self.cursor.execute(query)
            leases = self.cursor.fetchall()

            if not leases:
                print("No active leases found.")
                return []

            active_leases = []
            for lease in leases:
                lease_obj = Lease(leaseID=lease[0], vehicleID=lease[1], customerID=lease[2],
                                  startDate=lease[3], endDate=lease[4], type=lease[5], returned=lease[6])
                active_leases.append(lease_obj)

            return active_leases
        except Exception as e:
            print(f"Error retrieving active leases: {e}")
            return []

    def list_lease_history(self):
        try:
            query = "SELECT leaseID, vehicleID, customerID, startDate, endDate, type, returned FROM Lease"
            self.cursor.execute(query)
            leases = self.cursor.fetchall()

            if not leases:
                print("No lease history found.")
                return []

            lease_history = []
            for lease in leases:
                # Pass the correct order and arguments to the Lease constructor
                lease_obj = Lease(leaseID=lease[0], vehicleID=lease[1], customerID=lease[2],
                                  startDate=lease[3], endDate=lease[4], type=lease[5], returned=lease[6])
                lease_history.append(lease_obj)

            return lease_history
        except Exception as e:
            print(f"Error retrieving lease history: {e}")
            return []

    # Method to record payment (with manual paymentID)
    def record_payment(self, lease: Lease, amount: float):
        if not self._find_lease_by_id(lease.leaseID):  # Validate if lease exists
            raise LeaseNotFoundException(f"Lease with ID {lease.leaseID} not found.")

        # Fetch the highest paymentID and increment
        self.cursor.execute("SELECT MAX(paymentID) FROM Payment")
        max_payment_id = self.cursor.fetchone()[0] or 0  # Use 0 if no records exist
        new_payment_id = max_payment_id + 1

        query = "INSERT INTO Payment (paymentID, leaseID, amount) VALUES (?, ?, ?)"
        values = (new_payment_id, lease.leaseID, amount)
        self.cursor.execute(query, values)
        self.connection.commit()
        print(f"Payment of {amount} recorded for Lease ID {lease.leaseID}, Payment ID: {new_payment_id}.")

    def get_payment_history(self, customerID: int) -> List[Payment]:
        query = """
            SELECT p.paymentID, p.leaseID, p.paymentDate,p.amount
            FROM Payment p
            JOIN Lease l ON p.leaseID = l.leaseID
            WHERE l.customerID = ?
        """
        self.cursor.execute(query, (customerID,))
        rows = self.cursor.fetchall()

        # Debugging: Check the structure of the rows
        print(f"Retrieved rows: {rows}")

        return [self._map_payment(row) for row in rows]

    def calculate_total_revenue(self) -> float:
        query = "SELECT SUM(amount) FROM Payment"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0] if result[0] else 0.0

    def get_lease_by_id(self, leaseID: int) -> Lease:
        query = "SELECT leaseID, vehicleID, customerID, startDate, endDate, type , returned FROM Lease WHERE leaseID = ?"
        try:
            self.cursor.execute(query, (leaseID,))
            row = self.cursor.fetchone()

            if row:
                return Lease(
                    leaseID=row.leaseID,
                    vehicleID=row.vehicleID,
                    customerID=row.customerID,
                    startDate=row.startDate,
                    endDate=row.endDate,
                    type=row.type,
                    returned=row.returned
                )
            else:
                raise LeaseNotFoundException(f"Lease with ID {leaseID} not found.")
        except LeaseNotFoundException:
            # Let this propagate so your test can catch it
            raise
        except Exception as e:
            raise Exception(f"Error fetching lease with ID {leaseID}: {e}")
