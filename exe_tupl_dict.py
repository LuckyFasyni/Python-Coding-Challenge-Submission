# -*- coding: utf-8 -*-
"""
Created on Wed May 27 14:47:52 2020

@author: user
"""

#TUPLE
myTuple = (1, 10, 100)

t1 = myTuple + (1000, 10000)
t2 = myTuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in myTuple)
print(-10 not in myTuple)

var = 123
t1 = 1, 
t2 = 2, 
t3 = 3, var

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

#DICTIONARY
dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
phoneNumbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
emptyDictionary = {}

print(dict['dog'])
print(phoneNumbers['Suzy'])
#print(emptyDictionary('dog'))

words = ['cat', 'dog', 'horse']

for word in words:
    if word in dict:
        print(word, "->", dict[word])
    else:
        print(word, "is not in dictionary")
  
#to browse it within for loop      
for english in dict.keys():
    print(english, "->", dict[english])
    print(english)
    
#to browse with sorted version    
for key in sorted(dict.keys()):
    print(key, "->", dict[key])
    
for english, french in dict.items():
    print(english, "->", french)
    
for french in dict.values():
    print(french)
    
dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

#replace a value
dict['cat'] = 'minou'
print(dict)

#adding a new key
dict['swan'] = 'cygne'
print(dict)

#insert an item using update
dict.update({'duck' : 'canard'})
print(dict)

#remove a key
del dict['cat']
print(dict)

#remove the last item 
dict.popitem()
print(dict)




# evaluate the students' average scores

schoolClass = {}

while True:
    name = input("Enter the student's name (or type exit to stop): ")
    if name == 'exit':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    
    if name in schoolClass:
        schoolClass[name] += (score,)
    else:
        schoolClass[name] = (score,)
        
for name in sorted(schoolClass.keys()):
    sum = 0
    counter = 0
    for score in schoolClass[name]:
        sum += score
        counter += 1
    print(name, ":", sum / counter)



#unpacked
tup = 1, 2, 3
a, b, c = tup

print(a * b * c)

#count
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2) # your code

print(duplicates)    # outputs: 4

#glue d1 and d2 to new d3
d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

#convert to tuple
l = ["car", "Ford", "flower", "Tulip"]

t = tuple(1)# your code
print(t)

#convert to dict
colors = (("green", "#008000"), ("blue", "#0000FF"))

colDict = dict(colors)# your code

print(colDict)

#copy the dictionary
myDict = {"A":1, "B":2}
copyMyDict = myDict.copy()
myDict.clear()

print(copyMyDict)

colors = {
    "white" : (255, 255, 255),
    "grey"  : (128, 128, 128),
    "red"   : (255, 0, 0),
    "green" : (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb)

tup1 = 1, 2, 3, 
tup1 = 4, 5, 6, 
print(tup1)

