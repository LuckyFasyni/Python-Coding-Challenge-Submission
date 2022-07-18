# -*- coding: utf-8 -*-
"""
Created on Tue May 26 20:49:53 2020

@author: user
"""

#two parameter function
def lbtokg(lb):
    return lb*0.45359237

def ftintom(ft, inch=0.0):
    return ft*0.3048 + inch*0.0254

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2

print(bmi(lbtokg(176), ftintom(5, 7)))

#compact version
def bmi(lb, ft, inch=0.0):
    w = lb*0.45359237
    h = ft*0.3048 + inch*0.0254
    if h < 1.0 or h > 2.5 or \
    w < 20 or w > 200:
        return None
    
    return w / h ** 2

print(bmi(176, 5, 7))