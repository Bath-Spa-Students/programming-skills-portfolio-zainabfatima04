#Write a Python program to display the current date and time.

#Importing datetime module for now()
import datetime

#Using now() to get current time
current_time = datetime.datetime.now()

#Printing attributes of now()
print("The attribute of now() are")
print("Year :", current_time.year)
print("Month :", current_time.month)
print("Day :", current_time.day)
print("Hour :", current_time.hour)
print("Minute :", current_time.minute)
print("Second :", current_time.second)