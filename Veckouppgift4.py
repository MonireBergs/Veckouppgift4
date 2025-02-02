#1.skriv en funktion som tar en sträng som parameter
from operator import truediv


def my_function(namn):
    print(f"{namn} är en fena på programmering")

#2.a upprepar inmatade parametern
def eko(ekot):
    print(ekot*2)
eko("hej")

#2.b lägger till en count för att utöka antalet gånger
def eko(ekot, count):
    print(ekot * count)

eko("hej", 3)

#3.koden ska sluta loopa efter 5 gånger
def sluta_loopa():
    y = 1
    for x in range(1, 100):
        y *= 2
        if x == 5:
            print("slut på loop")
            break
    else:
        print (".")
    # avsluta loopen med en if-sats här
    print(y)

sluta_loopa()

# #4skriv en funktion med last och skriv ut sista siffran i listan
def last(lista):
    return lista[2]

print(last([1,2,3]))

#5.Skriv en funktion med namnet cut_edges. Den ska ta en lista som parameter. När den anropas ska den returnera en ny lista, där den har tagit bort första och sista elementet.

def cut_edges(lista):
    return lista[1:-1]

print (cut_edges([1,2,3,4,5]))

#6. lös felet
def increase(x):
    x += 1
    return x

print(increase(1))

#7.Bygg en funktion med namnet average. Den ska ta parametrar: x och y. Båda ska vara tal. Funktionen ska returnera medelvärdet. Till exempel så räknar man ut medelvärdet av 4 och 8 genom med formeln: (4 + 8) / 2, vilket blir 6.
def average(x,y):
    return (x+y)/2

print(average(4,8))

#8.Gör en funktion som kan skriva ut innehållet i en lista lite snyggare. Först ska funktionen tala om ifall listan är tom, eller hur många element den har. Sedan ska funktionen skriva ut elementen i en punktlista.
def snyggare_lista(listan):
    if len(listan) == 0:
        print("listan är tom")
    else:
        print(f"listan har {len(listan)} element:")
        for index in range(len(listan)):
            print(f"{index + 1}. {listan[index]}")

snyggare_lista(["a", "b", 3.14])





