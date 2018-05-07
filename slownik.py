dni = {"1" : "poniedziałek", "2" : "wtorek", "3" : "środa", "4" : "czwartek", "5" : "piątek", "6" : "sobota", "7" : "niedziela"}

a = input("Podaj numer dnia tygodnia: ")

if a == "1":
	print(dni["1"])
elif a == "2":
	print(dni["2"])
elif a == "3":
	print(dni["3"])
elif a == "4":
	print(dni["4"])
elif a == "5":
	print(dni["5"])
elif a == "6":
	print(dni["6"])
elif a == "7":
	print(dni["7"])
else:
	print("Dokonałeś złego wyboru!")