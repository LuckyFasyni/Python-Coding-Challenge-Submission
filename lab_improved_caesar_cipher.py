# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 16:51:22 2020

@author: user
"""

#improved caesar cipher

text = input('Input one line to encrypt: ')
shift = int(input('Input shift value: '))
cipher = ''
for letter in text:
    if not letter.isalpha():
        cipher += letter
    else:
        digit = ord(letter) + shift
        if letter.isupper():
            if digit <= ord('Z'):
                cipher += chr(digit)
            else:
                digit = ord('A') + (digit - ord('Z')) - 1
                cipher+= chr(digit)
        if letter.islower():
            if digit <= ord('z'):
                cipher += chr(digit)
            else:
                digit = ord('a') + (digit - ord('z')) - 1
                cipher+= chr(digit)
print(cipher)