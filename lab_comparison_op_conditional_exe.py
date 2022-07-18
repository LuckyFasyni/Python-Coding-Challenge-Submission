#Scenario
#Spathiphyllum, more commonly known as a peace lily or white sail plant
#Imagine that your computer program loves these plants. 
#Whenever it receives an input in the form of the word Spathiphyllum, 
#it involuntarily shouts to the console the following string: "Spathiphyllum is the best plant ever!"

plant = input("What is my favorite plant? ")

if plant == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not " + plant)