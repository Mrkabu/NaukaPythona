print("Program do określenia humoru Iwonki: ")
list = []


for i in range(4):
	a = input("Podaj liczbę od 1 do 5, aby określic humor Iwonki: ")
	list.append(a)
	if (a == '1'):
  		print("Iwonka ma fatalny humor i nie ugotuje obiadu")
	elif (a == '2'):
  		print("Iwonka ma trochę lepszy humor i może się poprzytulacie")
	elif (a == '3'):
  		print("Iwonka ma w miarę dobry humor i jest szansa na bzykanko")
	elif (a == '4'):
  		print("Iwonka jest w tak dobrym humorze, że masz 90% szans na bzykanko i 70% na obiad")
	elif (a == '5'):
	  	print("Masz dużo szczęścia. Iwonka jest w tak dobrym humorze, że masz praktycznie 100% szans na bzykanko i obiad")
	else:
	 		 print("Dokonałeś złego wyboru. Uruchom program jeszcze raz, aby określić humor Iwonki")

#print(list)

print("Historia humoru Iwonki:")
for i in list:
	if (i == '1'):
		print("Iwonka ma fatalny humor i nie ugotuje obiadu")
	elif (i == '2'):
		print("Iwonka ma trochę lepszy humor i może się poprzytulacie")
	elif (i == '3'):
		print("Iwonka ma w miarę dobry humor i jest szansa na bzykanko")
	elif (i == '4'):
		print("Iwonka jest w tak dobrym humorze, że masz 90% szans na bzykanko i 70% na obiad")
	elif (i == '5'):
		print("Masz dużo szczęścia. Iwonka jest w tak dobrym humorze, że masz praktycznie 100% szans na bzykanko i obiad")