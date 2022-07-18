#bubble sort algorithm
#sorting simple list

myList = [8, 10, 6, 2, 4]

for i in range(len(myList)-1):
    if myList[i] > myList[i+1]:
        myList[i], myList[i+1] = myList[i+1], myList[i]
        
print(myList)

swapped = True

while swapped:
    swapped = False
    for i in range(len(myList)-1):
        if myList[i] > myList[i+1]:
            swapped = True
            myList[i], myList[i+1] = myList[i+1], myList[i]
            
print(myList)

#interactive version

myList = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    myList.append(val)

while swapped:
    swapped = False
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print("\nSorted:")
print(myList)