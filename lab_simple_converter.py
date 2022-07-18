# -*- coding: utf-8 -*-
"""
Created on Thu May 14 10:34:05 2020

@author: user
"""

#Length
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers/1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#Kurs
usd = float(input("Drop USD in your pocket: "))
eur = float(input("Well, now your Euro: "))

eur_to_usd = eur*1.08
usd_to_eur = usd/1.08

print(usd, "USD is", round(usd_to_eur, 2), "Euro")
print(eur, "Euro is", round(eur_to_usd, 2), "USD")

#Temperature
temperature = float(input("Your body temperature: "))
unit = str(input("Celcius or Fahrenheit? (type with lower cases) "))

if unit == "celcius":
    celcius_to_fahrenheit = temperature*(9/5)+32
    print("Your body temperature is", round(temperature, 1), "Celcius, or equal to", round(celcius_to_fahrenheit, 1), "Fahrenheit") 
else:
    fahrenheit_to_celcius = temperature*(5/9)-32
    print("Your body temperature is", round(temperature, 1), "Fahrenheit, or equal to", round(fahrenheit_to_celcius, 1), "Celcius")