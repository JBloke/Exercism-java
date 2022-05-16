#!/usr/bin/env python3
# Write a Python program that assigns the principal amount of 10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8% (0.08). Then have the program prompt the user for the number of years, t, that the money will be compounded for. Calculate and print the final amount after t years.

principal = int(input("Enter the principal amount "))
n = int(input("Enter the n value "))
rate = int(input("Enter the interest rate ")) 
rate = rate / 100
time = int(input("Enter the time (number of year) "))
final_amount = principal * (1 + rate / n) ** (n * time)
print("The final amount after", time, "years is",final_amount)

