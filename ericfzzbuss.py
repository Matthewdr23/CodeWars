#I want you to solve from x - 500
#for 3 it will show fuzz 
# if it is divisble by 5 it will show buzz
#if it is divisible by 3 & 5 it will show fizzbuzz but x is going to start at a random number from 50 to 100 as a starting number
import random
limit = 500
x = random.randrange(50, 100)
print(x)

def fizzbuzz(x):
    while x < limit:
        print(x+1)