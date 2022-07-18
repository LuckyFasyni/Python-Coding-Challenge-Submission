for s in open('newtext.txt', 'rt'):
    print(s, end='')


#from os import strerror
#
##count characters in real file
#try:
#    cnt = 0
#    s = open('text.txt', "rt")
#    ch = s.read(1)
#    while ch != '':
#        print(ch, end='')
#        cnt += 1
#        ch = s.read(1)
#    s.close()
#    print("\n\nCharacters in file:", cnt)
#except IOError as e:
#    print("I/O error occurred: ", strerror(e.errno))
#    
##other version
#try:
#    cnt = 0
#    s = open('text.txt', "rt")
#    content = s.read()
#    for ch in content:
#        print(ch, end='')
#        cnt += 1
#        ch = s.read(1)
#    s.close()
#    print("\n\nCharacters in file:", cnt)
#except IOError as e:
#    print("I/O error occurred: ", strerror(e.errno))
#    
##count lines in real file
#try:
#    stream = open('text.txt', 'rt')
#    line = stream.readline()
#    lcounter = ccounter = 0
#    while line != '':
#        lcounter += 1
#        for ch in line:
#            print(ch, end='')
#            ccounter += 1
#        line = stream.readline()
#    stream.close()
#    print('\n\nThe characters :', ccounter)
#    print('The lines :', lcounter)
#except IOError as exc:
#    print('I/O error occurred: ', strerror(exc.errno))
#    
##readlines()
#from os import strerror
#
#try:
#    ccnt = lcnt = 0
#    s = open('text.txt', 'rt')
#    lines = s.readlines(20)
#    while len(lines) != 0:
#        for line in lines:
#            lcnt += 1
#            for ch in line:
#                print(ch, end='')
#                ccnt += 1
#        lines = s.readlines(10)
#    s.close()
#    print("\n\nCharacters in file:", ccnt)
#    print("Lines in file:     ", lcnt)
#except IOError as e:
#    print("I/O error occurred:", strerror(e.errno))
#    
##an object from class open    
#from os import strerror
#
#try:
#	ccnt = lcnt = 0
#	for line in open('text.txt', 'rt'):
#		lcnt += 1
#		for ch in line:
#			print(ch, end='')
#			ccnt += 1
#	print("\n\nCharacters in file:", ccnt)
#	print("Lines in file:     ", lcnt)
#except IOError as e:
#	print("I/O error occurred: ", strerror(e.errno))
#
#'''
#examples of write open mode
#'''
#
#from os import strerror
#
#try:
#	fo = open('newtext.txt', 'wt') # a new file (newtext.txt) is created
#	for i in range(10):
#		s = "line #" + str(i+1) + "\n"
#		for ch in s:
#			fo.write(ch)
#	fo.close()
#except IOError as e:
#	print("I/O error occurred: ", strerror(e.errno))
#    
##another way
#from os import strerror
#
#try:
#	fo = open('newtext2.txt', 'wt')
#	for i in range(10):
#		fo.write("line #" + str(i+1) + "\n")
#	fo.close()
#except IOError as e:
#	print("I/O error occurred: ", strerror(e.errno))
#    
#import sys
#sys.stderr.write('Error message') #tertulis implicitly
#
#'''
#Bytearray
#'''
#
#data = bytearray(10)
#
#for i in range(len(data)):
#    data[i] = 10 - i
#
#for b in data:
#    print(hex(b))
#    
#from os import strerror
#
#data = bytearray(10)
#
#for i in range(len(data)):
#    data[i] = 10 + i
#
##wirte a binary file
#try:
#    bf = open('file.bin', 'wb')
#    bf.write(data)
#    bf.close()
#except IOError as e:
#    print("I/O error occurred:", strerror(e.errno))
#
##read a binary file
#try:
#    bf = open('file.bin', 'rb')
#    bf.readinto(data)
#    bf.close()
#    
#    for b in data:
#        print(hex(b), end='')
#except IOError as exc:
#    print('I/O error occurred:', strerror(exc.errno))
#    
#try:
#    bf = open('file.bin', 'rb')
#    data = bytearray(bf.read()) #bf.read(max number of bytes to read)
#    bf.close()
#    
#    for b in data:
#        print(hex(b), end = '')
#except IOError as e:
#    print('I/O error occurred:', strerror(e.errno))

#copy paste a file

#from os import strerror
#
#sourc = input('Input a source file: ')
#try:
#    sourc = open(sourc, 'rb')
#except IOError as exc:
#    print(strerror(exc.errno))
#    exit(exc.errno)
#
#dest = input('Input a destinantion file: ')
#try:
#    dest = open(dest, 'wb')
#except IOError as exc:
#    print(strerror(exc.errno))
#    exit(exc.errno)
#    sourc.close()
#
#buffer = bytearray(65536)
#total = 0
#try:
#    readin = sourc.readinto(buffer)
#    while readin > 0:
#        written = dest.write(buffer[:readin])
#        total += written
#        readin = sourc.readinto(buffer)
#except IOError as exc:
#    print(strerror(exc.errno))
#    exit(exc.errno)
#    
#print(total, 'bytes written in the destination file')
#sourc.close()
#dest.close()