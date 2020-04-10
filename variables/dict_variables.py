from collections import OrderedDict
from faker import Faker
import random


LIST__ANIMALS = ["cat", "dog"]
DICT__FINNISH = OrderedDict([("cat", "kissa"), ("dog", "koira")])
DICT__SALARIES = OrderedDict([("Pat", 10000), ("Mat", 100000), ("Kat", 19999), ("Sat", 188888)])

fake = Faker('fi_FI')
my_dict = {}
for i in range (10):
    x = fake.name()
    name = x.split(' ')
    #print(name[0])
    y = random.randint(40,55)
    my_dict[name[0]] = y

#print("Dictionary is {}: ".format(my_dict))

#DICT__MYORDRDICT= OrderedDict([("Timo", 54)])

DICT__MYORDRDICT= OrderedDict([])
d = {}
for x in range (5):
    x = fake.name()
    name = x.split(' ')
    #print(name[0])
    y = random.randint(40,55)
    d[name[0]] = y
    DICT__MYORDRDICT.update(d)

#print(DICT__MYORDRDICT)


def dynamic_list_variables(count=5):
    JOB= []
    for x in range (count):
        job = fake.job()
        JOB.append(job)
    return JOB

dict = {('Meraki_Organization_Scenarios', 'failed'),
        ('Meraki_HttpServer_Scenarios', 'failed'),
        ('Meraki_HttpServer_Scenarios', 'passed'),
        ('Meraki_Organization_Scenarios', 'passed'),
        ('Meraki_Networks_Scenarios', 'failed'),
        ('Meraki_Networks_Scenarios', 'passed')}

LIST__JOBS = dynamic_list_variables(5)
#print(LIST__JOBS)
def ret_failed_as_list():
    final_results = {}
    for name, status in dict:
        current_status = final_results.get(name, 'notset')
        if current_status != 'failed':
            final_results[name] = status
    return list(final_results.items())

print(ret_failed_as_list())