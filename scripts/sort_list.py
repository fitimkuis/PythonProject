#names = ['AA-1', 'AA-2', 'AA-2 (1)', 'AA-10']
import re
from natsort import natsorted, ns
names = ['AA-1', 'AA-10', 'AA-2', 'AA-2 (1)']
'''
should be sorted as this way
AA-1
AA-2
AA-2 (1)
AA-10
'''

#sort names
#print("used sorted")
#print(sorted(names))

print("used natsort")
print(natsorted(names, key=lambda y: y.lower()))

def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

#print(natural_sort(names))



