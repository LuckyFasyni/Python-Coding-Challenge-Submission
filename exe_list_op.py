# -*- coding: utf-8 -*-
"""
Created on Sat May 23 23:57:31 2020

@author: user
"""

list1 = [1]
list2 = list1
list1[0] = 2
print(list2)

list3 = [1]
list4 = list3[:]
list3[0] = 2
print(list4)

list5 = [2, 4, 6, 8, 10]

list6 = list5[2:4]
print(list6)

list7 = list5[1:-1]
print(list7)

list8 = list5[-1:1]
print(list8)

list9 = list5[2:]
print(list9)

list10 = list5[:2]
print(list10)

myList = [1, 2, 3, 4, 5]
del myList[:]
print(myList)

myList2 = [1, 2, 3, 4, 5]
del myList2[1:3]
print(myList2)

del myList2
print(myList2)

myList3 = [0, 3, 12, 8, 2]

print(5 in myList3)
print(5 not in myList3)
print(12 in myList3)