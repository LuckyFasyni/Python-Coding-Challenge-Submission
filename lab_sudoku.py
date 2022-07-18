# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 22:03:29 2020

@author: user
"""

#sudoku

player = input('enter numbers: ').split()
answer = 'Yes'

#ngecek keunikan nomor per baris
if answer:
    for digits in player:
        for digit in digits:
            counter = digits.count(digit)
            if counter > 1:
                answer = 'No'
                break
        if not answer:
            break

#ngecek keunikan nomor per kolom
column = []
if answer:
    for i in range(9):
        strng = ''
        for digit in player:
            strng += digit[i]
        column.append(strng)
    for digits in column:
        for digit in digits:
            counter = digits.count(digit)
            if counter > 1:
                answer = 'No'
                break
        if not answer:
            break

#ngecek keunikan nomor per subsquare
subsq = []
subsq1 = player[0][0:3] + player[1][0:3] + player[2][0:3]
subsq2 = player[0][3:6] + player[1][3:6] + player[2][3:6]
subsq3 = player[0][6:9] + player[1][6:9] + player[2][6:9]    

subsq4 = player[3][0:3] + player[4][0:3] + player[5][0:3]
subsq5 = player[3][3:6] + player[4][3:6] + player[5][3:6]
subsq6 = player[3][6:9] + player[4][6:9] + player[5][6:9]

subsq7 = player[6][0:3] + player[7][0:3] + player[8][0:3]
subsq8 = player[6][3:6] + player[7][3:6] + player[8][3:6]
subsq9 = player[6][6:9] + player[7][6:9] + player[8][6:9]

subsq.append(subsq1)
subsq.append(subsq2)
subsq.append(subsq3)
subsq.append(subsq4)
subsq.append(subsq5)
subsq.append(subsq6)
subsq.append(subsq7)
subsq.append(subsq8)
subsq.append(subsq9)

if answer:
    for digits in subsq:
        for digit in digits:
            counter = digits.count(digit)
            if counter > 1:
                answer = 'No'
                break
        if not answer:
            break
        
print(answer)