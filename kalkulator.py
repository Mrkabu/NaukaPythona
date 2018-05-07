print("Prosty kalkulator")

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

if (a < b):
	print("Liczba większa to ", b)
elif (b < a):
	print("Liczba większa to ", a)

c = int(input("Wybierz działanie (1 - dodawanie, 2 - odejmowanie, 3 - mnożenie, 4 - dzielenie) "))

if (c == 1):
	wynik = a + b
	#print(wynik1)
elif (c == 2):
	wynik = a - b
elif (c == 3):
	wynik = a * b
elif (c == 4 and b == 0):
	wynik = 'Błąd! Nie można dzielić przez 0!'
elif (c == 4):
	wynik = a / b
else:
	print("Dokonałeś złego wyboru!")

print("Wynik: ", wynik)