# -*- coding: utf-8 -*-
"""
Created on Tue May 26 22:22:59 2020

@author: user
"""

#recursion
#method of solving a problem where the solution 
#depends on solutions to smaller instances of the same problem

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(7))

def Factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n*Factorial(n-1)

print(Factorial(5))

def factorial(n):
    return n * factorial(n - 1)

print(factorial(4)) #ERROR krn ga ada kondisi

def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)

print(fun(25))