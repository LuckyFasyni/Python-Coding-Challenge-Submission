def readint(prompt, min, max):
    status = False
    while status == False:
        try:
            x = int(input(prompt))
            status = True
        except ValueError:
            print("Error: wrong input")
            continue
        if status == True:
            status = x >= min and x <= max
        if status == False:
            print("Error: the value is not within permitted range (" + str(min) + "..." + str(max) + ")")
    return x

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)