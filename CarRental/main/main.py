import pyodbc
from datetime import date
from entity.car import Car
from entity.customer import Customer
from entity.lease import Lease
from entity.payment import Payment

from dao.CarLeaseRepositoryImpl import CarLeaseRepositoryImpl
from exceptions.CarNotFoundException import CarNotFoundException
from exceptions.CustomerNotFoundException import CustomerNotFoundException
from exceptions.LeaseNotFoundException import LeaseNotFoundException


def main():
    try:
        # Create an instance of CarLeaseRepositoryImpl
        repo = CarLeaseRepositoryImpl()

        while True:
            print("\n=== Car Rental Management System ===")
            print("1. Manage Cars")
            print("2. Manage Customers")
            print("3. Manage Leases")
            print("4. Manage Payments")
            print("0. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                manage_cars(repo)
            elif choice == '2':
                manage_customers(repo)
            elif choice == '3':
                manage_leases(repo)
            elif choice == '4':
                manage_payments(repo)
            elif choice == '0':
                print("🔚 Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    except pyodbc.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def manage_cars(repo):
    print("\n--- Manage Cars ---")
    print("1. Add Car")
    print("2. Remove Car")
    print("3. List Available Cars")
    print("4. List Rented Cars")
    print("5. Find Car by ID")
    choice = input("Enter your choice: ")

    if choice == '1':
        # Inside your main.py, within the "Add Car" option handling:

        make = input("Enter car make: ")
        model = input("Enter car model: ")
        year = input("Enter car year: ")
        daily_rate = input("Enter daily rental rate: ")
        status = input("Enter car status ('available' or 'notAvailable'): ")
        passenger_capacity = input("Enter passenger capacity: ")
        engine_capacity = input("Enter engine capacity: ")

        try:
            car = Car(None, make, model, int(year), float(daily_rate), status, int(passenger_capacity),
                      int(engine_capacity))
            repo.add_car(car)
            print("Car added successfully.")
        except ValueError:
            print(
                "Invalid input. Please enter valid numbers for year, daily rate, passenger capacity, and engine capacity.")
    elif choice == '2':
        vehicle_id = int(input("Enter car ID to remove: "))
        try:
            repo.remove_car(vehicle_id)
            print("Car removed successfully!")
        except CarNotFoundException as e:
            print(e)
    elif choice == '3':
        cars = repo.list_available_cars()
        for car in cars:
            print(car)
    elif choice == '4':
        cars = repo.list_rented_cars()
        for car in cars:
            print(car)
    elif choice == '5':
        vehicle_id = int(input("Enter car ID: "))
        try:
            car = repo.find_car_by_id(vehicle_id)
            print(car)
        except CarNotFoundException as e:
            print(e)
    else:
        print("Invalid option")


def manage_customers(repo):
    print("\n--- Manage Customers ---")
    print("1. Add Customer")
    print("2. Remove Customer")
    print("3. List Customers")
    print("4. Find Customer by ID")
    choice = input("Enter your choice: ")

    if choice == '1':
        firstname = input("Enter first name: ")
        lastname=input("Enter last name: ")
        email = input("Enter customer email: ")
        phone = input("Enter customer phone: ")
        customer = Customer(firstname,lastname, email, phone)
        repo.add_customer(customer)
        print("Customer added successfully!")
    elif choice == '2':
        customer_id = int(input("Enter customer ID to remove: "))
        try:
            repo.remove_customer(customer_id)
            print("Customer removed successfully!")
        except CustomerNotFoundException as e:
            print(e)
    elif choice == '3':
        customers = repo.list_customers()
        for customer in customers:
            print(customer)
    elif choice == '4':
        customer_id = int(input("Enter customer ID: "))
        try:
            customer = repo.find_customer_by_id(customer_id)
            print(customer)
        except CustomerNotFoundException as e:
            print(e)
    else:
        print("Invalid option")


def manage_leases(repo):
    print("\n--- Manage Leases ---")
    print("1. Create Lease")
    print("2. Return Car")
    print("3. List Active Leases")
    print("4. List Lease History")
    choice = input("Enter your choice: ")

    if choice == '1':
        customer_id = int(input("Enter customer ID: "))
        vehicle_id = int(input("Enter vehicle ID: "))
        start_date = input("Enter lease start date (YYYY-MM-DD): ")
        end_date = input("Enter lease end date (YYYY-MM-DD): ")
        lease_type = input("Enter lease type: ")
        start_date = date.fromisoformat(start_date)
        end_date = date.fromisoformat(end_date)
        try:
            lease = repo.create_lease(customer_id, vehicle_id, start_date, end_date, lease_type)
            print(f"Lease created successfully! Lease ID: {lease.get_leaseID()}")
        except (CarNotFoundException, CustomerNotFoundException) as e:
            print(e)
    elif choice == '2':
        lease_id = int(input("Enter lease ID to return car: "))
        try:
            repo.return_car(lease_id)
            print("Car returned successfully!")
        except LeaseNotFoundException as e:
            print(e)
    elif choice == '3':
        leases = repo.list_active_leases()
        for lease in leases:
            print(lease)
    elif choice == '4':
        leases = repo.list_lease_history()
        for lease in leases:
            print(lease)
    else:
        print("Invalid option")


def manage_payments(repo):
    print("\n--- Manage Payments ---")
    print("1. Record Payment")
    print("2. View Payment History")
    print("3. Total Revenue")
    choice = input("Enter your choice: ")

    if choice == '1':
        lease_id = int(input("Enter lease ID for payment: "))
        amount = float(input("Enter payment amount: "))
        try:
            lease = repo._find_lease_by_id(lease_id)
            repo.record_payment(lease, amount)
            print("Payment recorded successfully!")
        except LeaseNotFoundException as e:
            print(e)
    elif choice == '2':
        customer_id = int(input("Enter customer ID: "))
        payments = repo.get_payment_history(customer_id)
        for payment in payments:
            print(payment)
    elif choice == '3':  # Updated choice for total revenue
        total_revenue = repo.calculate_total_revenue()  # Call on repo instance
        print(f"Total revenue from payments: {total_revenue:.2f}")
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
