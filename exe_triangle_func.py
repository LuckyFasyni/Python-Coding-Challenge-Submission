# -*- coding: utf-8 -*-
"""
Created on Tue May 26 20:55:24 2020

@author: user
"""

##is it a triangle
def isItATriangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(isItATriangle(1, 1, 1))
print(isItATriangle(1, 1, 3))

#compact version
def isItATriangle1(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

print(isItATriangle1(1, 1, 1))
print(isItATriangle1(1, 1, 3))

##more compact version
def isItATriangle2(a, b, c):
    return a + b > c and a + c > b and b + c > a

print(isItATriangle2(1, 1, 1))
print(isItATriangle2(1, 1, 3))

#right angle triangle
def RightTriangle(a, b, c):
    if isItATriangle(a, b, c) == False:
        return False
    if a > b and a > c:
        return a**2 == b**2 + c**2
    if b > a and b > c:
        return b**2 == a**2 + c**2
    if c > a and c > b:
        return c**2 == a**2 + b**2

a = float(input("Enter the first side's length: "))
b = float(input("Enter the second side's length: "))
c = float(input("Enter the third side's length: "))

print(RightTriangle(a, b, c))

#evaluating triangle field
def heron(a, b, c):
    s = (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5

def fieldOfTriangle(a, b, c):
    if not isItATriangle(a, b, c):
        return None
    return heron(a, b, c)

print(fieldOfTriangle(1., 1., 2. ** .5))
