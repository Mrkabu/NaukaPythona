string = input("Podaj ciag znakow: ")

for i in ['a']:

    if i in string:
        string = string.replace(i, " 61")

for i in ['b']:

    if i in string:
        string = string.replace(i, " 62")

for i in ['c']:

    if i in string:
        string = string.replace(i, " 63")

print(string)