# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:05:13 2020

@author: user
"""

#Scenario
#A junior magician has picked a secret number. He has hidden it in a variable named secret_number. 
#He wants everyone who run his program to play the Guess the secret number game, 
#and guess what number he has picked for them. 
#Those who don't guess the number will be stuck in an endless loop forever!

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input("guess the secret number: "))

while number != secret_number:
    print("ha ha! You're stuck in my loop!")
    number = int(input("guess the secret number: "))
    
print("Well done, muggle! You are free now.")