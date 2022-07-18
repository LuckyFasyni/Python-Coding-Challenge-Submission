#write and test a function which takes three arguments (a year, a month, and a day of the month)
#returns the corresponding day of the year
#returns None if any of the arguments is invalid.

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
    if month <= 12:
        odd = [1, 3, 5, 7, 8, 10, 12]
        even = [4, 6, 9, 11]
        if month in odd:
            m = 31
        elif month in even:
            m = 30
        elif month == 2:
            if isYearLeap(year) == True:
                m = 29
            else:
                m = 28
        return m

#print(daysInMonth(2020, 13))
def dayOfYear(year, month, day):
    if daysInMonth(year, month) != None:
        d = 0
        for i in range(1, month):
            d += daysInMonth(year, i)
        if day <= daysInMonth(year, month):
            d += day
            return d
    
print(dayOfYear(2000, 12, 31))