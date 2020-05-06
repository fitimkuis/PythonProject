import os, sys
from natsort import natsorted


def myFunction(arg1,names):
    print ("calling python function with parameters:")
    print (arg1)
    print (names)
    res = names.strip('][').split(', ')
    print (res)
    print(natsorted(names, key=lambda y: y.lower()))
myFunction(sys.argv[0], sys.argv[1])

def test_division_float(a, b):
    return a/b

def test_division_int(a, b):
    return a//b

print(test_division_float(10, 5))

print(test_division_int(10, 5))

print('47')

c = '/'
print("The ASCII value of '" + c + "' is", ord(c))

a = chr(47)


