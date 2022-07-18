# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:16:39 2020

@author: user
"""

#def wishes():
#    print("My wishes")
#    return "Happy Birthday!"
#    
#wishes()
#w = wishes()
#print(w)
#print(wishes())

#var = 2
#print(var)    # outputs: 2
#
#def retVar():
#    global var
#    var = 5
#    return var
#
#print(retVar())    # outputs: 5
#var = 3
#print(var)    # outputs: 5

#print(1 // 2)
#
#z = 0
#y = 10
#x = z > y and y < z or z < y and y > z
#print(x)
#
#x = 1
#y = 2
#x, y, z = x, x, y
#z, y, z = x, y, z
#
#print(x, y, z)
#
#print(0%2)

#print(None*None)
#
#def func(a, b):
#    return b**a
#
#print(func(b = 2, 2))

dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="")
#    
#print()
    
#nums = [1, 2, 3]
#vals = nums
#del vals[:]
#print(nums)
#print(vals)

#print(1%2)
#print(2%1)
#
#def fun(x):
#    if x % 2 == 0:
#        return 1
#    else:
#        return 2
#    
#print(fun(fun(2)))

#tup = (1, 2, 3)
#
#tup[1] = tup[1] + tup[0]

#lst = [i for i in range(-1, -2)]
#print(lst)
#
#print("a", "b", "c", sep = "sep")
#
#print(1 // 5 + 1 / 5)
#
#tup = (1, 2, 4, 8)
#tup = tup[-2:-1]
#tup = tup[-1]
#print(tup)
#
#a = 1
#b = 0
#a = a ^ b
#b = a ^ b
#a = a ^ b
#
#print(a, b)

#dd = {"1" : "0", "0" : "1"}
#for x in dd.vals():
#    print(x, end = "")
    
#def func(a, b):
#    return b ** a
#print(func(b = 2, 2))

#print(4**(1/2))
#
#def fun(inp=2, uup = 3):
#    return inp * uup
#print(fun(uup=2))

#lst = [[x for x in range(3)] for y in range(3)]
#
#for r in range(3):
#    for c in range(3):
#        if lst[r][c] % 2 != 0:
#            print("#")

#i = 0
#while i < i + 2:
#    i += 1
#    print("*")
#else:
#    print("*")

print()

lst = [i for i in range(-1, -2)]
print(len(lst))