# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:40:28 2020

@author: user
"""

#counting mississippily
import time

for i in range(1, 6):# Write a for loop that counts to five.
    print(i, "Mississippi")# Body of the loop - print the loop iteration number and the word "Mississippi".
    time.sleep(1)# Body of the loop - use: time.sleep(1)

#For the time being, we'd just like you to know that 
#we've imported the time module and used the sleep() method 
#to suspend the execution of each subsequent print() function inside the for loop for one second

time.sleep(3) #3 seconds
print("")
print("I will find you!!!")# Write a print function with the final message.