""" 31-03-2025"""
"""Task 1 : Accept the temparature in celsius and convert the same in farenheit."""
c=int(input("Enter the temperature :"))
f=(c*(9/5)+32)
print("The temperature after conversion from celsius to farenheit is ",f)
"""Task 2 : Write a python program to find the area of a cube."""
c=int(input("Enter the side of the cube :"))
a=(c*c*c)
print("Area of the cube is ",a)
""""Task 3 : Write a python program to find the area of a cylinder."""
r=float(input("Enter the radius of the circle :"))
h=float(input("Enter the height of the circle:"))

a=(2*3.14*r*h)+(2*3.14*r*r)
print("Area of the cylinder is ",a)
"""Task 4:Write a python program to enter a number and display its hex and octal equivalant values and its square root."""

import math
dec=int(input("Enter the number:"))
print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")
print(math.sqrt(dec), "is the square root of",dec)

"""Task 5 : Write a python program to print the digit at one's place of a number
          for eg: if the input is 12345 the output should be 5"""

num=int(input("Enter the number:"))
r=num%10
print("The ones digit of the number is",r)

Task 6 : Write a python program to print the memory location of two variables and
         find if the variables are using similar memory space or not.
	 use: identity operator in the code.

num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
if id(num1)==id(num2):
   print("same memory space")
else:
    print("No different memory space")
  
"""Task 7 : Write a program to input the radius of the sphere and calculate its volume """
import math
r=int(input("Enter the radius :"))
p=math.pi
v=(4/3)*(p*r*r*r )
print("Volume of sphere",v)
"""Write a python program to calculate the amoount payable after the simple intrest."""
r=int(input("Enter the rate :"))
p=int(input("enter principal amount: "))
t=int(input("enter time: "))
a=(p*r*t)/100
print("Simple interest is ",a)
"""Task 9 : Write a python program to calculate amount payable after compound intrest."""
import math
r=int(input("Enter the rate :"))
p=int(input("enter principal amount: "))
n=int(input("enter time: "))
c=r/100
a=p*(1+pow(r,n))-p
print("Compound interest is ",a)
"""
import csv
import pandas as pd
import json

# Task 1: Bank Class
class Bank:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance: {self.balance}")
        else:
            print("Insufficient balance.")

# Task 2: Student Marks Class
class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_marks(self, marks_list):
        self.marks = marks_list

    def get_total_marks(self):
        return sum(self.marks)

# Task 3: Rectangle Class
class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def area(self):
        return self.__length * self.__breadth

# Task 4: Student Information Class
class StudentDetails:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.marks = {}

    def add_marks(self, subject, marks):
        self.marks[subject] = marks

    def total_marks(self):
        return sum(self.marks.values())

# Task 5: Store Class with Product and Billing
class Store:
    def __init__(self):
        self.products = {
            1: {'name': 'Item A', 'price': 10},
            2: {'name': 'Item B', 'price': 20},
            3: {'name': 'Item C', 'price': 30}
        }

    def display_products(self):
        print("Products Available:")
        for code, product in self.products.items():
            print(f"Code: {code}, Name: {product['name']}, Price: {product['price']}")

    def generate_bill(self, quantities):
        total = 0
        for code, quantity in quantities.items():
            product = self.products[code]
            total += product['price'] * quantity
        print(f"Total Bill: {total}")

# Task 6: File Handling (CSV, Excel, and Text Files)
def read_csv(filename):
    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

def read_excel(filename):
    data = pd.read_excel(filename)
    print(data)

def read_text(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)

# Task 7: JSON Handling (Create and Convert JSON to Text File)
def create_json():
    data = {"name": "John", "age": 30, "city": "New York"}
    with open("data.json", "w") as json_file:
        json.dump(data, json_file)

def convert_json_to_text():
    with open("data.json", "r") as json_file:
        json_data = json.load(json_file)
        with open("data.txt", "w") as text_file:
            text_file.write(str(json_data))

# Task 8: Convert CSV to Excel
def convert_csv_to_excel(csv_filename, excel_filename):
    data = pd.read_csv(csv_filename)
    data.to_excel(excel_filename, index=False)

# Example Usage of Task 1 to 5:
if __name__ == "__main__":
    # Task 1: Bank Class
    bank_account = Bank()
    bank_account.deposit(500)
    bank_account.withdraw(200)

    # Task 2: Student Marks Class
    student = Student("Alice")
    student.add_marks([90, 85, 88])
    print(f"Total marks for {student.name}: {student.get_total_marks()}")

    # Task 3: Rectangle Class
    rect = Rectangle(5, 4)
    print(f"Area of the rectangle: {rect.area()}")

    # Task 4: Student Information Class
    student_details = StudentDetails(1, "John")
    student_details.add_marks("Math", 85)
    student_details.add_marks("Science", 90)
    print(f"Total marks for {student_details.name}: {student_details.total_marks()}")

    # Task 5: Store Class with Product and Billing
    store = Store()
    store.display_products()
    quantities = {1: 2, 2: 1, 3: 3}
    store.generate_bill(quantities)

    # Task 6: File Handling (Example)
    # Assuming files 'data.csv' and 'data.xlsx' exist
    read_csv('data.csv')
    read_excel('data.xlsx')
    read_text('data.txt')

    # Task 7: JSON Handling (Create and Convert JSON to Text File)
    create_json()
    convert_json_to_text()

    # Task 8: Convert CSV to Excel
    convert_csv_to_excel('data.csv', 'data.xlsx')

"""
