# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 12:32:29 2020

@author: user
"""

#lambda
#penggunaan map
list1 = [x for x in range(5)]
list2 = list(map(lambda x: 2 ** x, list1))
print(list2)
for x in map(lambda x: x * x, list2):
	print(x, end=' ')
print()

#jika tidak menggunakan lambda
lst = []
for x in range(5):
    a = 2 ** x
    lst.append(a)
print(lst)

for x in lst:
    a = x * x
    print(a, end = " ")
    
    
# contoh penggunaan filter
from random import seed, randint

seed(0)
data = [ randint(-10,10) for x in range(5) ]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
print(data)
print(filtered)