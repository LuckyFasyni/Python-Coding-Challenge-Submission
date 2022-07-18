# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:22:05 2020

@author: user
"""

#macam cara import modul

import math #you can use all entities in modul by: math.pi or math.sin

from math import sin, pi #you can use this specific entities without calling itss module: sin or pi
#but don't create any new variables using this name

from math import * #you can use all entities without calling itss module: sin or pi
#but don't create any new variables using this name
#YOU HAVE TO KNOW NAMES OF ENTIRE ENTITIES IN THE MODULE

import math as m #giving alias to module name

from math import sin as s, pi as p #giving alias to entities' name

#example
from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

from math import e, exp, log, log10, log2

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

print(log(1000, 10))
print(log10(1000))

print(log(16, 2))
print(log2(16))

print(log(2)) #natural logartithm or log(2, e)
print(log(2) == log(2, e))

from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))

#example 2
from random import random

#The most general function named random() (not to be confused with the module's name) produces a float number x coming from the range (0.0, 1.0) - in other words: (0.0 <= x < 1.0).
for i in range(5):
    print(random())
    
from random import random, seed

seed(0) #seed() function is able to directly set the generator's seed

for i in range(5):
    print(random())
    
from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

from random import randint, choice, sample

for i in range(10):
    print(randint(1, 10), end=',')
    
lst = [i for i in range(1, 11)]

#if you want the result is unique
print(choice(lst))
print(sample(lst, 5))
print(sample(lst, 10))

from platform import platform, machine, processor, system, version

#platform(aliased=0, terse=0) atau platform(aliased=False, terse=False)
print(platform())
print(platform(1))
print(platform(0, 1))

print(machine()) #know the generic name of the processor which runs your OS together with Python and your code
print(processor())
print(system())
print(version())

from platform import python_implementation, python_version_tuple

print(python_implementation()) #returns a string denoting the Python implementation (expect CPython here, unless you decide to use any non-canonical Python branch)

for atr in python_version_tuple(): #returns a three-element tuple 
    print(atr)
#the major part of Python's version;
#the minor part;
#the patch level number.
