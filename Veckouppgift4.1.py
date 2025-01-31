#uppgift 1a
# t finns inte skrivet i funktionens kropp därför skriver den bara ut "test"
print("uppgift 1a fel version:")
def foo(t):
    print("test")
foo("hej")


#för att skriva ut hej måste man skriva så här:
print("uppgift 1a rätt version:")
def foo(t):
    print(t)
foo("hej")

#uppgift 1b
#Skriver inte ut multiplikationen för att den printar bara talen.
print("uppgift 1b fel version: ")
def fun1(x, y):
    return x * y
print(3, 5)

#för att skriva ut multiplikationen måste man göra på följane sätt:
print("uppgift 1b rätt version:")
def fun1(x, y):
    return x * y
print(fun1 (3, 5))

#uppgift 1c
print("uppgift 1c, samma svar som ovan:")
def fun1(x, y):
    return x * y

print(fun1(3, 5))

#uppgift 1d
print("uppgift 1d rätt svar:")
def fun2(i):
    return 5 * i
x = 2
y = 3
a = fun2(fun2(x) + fun2(y))
print(a)

#uppgift 1e
#eftersom a är definerad utanför måste man ange global för att komma åt den
print("uppgift 1e rätt version:")
a = 5
def fun3():
    global a
    a += 1
fun3()
print(a)

#uppgift 1f
#Jag förstår inte varför i är = 3?! Annars förstår jag själva gången...
def foo(i):
    return 2*i*i

def goo(x, y):
    return x(y)

a = goo(foo, 3);
print(a)

#uppgift 1g
#skriver ut true true
print("uppgift 1g rätt version:")
def is_number(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    return False

print(is_number(2.0))
print(is_number(42))

#uppgift 1h
#den skrev inte ut eftersom den saknade print
def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found

result = average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])
print(result)

#uppgift 1i
#1. funktionsnamnet vill att man ska hitta minsta värdet?
#2. -11, inget värde, 100
#3. Rättar genom att för utskrift nr 2 sätta en retur på att det saknas värde/none.
# För utskrift 3 behöver vi sätta startvärdet för counter till listans första positition (vilket är talet 10) eller positionen [0]

def find_min(numbers):
    if not numbers:
        print("listan har inga siffor")
        return None

    counter = numbers[0]
    for item in numbers:
        if item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter

find_min([10, 3, -4, -11]) #utskrift 1
find_min([]) #utskrift 2
find_min([100]) #utskrift 3













