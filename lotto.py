import random

liczba = random.randint(1, 45)

x = input("Podaj liczbę od 1 do 45 którą mam na myśli: ")

if int(x) <= 45:

	if x == liczba:
		print("Brawo!!! Zgadłeś")
	else:
		print("Niestety nie zgadłeś")
		print("Liczba którą miałem na myśli to: ", liczba)
else:
	print("Podana liczba jest z poza zakresu")