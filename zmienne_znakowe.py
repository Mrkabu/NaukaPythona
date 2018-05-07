import string
import sys

imie = input("Podaj imię:")
print("id:", id(imie)) #pokazuje, gdzie w pamieci zapisano zmeinna

print(imie[2]) #wyswietla trzeci znak z wprowadzonego imienia, numerowanie zaczyna sie od 0
print(imie[1:4])
print(imie.capitalize()) #zmienia wielkosc pierwszego znaku na kapitalik

print(len(sys.argv))
print(str(sys.argv))
print(str(sys.argv[0]))

print(imie.upper()) #kapitaliki dla wszystkich znakow

rok = input("Podaj dwie pierwsze cyfry aktualnego roku:")
rok2 = input("Podaj dwie ostatnie cyfry roku:")

rok3 = int(rok)
rok4 = int(rok2)

print(rok3[0:1], rok4[0:1])