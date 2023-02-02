import pyinputplus as pip
s=0
breadtype=pip.inputMenu(['wheat','white','sourdough'],prompt='What is ur preferred food?\n')
if breadtype=='wheat':
    s=s+204
elif breadtype=='white':
    s=s+240
else:
    s=s+200
protein=pip.inputMenu(['chicken','turkey','ham','tofu'],prompt='What is your preferred meat\n')
if protein=='chicken':
    s=s+104
elif protein=='turkey':
    s=s+104
elif protein=='ham':
    s=s+200
elif protein=='tofu':
    s=s+206
cheese=pip.inputYesNo(prompt='Do u want cheese?')
if cheese=='YES' or 'yes' or'Yes':
    s=s+10
number=pip.inputInt(min=1,prompt='Number pf sandwiches')
p=number*s
print(breadtype,protein,cheese,number)
print(p,':total amount',s,':for one burger')
