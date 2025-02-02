import random


def poker_hand(cards):
    print(f"du fick ett par med valören:{cards}")

def slumpa_kort():
    color = ["ruter","hjärter", "spader", "klöver"]
    valor = [2, 3, 4,5,6,7,8,9,10,11,12,13,14]
    farg = random.choice(color)
    valor= random.choice(valor)
    return (farg,valor)

kort = slumpa_kort()
poker_hand(kort)

#jämför
def jamfor():
    spelkort_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    spelkort_2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

    jamfor_1 = random.choice(spelkort_1)
    jamfor_2 = random.choice(spelkort_2)

    if jamfor_1 == jamfor_2:
        print(f"korten har samma valör{jamfor_1}, {jamfor_2}")
    else:
        print("inget")

jamfor()
