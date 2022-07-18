# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 22:44:12 2020

@author: user
"""

class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def makePizza(pizza, cheese):
	if pizza not in ['margherita', 'capricciosa', 'calzone']:
		raise PizzaError(pizza, "no such pizza on the menu")
	if cheese > 100:
		raise TooMuchCheeseError(pizza, cheese, "too much cheese")
	print("Pizza ready!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
	try:
		makePizza(pz, ch)
	except TooMuchCheeseError as tmce:
		print(tmce, ':', tmce.cheese)
	except PizzaError as pe:
		print(pe, ':', pe.pizza)
		

class burgerError(Exception):
    def __init__(self, burger, message):
        super().__init__(message) # we can write as Exception.__init__(self, message) too
        self.burger = burger
        
class tooMuchMeat(burgerError):
    def __init__(self, burger, meat, message):
        super().__init__(burger, message)
        self.meat = meat
        
def makeBurger(burger, meat):
    if burger not in ['BigMac', 'Mac', 'SuperMac']:
        raise burgerError(burger, 'There is no such burger on the menu')
    if meat > 10:
        raise tooMuchMeat(burger, meat, 'That is too much meat')
    print('Pizza ready!')

for (burger, meat) in [('Mac', 8), ('SuperBigMac', 4), ('BigMac', 13)]:
    try:
        makeBurger(burger, meat)
    except tooMuchMeat as tmm:
        print(tmm, ':', tmm.meat)
    except burgerError as be:
        print(be, ':', be.burger)