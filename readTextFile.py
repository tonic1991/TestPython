#! /usr/bin/env python

'readTextFile.py -- read and display text file'

# get file name
fName = input('please input the file name you want to read:')

# open file
try:
    fObj = open(fName, 'r')
except IOError as e:
    print('this file %s doesn\'t exit' % fName)
else:
    # display this file
    for eachLine in fObj:
        print(eachLine)
    fObj.close()