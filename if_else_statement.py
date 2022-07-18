# -*- coding: utf-8 -*-
"""
Created on Thu May 14 22:21:02 2020

@author: user
"""

#Scenario
#if the citizen's income was not higher than 85,528 thalers, 
#the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was the so-called tax relief)
#if the income was higher than this amount, 
#the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.

income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = ((18/100)*income) - 556
elif income > 85528:
    tax = 14839 + ((32/100)*(income-85528))

if tax < 0.:
    tax = 0.
    
tax = round(tax, 0)
print("The tax is:", tax, "thalers")