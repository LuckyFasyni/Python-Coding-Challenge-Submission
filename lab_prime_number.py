# -*- coding: utf-8 -*-
"""
Created on Mon May 25 22:19:49 2020

@author: user
"""

#write a function checking whether a number is prime or not
def isPrime(num):
    if num > 1:
        if num == 2:
            n = True
        else:
            for i in range(2, num):
                if num % i == 0:
                    n = False
                    break
                else:
                    n = True
        return n
    
#print(isPrime(9))
for i in range(1, 89):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()
