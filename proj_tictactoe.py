# -*- coding: utf-8 -*-
"""
Created on Wed May 27 21:37:04 2020

@author: user
"""

import random as rd

tictactoe = [["1", "2", "3"], ["4", "X", "6"], ["7", "8", "9"]]
        
def DisplayBoard(board):
    for i in range(len(board)):
        print(("+" + "-"*7)*3 + "+")
        print(("|" + " "*7)*3 + "|")
        print("|" + " "*2, board[i][0], " "*2 + "|" + " "*2, board[i][1], " "*2 + "|" + " "*2, board[i][2], " "*2 + "|")
        print(("|" + " "*7)*3 + "|")
    print(("+" + "-"*7)*3 + "+")

#DisplayBoard(tictactoe)
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#

def EnterMove():
    a = True
    while a:
        user = input("Your move, hooman: ")
        for i in range(3):
            for j in range(3):
                if user in tictactoe[i][j] and user != "" and user != "X" and user != "O":
                    a = False
                    break
            if a == False:
                break
        if a:
            print("Try again")
    tictactoe[i][j] = "O"
    DisplayBoard(tictactoe)
    
#def EnterMove():
#    while True:
#        x = int(input("Your move! Which row: "))
#        y = int(input("Your move! Which column: "))
#        if x > 2 or y > 2:
#            print("Choose another move!")
#            continue
#        elif tictactoe[x][y] == "X" or tictactoe[x][y] == 0:
#            print("Choose another move!")
#            continue
#        else:
#            tictactoe[x][y] = 0
#            break
#    DisplayBoard(tictactoe)
    
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#

def MakeListOfFreeFields():
    free = []
    for i in range(3):
        for j in range(3):
            if tictactoe[i][j] != "X" and tictactoe[i][j] != "O":
                tupel = (i, j)
                free.append(tupel)
#    print(free)
    return len(free)
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#

def VictoryFor():
    a = 0
    if tictactoe[0][0] == "O" and tictactoe[0][1] == "O" and tictactoe[0][2] == "O":
        a = 1
    if tictactoe[2][0] == "O" and tictactoe[2][1] == "O" and tictactoe[2][2] == "O":
        a = 1
    if tictactoe[0][0] == "O" and tictactoe[1][0] == "O" and tictactoe[2][0] == "O":
        a = 1
    if tictactoe[0][2] == "O" and tictactoe[1][2] == "O" and tictactoe[2][2] == "O":
        a = 1
    if tictactoe[0][0] == "X" and tictactoe[0][1] == "X" and tictactoe[0][2] == "X":
        a = 2
    if tictactoe[1][0] == "X" and tictactoe[1][1] == "X" and tictactoe[1][2] == "X":
        a = 2
    if tictactoe[2][0] == "X" and tictactoe[2][1] == "X" and tictactoe[2][2] == "X":
        a = 2
    if tictactoe[0][0] == "X" and tictactoe[1][0] == "X" and tictactoe[2][0] == "X":
        a = 2
    if tictactoe[0][1] == "X" and tictactoe[1][1] == "X" and tictactoe[2][1] == "X":
        a = 2
    if tictactoe[0][2] == "X" and tictactoe[1][2] == "X" and tictactoe[2][2] == "X":
        a = 2
    if tictactoe[0][0] == "X" and tictactoe[1][1] == "X" and tictactoe[2][2] == "X":
        a = 2
    if tictactoe[0][2] == "X" and tictactoe[1][1] == "X" and tictactoe[2][0] == "X":
        a = 2
    return a
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
   
# the function draws the computer's move and updates the board
def DrawMove():
    while True:
        xcomp = rd.randrange(0, 3)
        ycomp = rd.randrange(0, 3)
        if tictactoe[xcomp][ycomp] == "X" or tictactoe[xcomp][ycomp] == "O":
            continue
        else:
            tictactoe[xcomp][ycomp] = "X"
            break
    print("\nThis is my move, huh!")
    DisplayBoard(tictactoe)

DisplayBoard(tictactoe)
while True:
    EnterMove()
    if MakeListOfFreeFields() == 0:
        print("Tictactoe is Draw!")
        break
    VictoryFor()
    if VictoryFor() == 1:
        print("Hooman is the real winner!")
        break
    DrawMove()
    if MakeListOfFreeFields() == 0:
        print("Tictactoe is Draw!")
        break
    VictoryFor()
    if VictoryFor() == 2:
        print("This is unreal! Computer won!")
        break
