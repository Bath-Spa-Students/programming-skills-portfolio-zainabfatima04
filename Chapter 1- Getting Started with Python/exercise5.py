#Write a Python program which accepts the radius of a circle from the user and compute the area.
#Import the math module for the constant pi
import math

#Asking the user for radius
radius = float(input("Enter the radius of the circle: "))

#Calculate the area
area = math.pi * (radius ** 2)

#Print the result
print("The area of the circle is:", area)