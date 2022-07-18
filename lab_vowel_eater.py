# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:28:32 2020

@author: user
"""

#Ugly Vowel Eater
#user must input a word
#print the uneaten letters (non vowel)to the screen, each one of them on a separate line.

import time

userWord = input("enter a word: ")# Prompt the user to enter a word
userWord = userWord.upper()# and assign it to the userWord variable.

for letter in userWord:# Complete the body of the for loop.
    if letter in ("A", "I", "U", "E", "O"):
        continue
    print(letter)
    time.sleep(1)

#Pretty Vowel Eater
WordWithoutVowel = ""

for letter in userWord:
    if letter in ("A", "I", "U", "E", "O"):
        continue
    WordWithoutVowel += letter
    
print(WordWithoutVowel)