def printGreeting():
    print("Buna ziua! Bine ati venit!")

def printGreetingByName(nume, prenume):
    print(f'Buna ziua {nume} {prenume}')

def MediaNr(a, b, c):
    return (a + b + c) / 3

def piValue():
    return 3.14

#exercitiu
# daca persoana este majora, altfel false
def verificareMajor(varsta):
    if varsta >= 18:
        return True
    else:
        return False


# ziba de apelare (desktop)
printGreeting()
printGreeting()
printGreetingByName('S', 'Andy')
print(MediaNr(3,3,7))
print(piValue())

# se ia varsta utilizatorului
age = int(input('introduceti varsta dvs'))
if verificareMajor((age)):
    print('Cont creat. Bine ai venit in aplicatie')
else:
    print('Nu ai varsta minimca necesara pentru a paria')

# oop
# variabile => atribute, proprietati sau fields
# functii => metode 
