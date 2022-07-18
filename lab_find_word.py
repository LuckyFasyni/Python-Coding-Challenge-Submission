# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 21:47:37 2020

@author: user
"""

#find a word
fstrng = input('Enter the first string: ').lower()
secstrng = input('Enter the second string: ').lower()
    
def pos(fstrng, secstrng):
    answer = ''
    for letter in fstrng:
        if secstrng.find(letter) != -1:
            answer = 'Yes'
        else:
            answer = 'No'
            break
    print(answer)
    return answer

pos(fstrng, secstrng)    