def foo():
    """this is a practice code"""
    return True


heStr = "hello123"
print(heStr[2: 5])

heheStr = 'hello123'
print(heheStr * 4)

# a = input("please input a string")
# help(input)

a = 5 / 3  # 1.66666667
print(a)
b = 5 // 3  # 1

print("%f is 5 /3  and 5 // 3 is %f " % (a, b))

print(- 4 * 2 + 3 ** 2 + 1)  # **

print(2 < 4 and 2 == 4)

print(3 < 4 < 5)

aList = [1, 2, 3, 4]
print(aList)

aTuple = ('1', '2', '3')
print(aTuple)

aDict = {'host': 'earth'}
aDict['path'] = '80'
print(aDict)
for key in aDict:
    print(key, aDict[key])

if 3 < 4:
    print("3 < 4 is True")

counter = 0
while counter < 5:
    print('loop of counter %d' % (counter))
    counter += 1

counter = 0
for item in aDict:
    print(item, aDict[item])

print('range()')
for item in range(4):
    print(item)

heStr = 'hello123'
for i in range(len(heStr)):
    print(heStr[i], i)

squared = [x ** 2 for x in range(4)]
for i in squared:
    print(i)


try:
    handle = open('123.txt', 'r')
    for eachLine in handle:
        print(eachLine)
    handle.close()
except IOError as e:
    print('file open error', e)

print("class")