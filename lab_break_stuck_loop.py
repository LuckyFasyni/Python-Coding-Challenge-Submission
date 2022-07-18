# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:10:07 2020

@author: user
"""
#Scenario
#Design a program that uses a while loop and continuously asks the user to enter a word 
#unless the user enters "chupacabra" as the secret exit word, 
#in which case the message "You've successfully left the loop." should be printed to the screen, 
#and the loop should terminate.

word = input("guess a word: ")

while True:
    if word == "chupacabra":
        break
    word = input("guess a word: ")
    
print("\nYou've succesfully left the loop.")