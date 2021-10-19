class Person:
    # initializing the variables
    name = ""
    age = 0

    # defining constructor
    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

        # defining class methods

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)

# definition of subclass starts here
class Student(Person):
    studentId = ""

    def __init__(self, student_name, student_age, student_id):
        #Person.__init__(self, student_name, student_age)
        super().__init__(student_name, student_age)
        self.studentId = student_id

    def get_id(self):
        return self.studentId  # returns the value of student id


# end of subclass definition

class MyParentClass():

    x = 0
    y = 0

    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def result(self):
        print(self.x + self.y)

    def are_res(self):
        return self.x * self.y

class SubClass(MyParentClass):

    c = 0
    def __init__(self, _x, _y, _c):
        super().__init__(_x, _y)
        self.c = _c

    def area(self):
        print("area "+str(self.are_res())+" number " + str(self.c))
        #print(self.c)

class OneMore(SubClass):

    def __init__(self, _x, _y, _c):
        super().__init__(_x, _y, _c)

    def second_print(self):
        print("in third class area "+str(self.are_res())+" number " + str(self.c))

C = MyParentClass(3,3)
C.result()
B = SubClass(2,8,1234)
B.result()
B.area()
D = OneMore(4,5,4321)
D.second_print()

# Create an object of the superclass
person1 = Person("Richard", 23)
# call member methods of the objects
person1.show_age()
# Create an object of the subclass
student1 = Student("Max", 22, "102")
print(student1.get_id())
student1.show_name()