# -*- coding: utf-8 -*-
"""
Created on Tue May 26 20:25:57 2020

@author: user
"""

def myFunction0():
    global var #supaya variabel setelahnya berlaku global(di dalam maupun di luar fungsi), menghapus nilai dengan nama variabel yg smaa yg dipanggil sebelum fungsi
    var = 2
    print("Do I know that variable?", var)

var = 1
myFunction0()
print(var)

def myFunction(n):
    print("I got", n)
    n += 1
    print("I have", n)

var = 1
myFunction(var)
print(var)

def myFunction1(myList1):
    print(myList1)
    #myList1 = [0, 1] --> tdk mengubah list di luar fungsi
    del myList1[0] #memodif list di luar fungsi

myList2 = [2, 3]
myFunction1(myList2)
print(myList2)
#print(myFunction(myList2))

#EXERCISEEEEEEEE
def message():
    alt = 1
    print("Hello, World!")

print(alt)
#HASIL AKAN ERROR

a = 1

def fun():
    a = 2
    print(a)

fun() #a = 2
print(a) #a = 1

a = 1

def fun1():
    global a
    a = 2
    print(a)

#opsi 1
fun1()
a = 3
print(a) #hasilnya a = 3 karena ditaruh setelah fungsi (yg memiliki nilai global) dipanggil

#opsi 2
a = 3
fun1()
print(a)