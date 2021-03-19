import string
import random

def passgen(length,with_digits=True,with_uppercase=True):
    mdp=string.ascii_letters+string.digits
    for i in range(length):
        res=random.choice(mdp)
        print(res,end="")

test=int(input("Enter a number to generate a password : "))
passgen(test)