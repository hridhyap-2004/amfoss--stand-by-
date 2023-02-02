import random
import time
for i in range (0,10):
    n1=random.randint(0,9)
    n2=random.randint(0,9)
    max_time =8
    start_time = time.time() 
    answer=int(input())
    while (time.time() - start_time) < max_time:
        if(answer==(n1*n2)):
            print('correct')
            time.sleep(1)
        else:
            try2=int(input())
            try3=int(input())
        if (try3==(n1*n2) or try2==(n1*n2)):
            print('Correct!')
            time.sleep(1)