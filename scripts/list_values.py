from faker import Faker


LIST__WORKS = []
fake = Faker('fi_FI')
def __list_variables(count):
    JOB= []
    for x in range (count):
        job = fake.job()
        JOB.append(job)
    return JOB

def generate_works(cnt):
    LIST__WORKS = __list_variables(int(cnt))
    #print(LIST__WORKS)
    return LIST__WORKS
    #print(LIST__WORKS)
#LIST__WORKS = LIST__JO