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