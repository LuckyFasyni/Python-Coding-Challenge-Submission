# -*- coding: utf-8 -*-
"""
Created on Tue May 19 22:50:24 2020

@author: user
"""

#Collatz's hypothesis
#The hypothesis says that regardless of the initial value of c0, it will always go to 1.

c0 = int(input("enter a non-negative and non-zero number: "))
step = 0

while True:
    if c0 % 2 == 0:
        c0 /= 2
    else:
        c0 = 3*c0 + 1
    print(int(c0))
    step += 1
    if c0 == 1:
        break
    
print("steps =", step)