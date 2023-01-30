n=0
heads=0
tails=0
import random
while n<10001:
    n+=1
    h=0
    j=0
    t=0
    z=0
    l=[]
    for i in range (0,100):
        r=random.randint(0,1)
        if r==0:
            h+=1
            l.append('h')
        if r==1:
            t+=1
            l.append('t')
    print(l)
    print(h,t)
    i=0
    v=0
    for i in range(0,99):
        for j in range(1,100):
            if l[i]==l[j]:
                v+=1
                if(v==6):
                    if l[i]=='t':
                        j+=1
                        v=0
                    if l[i]=='h':
                        z+=1
                        v=0
                if l[i]!=l[j]:
                    v=0
    heads=z+heads
    tails=tails+j
print(heads//100)
print(tails//100)
