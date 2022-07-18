# -*- coding: utf-8 -*-
"""
Created on Tue May 26 22:08:44 2020

@author: user
"""

#Fibonacci number

#my own version
def fib(n):
    if n > 0:
        prod = []
        for i in range(1, n+1):
            if i < 3:
                x = 1
                prod.append(x)
            if i >= 3:
                x = prod[i-2] + prod[i-3]
                prod.append(x)
        return x

#print(fib(3))        
for i in range(10): #testing
    print(i, "->", fib(i))
    
#netacad version    
def fib2(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

print()
for n in range(1, 10): # testing
    print(n, "->", fib2(n))
