# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 17:10:37 2020

@author: user
"""

text = input("enter a palindrome: ")
lst = []
for letter in text:
    if letter.isalpha():
        letter = letter.upper()
        lst.append(letter)
lst2 = lst[::-1]
if lst == lst2:
    print('It\'s a palindrome')
else:
    print('It\'s not a palindrome')
