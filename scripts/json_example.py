import json
import re
import requests
from addict import Dict
import pprint
from collections import defaultdict
from pprint import pprint

def get_json_dict():
    r = requests.get('http://api.zippopotam.us/us/ma/belmont')
    ad = Dict(r.json())
    print(ad)
    print (ad.state)
    print (ad.places[1]['post code'])
    return ad

def recursive_iter(obj):
    if isinstance(obj, dict):
        for item in obj.values():
            yield from recursive_iter(item)
    elif any(isinstance(obj, t) for t in (list, tuple)):
        for item in obj:
            yield from recursive_iter(item)
    else:
        yield obj

def recursive_iteration(obj, keys=()):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from recursive_iteration(v, keys + (k,))
    elif any(isinstance(obj, t) for t in (list, tuple)):
        for idx, item in enumerate(obj):
            yield from recursive_iteration(item, keys + (idx,))
    else:
        yield keys, obj

def custom_hook(obj):
    # Identify dictionary with duplicate keys
    # If found create a separate dict with single key and val and as list.
    if len(obj) > 1 and len(set(i for i, j in obj)) == 1:
        data_dict = defaultdict(list)
        for i, j in obj:
            data_dict[i].append(j)
        return dict(data_dict)
    return dict(obj)


result = """{
    "firstName": "Jane",
    "lastName": "Doe",
    "firstName": "John",
    "lastName": "Parson"
}"""
data = json.loads(result)

dat = json.loads(result, object_pairs_hook=custom_hook)
pprint(dat)


#for keys, item in recursive_iteration(data):
#    print(keys, item)

data = json.loads(result)
for x in data:
    print("%s: %s" % (x, data[x]))

res = '{"firstname": "alex", "lastname": "leda", "firstname":"john", "lastname":"parsons",  "firstname":"pat", "lastname":"mat"}'
obj = json.loads(res)

data = json.loads(res)
#print(data)

d = json.dumps(res) #d is string now
print(type(d))
d = d.split(',')
#print(d)




for keys, item in recursive_iteration(res):
    #print(keys, item)
    r = "".join(re.split("[^a-zA-Z , :]*", str(set(list(list(zip([item]))[0]))))) #remove all unwanted chars
    print(r)

r = r.split(',')

for x in r:
    x = x.split(':')
    print(x[0]+ " "+ x[1])
    if x[1] == 'john':
        print(x[0]+ " "+ x[1])


'''
p = item.replace('{',"").replace('}',"").replace('[',"").replace(']',"")
#print(item.replace('{',"").replace('}',"").replace('[',"").replace(']',""))
j = p.split(',')
#print(j[0])
#print(j[2])
t = j[2].split(':')
print(t[1].replace('"',""))
'''



