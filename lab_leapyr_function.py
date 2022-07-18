#to write and test a function which takes one argument (a year)
#returns True if the year is a leap year, or False otherwise.
def isYearLeap(year):
    if year % 4 != 0:
        y = False
    elif year % 100 != 0:
        y = True
    elif year % 400 != 0:
        y = False
    else:
        y = True
    return y

#print(isYearLeap(1987))

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")