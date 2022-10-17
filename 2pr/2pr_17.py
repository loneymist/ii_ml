datamass = []
invalid = []
i = 0
j = 0
c = 0
with open(r'2pr/data.txt','r') as data:
     lines = data.readlines()
     for line in lines:
        datamass.append(line.split(' '))
datamass.pop(0)
print(len(lines))
while i < 4:
        if len(datamass[i]) == 4:
                 c += 1
        else:
                invalid.append(datamass[i])
        i += 1         
print(c)
print(invalid)