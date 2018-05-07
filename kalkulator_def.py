def dodawanie(a, b):
	d = a + b
	return d

def odejmowanie(a, b):
	d = a - b
	return d
def mnozenie(a, b):
	d = a * b
	return d
def dzielenie(a, b):
	d = a / ba
	return d

a = int(input("Wprowadź 1 liczbę "))
b = int(input("Wprowadź 2 liczbę"))
c = int(input("Wybierz działanie"))
	
if (c == 1):
	wynik = dodawanie(a, b)
else:
	print("zle")

print("Wynik to", wynik)