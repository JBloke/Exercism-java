#!/usr/bin/env python3

# It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights you would return home on a Saturday (day 6) Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of day of the week you will return on.

day_leave = int(input("Enter the day you leave (0-6)? "))
return_date = int(input("Enter the day you return? "))

day_return = (day_leave + return_date) % 7
print(day_return)
