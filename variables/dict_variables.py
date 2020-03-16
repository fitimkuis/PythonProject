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
    print(name[0])
    y = random.randint(40,55)
    my_dict[name[0]] = y

print("Dictionary is : ",my_dict)

