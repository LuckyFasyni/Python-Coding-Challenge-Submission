#removes all the number repetitions from the list. 
#The goal is to have a list in which all the numbers appear not more than once.
myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newList = []

for i in myList:
    if i not in newList:
        newList.append(i)

print("The list with unique elements only:")
print(newList)