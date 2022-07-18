# -*- coding: utf-8 -*-
"""
Created on Mon May 25 16:42:38 2020

@author: user
"""

a = []

def printing():
    while True:
        print("Please enter a number or 0 if you want to stop: ")
        x = int(input())
        if x != 0:
            a.append(x)
        else:
            break
    a.sort()
    print(a)

printing()

#function(parameter)
def pythagoras(a, b):
    c = (a**2 + b**2)**(1/2)
    print("Panjang sisi miring segitiga siku-sikunya adalah", c)
    
#function(arguments)
pythagoras(3, 4)

#memungkinkan untuk variabel bernama sama dengan parameter fungsi yang ada
b = 17
print(b)

#keyword passing argument
pythagoras(6, 8)
pythagoras(b = 8, a = 6)

def intro(firstName, surName):
    print("Hello, my name is", firstName, surName)
    
intro("Lucky", "Fasyni")
intro(surName = "Fasyni", firstName = "Lucky")

#parametrized function
def footballer(firstName, surName, number = 7):
    print(firstName, surName + "'s number is", number)
    
footballer("Thomas", "Muller", 25)
footballer("Cristiano", "Ronaldo")
footballer(surName = "Hazard", firstName = "Eden")
footballer("Luka", number = 9, surName = "Jovic")

#exercise
def intric(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intric()
intric(b="Sean Connery")

def eintracht(a, b="Bond"):
    print("My name is", b + ".", a + ".")

eintracht("Susan")

def sum(a, b=2, c):
    print(a + b + c)

sum(a=1, c=3)
#result is error because a non-default argument (c) follows a default argument (b=2)