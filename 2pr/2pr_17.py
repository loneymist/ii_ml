datamass = []
with open(r'data.txt','r') as data:
     lines = data.readlines()
     for line in lines:
        datamass.append(line.split(' '))
print(datamass)