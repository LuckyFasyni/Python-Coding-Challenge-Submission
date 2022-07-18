# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:54:11 2020

@author: user
"""

'''
komentra multilineeeeeeeeeeee
woi
woi
'''

#demmonstrating ord and chr
ch1 = 'a'
ch2 = ' '

print(ord(ch1))
print(ord(ch2))

print(chr(97))
print(chr(32))
print(chr(97864))

#lower() untuk mengubah kapital menjadi lower case
yey = "CIKARANG"
vokal = ['a', 'i', 'u', 'e', 'o']
for i in range(len(yey)):
    if yey[i].lower() in vokal:
        continue
    else:
        print(yey[i], end='')
print()
print(yey.lower())

#mencari indeks suatu string
print(yey.index('K'))

#iterating through a string
for ch in yey:
    print(ch, end="-")
print()

#bukti string immutable
s = ['s', 'a', 'b']
ss = 'sab'
try:
    s[0] = 'a'
    ss[0] = 'i' #menghasilkan error krn string immutable
    print(s)
    print(ss)
except:
    print("error")

#logic    
keyboard = 'qwertyuiop'

print('q' in keyboard)
print('Q' in keyboard)
print('qwe' in keyboard)
print('poi' in keyboard)

if 'Q' in keyboard:
    print('merupakan substring')
else:
    print('bukan merupakan substring')

print('q' not in keyboard)
print('Q' not in keyboard)

#demonstratng min()
print(min('aAbduSDFpoi'))
#bakal dibalikin dlu ke unique/ordinal numbernya
#bukti
print(ord('A'), ord('a'))
#so it is for max()
print(max('aAbduSDFpoi'))

#list() dan tuple()
print(list('absdefg'))
print(tuple('abcdefg'))

#count()
print('abcabc'.count('b'))
print('abcdabcdabge'.count('a'))

#capitalize() cuma membuat awal string kapital
print('terima kasih, cekgu. kamu itu keren'.capitalize())

#center()
ap = 'lucky'
print('['+ap.center(8)+']')
print('['+ap.center(8, '-')+']')

#endswith()
print(ap.endswith('y'))
print(ap.endswith('ck'))

xxx = 'lucky.py'
print(xxx.endswith('.py'))
print(xxx.endswith('.txt'))

#find()
t = 'thetaka'
idx = t.find('aka')
print(idx)
print(t[idx:idx+len('aka')])

#isalnum() to check if the strings contains only alphanumerical char
print('lambda'.isalnum())
print('lambda30'.isalnum())
print('lambda_30'.isalnum())

#lstrip() to omit certain char. by default is space
print('yeyey   ey    '.lstrip())
print('yeyeyeye'.lstrip('y'))
print('www.itb.ac.id'.lstrip('w'))
print('pythoninstitute'.lstrip('python'))