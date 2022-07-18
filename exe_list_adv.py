# -*- coding: utf-8 -*-
"""
Created on Sun May 24 23:36:16 2020

@author: user
"""

#Temperature

#temps = [[0.0 for h in range(24)] for d in range(31)]
#
##monthly average noon temperature
#total = 0.0
#for day in temps:
#    total += day[11]
#avg = total/31
#print("Average temperature at noon: ", avg)
#
##highest temperature during the whole month
#highest = -100.0
#for day in temps:
#    for hour in day:
#        if hour > highest:
#            highest = hour
#print("Highest temperature during the whole month: ", highest)
#
##count the days when the temperature at noon was at least 20 ℃
#hotdays = 0.0
#for day in temps:
#    if day[11] > 20.0:
#        hotdays += 1
#print(hotdays, "hot days")

#Hotel
rooms = [[[False for r in range(20)] for f in range(15)] for b in range(3)]

rooms[2][14][1] = True
     
#room vacancy
vacancy = 0
for i in range(20):
    if rooms[2][14][i] == False:
#   if not rooms[2][14][i]:
        vacancy += 1
        
print(vacancy)