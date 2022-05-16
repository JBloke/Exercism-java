#!/usr/bin/env python3

# Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven and the number of gallons used. Print a nice message with the answer.

miles = int(input("Enter the number of miles  driven: "))
number_of_gallons = int(input("Enter the number of gallons used: "))
mpg = miles / number_of_gallons
print("The mpg of the car is", mpg, "mpg")

