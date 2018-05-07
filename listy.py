lista = []
lista2 = [1, '5', 'siema', 'nara', 'pa']

l1 = int(input("Podaj pierwszy element listy: "))
lista.append(l1)

l2 = input("Podaj drugi element listy: ")
lista.append(l2)

l3 = input("Podaj trzeci element listy: ")
lista.append(l3)

l4 = input("Podaj czwarty element listy: ")
lista.append(l4)

l5 = input("Podaj piąty element listy: ")
lista.append(l5)

print("Lista zawiera: ", lista)
print(len(lista))
lista2.extend(lista) #rozszerzenie jednej listy za pomocą drugiej - lista 2 zostaje rozszerzona przez lista
print(lista2)
print(lista[2])