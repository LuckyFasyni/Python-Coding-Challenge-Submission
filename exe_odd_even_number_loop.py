# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:50:46 2020

@author: user
"""

# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

number = int(input("enter a number or type 0 to stop: "))

#alternatif
#while number != 0:
while number:
    #if number % 2 == 1:
    if number % 2:
        odd_numbers += 1
    else:
        even_numbers +=1
    number = int(input("enter a number or type 0 to stop: "))

print("Odd numbers are", odd_numbers)
print("Even numbers are", even_numbers)

print("")

#using counter
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)