import re
password=re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$')
mo=password.search('OBAMAara1234')
print(mo.group())
