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
