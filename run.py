#  https://www.youtube.com/watch?v=XHWi2f9KziU
#  https://www.youtube.com/watch?v=U80-XkPne-8

class Calculator():  #  to jest definicja klasy

#  cialo klasy

    def __init__(self):  #  metoda magiczna init, wykona sie w kazdym utworzonym obiekcie na podstawie klasy Calculator
        print('Init')

    def __del__(self):  #  metoda magiczna wykonuje sie w trakcie usuwania obiektu, mozna tez usuwac zmienne wpisujac del nazwa_zmiennej
        print('Del')

    def __str__(self):  #  metoda magiczna, wykonuje sie gdy chcemy przekonwertowac nasza klase na ciag znakow
        return 'Hello'

    def __int__(self):  #  metoda magiczna, zwraca liczbe
        return 10

    def __len__(self):  #  metoda magiczna, oblicza dlugosc
        return 5

    def __bool__(self):
        return True

    def dodaj(self, a, b):  #  deklaracja funkcji
        wynik = a + b
        print('Wynik dodawania to: ', wynik)

    def odejmik(self, a, b):  #  deklaracja funkcji
        wynik = a - b
        print('Wynik dodawania to: ', wynik)

# klasa to struktura obiektu, obiekt jest utworzeniem kalasy, np. to jest Tomek

calc = Calculator()  #  to jest obiekt
calc.dodaj(10, 15)  # zeby wykonac to dzialanie niezbedne jest stworzenie obiektu jak wyzej

print(int(calc))

calc_2 = Calculator()
calc_2.dodaj(5, 25)

def main():
    calc = Calculator()
    calc.dodaj(25, 4)

wynik = int(calc) + 50  #  10 z int plus 50
print(wynik)
print(len(calc))

if calc:
    print('True')
else:
    print('False')

main()  #  wykonanie funkcji