#Write a Python program which accepts the radius of a circle from the user and computes the area.

#Import the math module for the constant pi
import math

# Accept the radius from the user
radius_str = input("Enter the radius of the circle: ")

# Convert the input to a floating-point number
radius = float(radius_str)

# Compute the area of the circle using the formula: area = π * r^2
area = math.pi * radius**2

# Print the result
print(f"The area of the circle with radius {radius} is: {area}")