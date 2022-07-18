#write and test a function which takes two arguments (a year and a month)
#returns the number of days for the given month/year pair


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

def daysInMonth(year, month):
    odd = [1, 3, 5, 7, 8, 10, 12]
    even = [4, 6, 9, 11]
    if month in odd:
        m = 31
    elif month in even:
        m = 30
    else:
        if isYearLeap(year) == True:
            m = 29
        else:
            m = 28
    return m

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")