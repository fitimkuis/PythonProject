from faker import Faker
from faker.providers import internet
from faker.providers import ssn
import re

fake = Faker('fi_FI')
#fake.add_provider(internet)

#print(fake.ipv4_private())


def validate_ssn(ssn):
    individual_number = int(ssn[7:10])
    assert individual_number <= 899

def test_ssn_sanity(fake):
    for age in range(100):
        ssn = fake.ssn(min_age=age, max_age=age + 1)
        if '-' in ssn:
            print(ssn)

def write_ssn(ssn):
    file = open('C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\scripts\\ssn.txt','w')
    file.write(ssn)
    file.write("\n")
    file.close()

def create_ssn():
    ssn = fake.ssn(artificial=False)
    if '-' in ssn:
        validate_ssn(ssn)
        #test_ssn_sanity(fake)
        write_ssn(ssn)
        print(ssn)
        return ssn
    else:
        print("ssn not contain '-' char")
        return 'ssn not valid'

from functools import reduce
from operator import or_

def merge(*dicts):
    return { k: reduce(lambda d, x: x.get(k, d), dicts, None) for k in reduce(or_, map(lambda x: x.keys(), dicts), set()) }

def combine_dictionaries(d1, d2):
    updated = d1.copy()
    updated.update(d2)
    #print(updated)
    return updated

d1 = { 'fname':'DIALPAD' , 'account_type': 'o365', 'dept': 'ROBOT' }
d2 = { 'name':'SMSNG', 'version':'11', 'port':4724, 'platformName':'android', 'type':'tab'}

d3 = d2 | d1
#print(d3)

a = merge(d1, d2)
#print(a)

updated = d1.copy()
updated.update(d2)
print(updated)

#for age in range(100):
#    print(fake.ssn(min_age=age, max_age=age + 1))