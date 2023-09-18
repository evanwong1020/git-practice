import threading 
import random

def collatz(x):
    print(x)
    if(x == 1):
        return 0
    elif(x % 2 == 0):
        return collatz(x/2)
    elif(x % 2 == 1):
        return collatz(x + random.randint(1,100))

thread1 = threading.Thread(target=collatz, args=(random.randint(1,100),))
thread2 = threading.Thread(target=collatz, args=(random.randint(1,100),))

thread1.start()
thread2.start()

thread1.join()
thread2.join()