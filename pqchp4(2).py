def my_func(L1):
    for name in L1:
        if(name==L1[-1]):
            print("and ",name)
            break
        else:
            print(name,",",end='')

l=input()
L=l.split(",")
my_func(L)