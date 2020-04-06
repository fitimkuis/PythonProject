import requests
from addict import Dict
import json
import csv
import re
from dateutil.parser import parse
from operator import itemgetter

def get_json_dict():
    r = requests.get('http://api.zippopotam.us/us/ma/belmont')
    ad = Dict(r.json())
    print(ad)
    print (ad.state)
    print (ad.places[1]['post code'])
    return ad

#print (data)
#print (data["contactDetail"]["email"])


with open('C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\scripts\\toMultipleCsv.json', 'r') as f:
    csv_dict = json.load(f)

print(csv_dict['messageType'])
print(csv_dict['messageID'])
print(csv_dict['messageCreatedTime'])
print(csv_dict['claimFromDate'])
print(csv_dict['confirmedAddress'])

print(csv_dict['contactDetail'])

print(csv_dict['dobVerification'])
print(csv_dict['inviteKey'])
print(csv_dict['livedAbroad'])

print(csv_dict['livedPeriodsAbroad'])

print(csv_dict['maritalStatus'])

print(csv_dict['overseasAccountDetail'])

print(csv_dict['partnerDetail'])

print(csv_dict['workedPeriodsAbroad'])

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

with open("C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\scripts\\toMultipleCsv.json", "r") as read_file:
    data = json.load(read_file)

for item in recursive_iter(data):
    print(item)

def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.
    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except:
        return False


with open('constants_file.csv', mode='w', newline='', encoding='utf-8') as constants_file:
    writer = csv.writer(constants_file)
    for keys, item in recursive_iteration(data):
        print(keys, item)

        s = None
        reg = None
        #reg = re.compile('\d\d\d\d-\d\d-\d\d\(T\)\d\d:\d\d:\d\d')
        s = re.sub(r'(.*\d\d\d\d-\d\d-\d\d)T(\d\d:\d\d:\d\d.*)',r'\1 \2',str(item))

        if len(keys) == 1 and (is_date(s) != True and item != True):
            lis0 = []
            r0 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[0])))))
            lis0.append(r0)
            r2 = "".join(re.split("[^a-zA-Z]*", str(item)))
            lis0.append(item)
            writer.writerow(lis0)

        if len(keys) == 1 and is_date(s):
            lil = []
            res100 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[0])))))
            lil.append(res100)
            lil.append(s)
            writer.writerow(lil)

        if len(keys) == 2 and is_date(s):
            list0 = []
            r10 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[0])))))
            list0.append(r10)
            r20 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[1])))))
            list0.append(r20)
            list0.append(s)
            writer.writerow(list0)

        if len(keys) == 1 and (item == "string" or item == True):
            li = []
            res1 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[0])))))
            li.append(res1)
            res2 = "".join(re.split("[^a-zA-Z]*", str([item])))
            li.append(res2)
            writer.writerow(li)

        if item == "string" and len(keys) == 2:
            l2 = []
            res12 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[0])))))
            l2.append(res12)
            res13 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[1])))))
            l2.append(res13)
            res14 = "".join(re.split("[^a-zA-Z]*", str([item])))
            l2.append(res14)
            writer.writerow(l2)

        if item == "string" and len(keys) == 3:
            ll = []
            res00 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[0])))))
            ll.append(res00)
            res01 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[1])))))
            #ll.append(res01)
            res02 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[2])))))
            ll.append(res02)
            res03 = "".join(re.split("[^a-zA-Z]*", str([item])))
            ll.append(res03)
            writer.writerow(ll)

        if item == "string" and len(keys) == 4:
            lis = []
            res000 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[0])))))
            lis.append(res000)
            res010 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[1])))))
            #lis.append(res010)
            res020 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[2])))))
            lis.append(res020)
            res030 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[3])))))
            lis.append(res030)
            res040 = "".join(re.split("[^a-zA-Z]*", str([item])))
            lis.append(res040)
            writer.writerow(lis)


print(keys, item)


'''
with open('constants_file.csv') as csv_file:
    reader = csv.reader(csv_file)
    mydict = dict(reader)

print(mydict)
'''