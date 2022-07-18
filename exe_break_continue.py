# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:57:49 2020

@author: user
"""


largest_number = -9999999
counter = 0

number = int(input("enter a number or type -1 to end program: "))

#using break
#while True:
#    if number == -1:
#        break
#    counter +=1
#    if number > largest_number:
#        largest_number = number
#    number = int(input("enter a number or type -1 to end program: "))

#using continue
while number != -1:
    if number == -1:
        continue
    counter += 1
    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter == 0:
    print("\nYou have not entered any numbers!")
elif counter == 1:
    print("\nYou have only entered a number!")
else:
    print("\nYou have entered", counter, "numbers. Great job!")

if counter != 0:
    print("The largest number is", largest_number)
    
