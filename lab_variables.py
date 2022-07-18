john = 3
mary = 5
adam = 6
print(john, mary, adam)

totalApples = john+mary+adam
print(totalApples)

print("Total number of apples", totalApples)

#Adam shares his apples to john and mary, in the same amount
list = (john, mary, adam)
john += adam/(len(list)-1)
mary += adam/(len(list)-1)
print("Total John's apples", int(john), "while Mary's", int(mary))