import re
date=re.compile(r'(0[0-9]|1|2[0-9]|3[0-2])/(0[1-9]|1[1-2])/([1-2][0-9]{3})')
m=date.search('31/09/2004')
print(m)
while True:
    day=int(m.group(1))
    month=int(m.group(2))
    year=int(m.group(3))
    break
print(day,month,year)
if month==2:
    if day>29:
        print('invalid')
    if year%100!=0 or year%400!=0:
        print('invalid year')
if month==4 or month==9 or month==11 or month==6:
    if day>30:
        print('invalid date')