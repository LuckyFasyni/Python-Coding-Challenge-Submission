#Factorial
def Factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    if n >= 2:
        product = 1
        for i in range(2, n + 1):
            product *= i
        return product
        
#print(Factorial(3))

#to check
for i in range(10):
    print(i, Factorial(i))