# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 22:52:51 2020

@author: user
"""

from os import strerror

srcfl = input('Input a file for counter: ')
try:
    stream = open(srcfl, 'rt')
    content = stream.read().lower()
except IOError as exc:
    print(strerror(exc.errno)) 
    
#print(content)
lst = []
dct = {}
for char in content:
    if char.isalpha():
        lst.append(char)
lst = sorted(lst)
for char in lst:
    dct[char] = lst.count(char)
for char, count in dct.items():
    print(char, '-->', count)
    
stream.close()
