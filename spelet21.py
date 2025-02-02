#version 1
import random

def forsta_talet():
    summa = 0
    tal = 1

    for i in range (1,101):
        summa += tal
        if summa > 21:
            print(f"det första talet som gör att summan blir större än 21 är {tal}")
            break
        tal +=1

forsta_talet()

#version 2
def forsta_talet():
    kort = random.randint(1,13)
    print(f" random tal är: {kort}")
forsta_talet()



