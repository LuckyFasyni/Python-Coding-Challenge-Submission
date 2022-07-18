# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 23:41:51 2020

@author: user
"""

from os import strerror

srcfl = input('Input a file: ')
try:
    stream = open(srcfl, 'rt')
    content = stream.read().lower()
except IOError as exc:
    print(strerror(exc.errno))

x = srcfl.find('.txt')
dstfl = srcfl.replace('.txt', '.hist.txt')  
try: 
    storm = open(dstfl, 'wt')
except IOError as exc:
    print(strerror(exc.errno))
    stream.close()

lst = []
dct = {}
for char in content:
    if char.isalpha():
        lst.append(char)
lst = sorted(lst)
for char in lst:
    dct[char] = lst.count(char)
#dct = sorted(dct.items(), key = lambda x : x[1])
for char, count in sorted(dct.items(), key = lambda x : x[1], reverse = True):
    storm.write(char + ' --> ' + str(count) + '\n')

storm.close()
stream.close()