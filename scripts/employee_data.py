from random import *
alphabets="abcdefghijklmnopqrstuvwxyz"
digits="0123456789"
cities=["Bangalore", "Chennai", "Hyderabad", "Delhi", "Mumbai", "Pune"]
designations=["software Engineer", "Senior Software Engineer", "Project Lead",
              "Team Lead", "Project Manager"]
def get_fake_name():
    name=choice(alphabets).upper()
    n=randint(2,9)
    for i in range(n):
        name=name+choice(alphabets)
    return name

def get_fake_eno():
    eno="e-"
    for i in range(4):
        eno=eno+choice(digits)
    return eno

def get_fake_salary():
    esal=uniform(10000,50000)
    return esal

def get_fake_city():
    city=choice(cities)
    return city

def get_fake_mno():
    mno=choice("6789")
    for i in range(9):
        mno=mno+choice(digits)
    return mno

def get_fake_designation():
    designation=choice(designations)
    return designation

def get_fake_emp_data():
    print("Employee name:", get_fake_name())
    print("Employee eno:", get_fake_eno())
    print("Employee salary:", get_fake_salary())
    print("Employee city:", get_fake_city())
    print("Employee mno:", get_fake_mno())
    print("Employee designation:",get_fake_designation())

for i in range(10):
    get_fake_emp_data()
    print()