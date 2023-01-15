s=0
z=0
def collatz(number):
    s=0
    if(number%2==0):
        s=number//2
        return s
    elif(number%2!=0):
        s=3*number+1
        return s
num=int(input('enter a number'))
while z!=1:
    z=collatz(num)
    print(z)
    num=z