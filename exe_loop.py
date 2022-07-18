# -*- coding: utf-8 -*-
"""
Created on Tue May 19 23:01:34 2020

@author: user
"""

#Create a for loop that counts from 0 to 10
#prints odd numbers to the screen.

for i in range(1, 10):
    if i % 2 != 0:
        print(i)
        
#Create a while loop that counts from 0 to 10
#prints odd numbers to the screen

x = 1

while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1
    
#Create a program with a for loop and a break statement. 
#The program should iterate over characters in an email address, 
#exit the loop when it reaches the @ symbol
#print the part before @ on one line

for ch in "luckyfasyni@gmail.com":
    if ch == "@":
        break
    print(ch, end="")
    
#Create a program with a for loop and a continue statement
#The program should iterate over a string of digits
#replace each 0 with x
#print the modified string to the screen

for digit in "0165031806510":
    if digit == "0":
        digit = "x"
    print(digit, end="")
    
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")