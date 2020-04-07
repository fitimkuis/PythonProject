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

with open("C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\scripts\\toMultipleCsv.json", "r") as read_file:
    data = json.load(read_file)

print("######################################################################################")
for key,value in data.items(): #this gives you both
    print(key,value)
print("######################################################################################")

for item in recursive_iter(data):
    print(item)

def recursive_iteration(obj, keys=()):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from recursive_iteration(v, keys + (k,))
    elif any(isinstance(obj, t) for t in (list, tuple)):
        for idx, item in enumerate(obj):
            yield from recursive_iteration(item, keys + (idx,))
    else:
        yield keys, obj

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
        #print(keys, item)

        s = None
        reg = None
        #reg = re.compile('\d\d\d\d-\d\d-\d\d\(T\)\d\d:\d\d:\d\d')
        s = re.sub(r'(.*\d\d\d\d-\d\d-\d\d)T(\d\d:\d\d:\d\d.*)',r'\1 \2',str(item))

        if len(keys) == 1 and (is_date(s) != True and item != True and item != "string"):
            l0 = []
            r0 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[0])))))
            l0.append(r0)
            r2 = "".join(re.split("[^a-zA-Z]*", str(item)))
            l0.append(item)
            writer.writerow(l0)

        if len(keys) == 1 and is_date(s):
            l1 = []
            r3 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[0])))))
            l1.append(r3)
            l1.append(s)
            writer.writerow(l1)

        if len(keys) == 2 and is_date(s):
            l2 = []
            r4 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[0])))))
            l2.append(r4)
            r5 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[1])))))
            l2.append(r5)
            l2.append(s)
            writer.writerow(l2)

        if len(keys) == 1 and (item == "string" or item == True):
            l3 = []
            r6 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[0])))))
            l3.append(r6)
            r7 = "".join(re.split("[^a-zA-Z]*", str([item])))
            l3.append(r7)
            writer.writerow(l3)

        if item == "string" and len(keys) == 2:
            l4 = []
            r8= "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[0])))))
            l4.append(r8)
            r9 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[1])))))
            l4.append(r9)
            res10 = "".join(re.split("[^a-zA-Z]*", str([item])))
            l4.append(res10)
            writer.writerow(l4)

        if item == "string" and len(keys) == 3:
            l5 = []
            r11 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[0])))))
            l5.append(r11)
            #res01 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[1])))))
            #ll.append(res01)
            r12 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[2])))))
            l5.append(r12)
            r13 = "".join(re.split("[^a-zA-Z]*", str([item])))
            l5.append(r13)
            writer.writerow(l5)

        if item == "string" and len(keys) == 4:
            l6 = []
            r14 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[0])))))
            l6.append(r14)
            #res010 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[1])))))
            #lis.append(res010)
            r15 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[2])))))
            l6.append(r15)
            r16 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[3])))))
            l6.append(r16)
            r17 = "".join(re.split("[^a-zA-Z]*", str([item])))
            l6.append(r17)
            writer.writerow(l6)


'''
with open('constants_file.csv') as csv_file:
    reader = csv.reader(csv_file)
    mydict = dict(reader)

print(mydict)
'''