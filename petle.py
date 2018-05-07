#x = 1
#w = 0
#while x < 10:
#	l = int(input("Podaj liczbę:"))
#	w += l
#	x += 1
#print(w)

lista = ['Kuba', 'Ania', 'Tomek', 'Ziomek']

for z in lista:
	print(z)

#for x in range(10):
#	print(x)
	
for y in range(1, 10, 3): #pierwsze dwa argumenty to zasieg, trzeci to krok co jaki maja byc generowane liczby. Wpisujac range (10) wygenerujemy liczby od 0 do 9 (w python zawsze zaczyna sie od 0)
		print(y)

l = range(1, 100)

for i in l:
	print(l[50])
	
