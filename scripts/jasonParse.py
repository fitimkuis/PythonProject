import requests
from addict import Dict
import json
import csv
import re
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



with open('constants_file.csv', mode='w', newline='', encoding='utf-8') as constants_file:
    writer = csv.writer(constants_file)
    for keys, item in recursive_iteration(data):
        if item == "string" and len(keys) == 1:
            l = []
            res1 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[0])))))
            l.append(res1)
            res2 = "".join(re.split("[^a-zA-Z]*", str([item])))
            l.append(res2)
            writer.writerow(l)

        if item == "string" and len(keys) == 2:
            l2 = []
            res1 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[0])))))
            l2.append(res1)
            res2 = "".join(re.split("[^a-zA-Z]*", str(set(list(list(zip(keys))[1])))))
            l2.append(res2)
            res3 = "".join(re.split("[^a-zA-Z]*", str([item])))
            l2.append(res3)
            writer.writerow(l2)


print(keys, item)


'''
with open('constants_file.csv') as csv_file:
    reader = csv.reader(csv_file)
    mydict = dict(reader)

print(mydict)
'''