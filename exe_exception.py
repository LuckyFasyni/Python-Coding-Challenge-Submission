# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:18:19 2020

@author: user
"""

#EKSEPSI
#PENANGANAN ERROR

##contoh 1
#fn = int(input())
#sn = int(input())
#
#try:
#    print(fn/sn)
#except:
#    print("The operation cannot be done")
#    
#print("The End.")
#
##contoh 2
#try:
#    print("1") #this block is executed
#    x = 1/0 #this expression cannot be done, so jump to except
#    print("2")
#except:
#    print("something has wrong")
#print("3")
#
##contoh 3
#try:
#    x = int(input("Masukin angka: "))
#    y  = 1/x
#    print(y)
#except ZeroDivisionError:
#    print("Gabisa dibagi 0 elah")
#except ValueError:
#    print("ya angka lah")
#except: #error selain yg sudah disebutkan di atas
#    print("Dah gw bingung salahnya apa")
#print("Kelar.")
#
##contoh 4
#def badFun(n):
#    try:
#        return 1 / n
#    except ArithmeticError:
#        print("Arithmetic Problem!")
#    return None
#
#badFun(0)
#
##contoh 5
#def badfun(n):
#    return 1 / n
#
#try:
#    badfun(0)
#except ArithmeticError:
#    print("An exception has been raised!")
#
#print("The End!")
#
##contoh 6
#def badfun(n):
#    try:
#        return n / 0
#    except:
#        print("Ada yang salah!")
#        raise
#        
#try:
#    badfun(1)
#except NameError:
#    print("I see name error")
#except ArithmeticError:
#    print("I see!")
#    
#print("The End")
#
##contoh 7
#import math
#
#try:
#    x = float(input("Enter x: "))
#    y = math.sqrt(x)
#    print("The square root of", x, "equals to", y)
#except:
#    print("Enter a positive number!")
#
##anatomy of exception
##contoh 1
#
#try:
#    y = 1 / 0
#except ZeroDivisionError:
#    print("Oooppsss...")
#
#print("THE END.")
#
#try:
#    y = 1 / 0
#except ArithmeticError: #a general class including zerodivision error
#    print("Oooppsss...")
#
#print("THE END.")
#
##contoh 2
#try:
#    y = 1 / 0
#except ZeroDivisionError:
#    print("Zero Division!")
#except ArithmeticError:
#    print("Arithmetic problem!")
#
#print("THE END.")
#
##compare with
#try:
#    y = 1 / 0
#except ArithmeticError:
#    print("Arithmetic problem!")
#except ZeroDivisionError:
#    print("Zero Division!")
#
#print("THE END.")
#
##contoh raise
#def badFun(n):
#    raise ZeroDivisionError #simulate raising actual exceptions
#
#try:
#    badFun(0)
#except ArithmeticError:
#    print("What happened? An error?")
#
#print("THE END.")
#
##contoh raise 2
#def badFun1(n):
#    try:
#        return n/0
#    except:
#        print("I did it again!")
#        raise
#        
#try:
#    badFun1(0)
#except ArithmeticError:
#    print("I see!")
#    
#print("THE END.")

#contoh assert

import math

x = int(input("Enter a number: "))
assert x >= 0

x = math.sqrt(x)

print(x)

#def readint(prompt, min, max):
#    a = False
#    while not a:
#        try:
#            x = int(input(prompt))
#            a = True
#        except ValueError:
#            print("error: wrong input")
#            continue
#        if a:
#            a = x >= min and x <= max
#        if not a:
#            print("Error: the value is not within permitted range (" + str(min) + ".." + str(max) + ")")
#    return x
#    
#v = readint("Enter a number from -10 to 10: ", -10, 10)
#
#print("The number is:", v)