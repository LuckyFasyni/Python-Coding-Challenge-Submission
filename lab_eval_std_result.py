# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:13:54 2020

@author: user
"""

from os import strerror

class StudentDataException(Exception):
    def __init__(self, file):
        self.file = file

class BadLine(StudentDataException):
    def __init__(self, file, message):
        super().__init__(file)
        self.message = message
        
class DataEmpty(StudentDataException):
    def __init__(self, file, message):
        super().__init__(file)
        self.message = message

srcfl = input('Input your student data file: ')        
try:
    stream = open(srcfl, 'rt')
    content = sorted(stream.readlines())
except IOError as exc:
    print(strerror(exc.errno))
    
def readfile(file, content):
    if len(content) == 0:
        raise DataEmpty(file, 'there is no data here!')
    lst = []
    studentdatadict = {}
    for line in content:
        x = line.split(' ')
#        print(x)
        if len(x) != 3:
            raise BadLine(file, 'bad line!')
        lst.append(x[0])
        lst.append(x[1])
        name = ' '.join(lst)
#        print(name)
        lst = []
        score = x[2].rstrip()
        score = float(score)
        if name in studentdatadict.keys():
            studentdatadict[name] += score
        else:
            studentdatadict[name] = score
    return studentdatadict

try:
    studentdatadict = readfile(srcfl, content)
    for name, score in studentdatadict.items():
        print(name, score)
except BadLine as bl:
    print(bl.message, ':', bl.file)
except DataEmpty as de:
    print(de.message, ':', de.file)
except:
    print('There is something wrong!!!')
    
stream.close()

#lst = ['Lucky 37', 'Fasyni 38', 'Achmad 39']
#for i in lst:
#    x = i.split(' ')
#    print(x)