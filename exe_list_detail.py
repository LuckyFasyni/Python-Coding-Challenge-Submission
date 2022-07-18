# find the location of a given element inside a list
myList = [2, 4, 6, 8, 10, 12, 14, 16]
target = 16
found = False

for i in range(len(myList)):
    found = myList[i] == target
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("Absent")
    
#how many numbers have you hit?
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)