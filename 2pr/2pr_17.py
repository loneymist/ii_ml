import random
import string
import re
def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string
datamass = []
invalid = []
valid1 = []
temppass = ''
tempmail = ''
i = 0
j = 0
c = 0
with open(r'2pr/data.txt','r') as data:
     lines = data.readlines()
     for line in lines:
        datamass.append(line.split(' '))
datamass.pop(0)
while i < 5:
        if len(datamass[i]) == 5 and re.match(r'\d\d.\d\d.\d\d\d\d\b',datamass[i][2])!=None and re.match(r'\+\d\d\d\d\d\d\d\d\d\d\d\b',datamass[i][4]):
                tempmail = datamass[i][0] + datamass[i][1]+generate_random_string(3) + '@corp.nstu.ru'
                temppass = generate_random_string(8)
                datamass[i].append(tempmail)
                datamass[i].append(temppass)
                valid1.append(datamass[i])
        else:
                invalid.append(datamass[i])
        i += 1         

with open(r'2pr/invalid.txt','w') as invalid1:
        for element in invalid:
                invalid1.write(str(element))
                invalid1.write('\n')


with open(r'2pr/valid.txt','w') as valid:
        for element in valid1:
                valid.write(str(element))
                valid.write('\n')
                
valid.close()
data.close()
invalid1.close()

# with open(r'2pr/data.txt','w') as data:
#         data.write('Name   Surname   DOB        COB      Email    Password'+'\n')
#         for element in valid1:
#                 data.write(str(element))
#                 data.write('\n')
# data.close()
