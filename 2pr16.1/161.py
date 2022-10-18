import re
a = re.match(r'\w\w.\w\w.\w\w\w\w', '19.092001')
if a!=None:
    print('True')
else:
    print('False')   
