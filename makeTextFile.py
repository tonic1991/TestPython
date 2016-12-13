#! /usr/bin/env python

'makeTextFile.py -- create text file'

import os
ls = os.linesep

# get file
while True:
    fName = input('please input file name:')
    if os.path.exists(fName):
        print("error %s is already exits hello!" % fName)
    else:
        break

# get file context lines
all = []
print("\n Enter lines ('.' by itself to quit).\n")

# loop until user terminate input
while True:
    entry = input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)

# write lines to file with proper line-ending
fobj = open(fName , 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all ])
fobj.close()
print('done!')




