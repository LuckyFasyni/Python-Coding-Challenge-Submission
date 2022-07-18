# -*- coding: utf-8 -*-
"""
Created on Thu May 14 22:39:00 2020

@author: user
"""

#Scenario(Leap year)
#Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:
#if the year number isn't divisible by four, it's a common year;
#otherwise, if the year number isn't divisible by 100, it's a leap year;
#otherwise, if the year number isn't divisible by 400, it's a common year;
#otherwise, it's a leap year.

year = int(input("Enter a year: "))

if year>=1582:
    if year%4 != 0:
        print("Common year")
    elif year%100 != 0:
        print("Leap year")
    elif year%400 != 0:
        print("Common year")
    else:
        print("Leap year")
else:
    print("Not within the Gregorian calendar period")