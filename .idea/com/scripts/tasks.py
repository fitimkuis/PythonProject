import re


with open("tasks.txt",'r') as file:
    data = file.read()
    r1 = re.findall(r"task\s\w+\s\w+\s\w+\s\w+\s\w+\s\d+",data)

print(r1)
with open("tasks.txt",'r') as file:
    data = file.read()
    r2 = re.findall(r"\d+",data)

print(r2)

r3 = list(map(int, r2))

print(r3) #list as integers

sum = 0
for i in range (len(r3)):
    print(r3[i])
    sum = sum + r3[i]

print(sum)

#minutes
minutes = (sum/1000)/60
print(minutes)

'''
f = open("tasks2.txt",'w')
for x in r2:
    f.write(x)
    #f.write('\n')
f.close()

with open("tasks2.txt",'r') as file:
    data = file.read()

print(data)
sum = data[0]+data[1]
print(sum)
#d = data.split(',')
#sumlist = [int(i) for i in data]
#print(d)


#print(sumlist)
'''