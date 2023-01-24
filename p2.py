def fun(sum):
    l=len(sum)
    print(" ' ",end='')
    for i in range (0,l):
        print(sum[i],',',end=' ')
    print(" ' ")

s=[]
while True:
    n=(input())
    if(n==''):
        break
    else:
        s.append(n)
fun(s)
 
    

