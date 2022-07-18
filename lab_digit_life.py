# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 21:37:37 2020

@author: user
"""

#the digit of life
birthdate = input("Enter your birthdate (DDMMYYYY): ")
while len(birthdate) != 1:
    digit = 0
    for i in birthdate:
        digit += int(i)
    birthdate = str(digit)
else:
    print(birthdate)