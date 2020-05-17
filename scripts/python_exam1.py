import textwrap

from win32timezone import now

s='Python is easy'
s1=s[6:-4]
print(s1)
#Line-1
s2 = s1.strip()
print(len(s2))
print("************************'")
result=8//6%5+2**3-2
print(result)
print("************************'")
s='AB CD'
list=list(s)
list.append('EF')
print(list)
print("************************'")
x=3#input('Enter First Number:')
y=4#input('Enter Second Number:')
#Line-1
print("Result: "+str(int(x)+int(y)))
print("************************'")
a=2
a += 1
# Line-1
a**=2
print(a)
print("************************'")
a1='10'
b1=3
c1=a1*b1
print(type(c1))
print("************************'")
a2=10
b2=3
c2=a2/b2
print(type(c2))
print("************************'")
a3=2.6
b3=1
c3=a3/b3
print(type(c3))
print("************************'")
a=15
b=5
print(a/b)
print("************************'")
n1=[10,20,30,40,50]
n2=[10,20,30,40,50]
print(n1 is n2)
print(n1 == n2)
n1=n2
print(n1 is n2)
print(n1 == n2)
print("************************'")
x= 'Larry'
y= 'Larry'
result= x is y
print(result)
print("************************'")
list=['Apple','Banana','Carrot','Mango']
print(list[3])
print(list[-1])
print("************************'")
n1=[10,20,30,40,50]
n2=[10,20,30,40,50]
print(n1 is n2)
print(n1 == n2)
print("************************'")
a=bool([False])
print(a)
b=bool(3)
print(b)
c=bool("")
print(c)
d=bool(' ')
print(d)
print("************************'")
x= 8
y= 10
result= x//3*3/2+y%2**2
print(result)
print("************************'")
a=5
b=10
c=2
d=True
x=a+b*c
y=a+b/d
if(x > y):
    print('Valid')
else:
    print('invalid')
print("************************'")
courses={1:'Java',2:'Scala',3:'Python'}
#for i in range(1,5):
#    print(courses[i])
#While executing this code we are getting the following error
#Traceback (most recent call last):
#File "test.py", line 3, in <module>
#print(courses[i])
#KeyError: 4
for i in range(1,5):
    if i in courses:
        print(courses[i])
print("************************'")
for i in courses:
    print(courses[i])
print("************************'")
for i in range(1,4):
    print(courses[i])
print("************************'")
for k,v in courses.items():
    print(k, v)
print("************************'")
data=[]
def get_data():
    marks = 10
    for i in range(1,5):
        #marks=input('Enter Marks:')
        data.append(marks)
        marks += 10
def get_avg():
    sum=0
    for mark in data:
        sum += int(mark)
    return sum/len(data)
get_data()
print(get_avg())
print("************************'")
x=5#int(input('Enter First Number:'))
y=0#int(input('Enter Second Number:'))
try:
    print(x/y)
except(ZeroDivisionError,ValueError) as e:
    print(e)
print("************************'")

msg = "sssssssshhhrrrrrwwwwwwwwwwwwwwååååååååå+++++77777777#####´´´´´´&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤´'''''''cccccccccccccccccccccccccccrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrssssssssssssssssssssssssssssssssssssssssssssssssssssssss"
print(textwrap.fill(msg[:400], 50))

email_content = """
 
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>html title</title>
  <style type="text/css" media="screen">
    table{
        background-color: #AAD373;
        empty-cells:hide;
    }
    td.cell{
        background-color: white;
    }
  </style>
 
 
 
<table style="border: blue 1px solid;">
 
<tbody>
<tr>
<td class="cell">Cell 1.1</td>
<td class="cell">Cell 1.2</td>
</tr>
 
 
<tr>
<td class="cell">Cell 2.1</td>
<td class="cell"></td>
</tr>
 
</tbody>
</table>
ääääääääää
öööööööööö
ÅÅÅÅÅÅÅÅÅÅ

 
"""

print("************************'")
print(textwrap.fill(email_content[:800], 50))
print("************************'")
issue_str = "blaa blaa"
responsible_person = "patMat"
start_time = now()
print("************************'")
print(textwrap.fill(msg[:400], 50), issue_str, responsible_person, start_time)

L=[10,20,25,32,42]
b=bytearray(L)
print(b[0])
print(b[-1])

from random import *
otp=''
for i in range(6):
    otp=otp+str(randint(0,9))
print(otp)