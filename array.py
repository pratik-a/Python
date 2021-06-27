from array import *

# import array as arr

values = array('i', [2, 3, 4, 5])

print(values.buffer_info())
print(values.typecode)

for x in values:
    print(x)

values.reverse()
print(values)

vowels = array('u', ['a', 'e', 'i', 'o', 'u'])
print(vowels)

newArr = array(values.typecode,( a * a for a in values))

for i in newArr:
    print(i)