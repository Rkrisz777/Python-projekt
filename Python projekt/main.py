from functions import *
choice = ''
while choice != '0':
    choice = menu()
    if choice == '0':
        Kilep()
    if choice == '1':
        Kilistazas()
    elif choice == '2':
         arFolyam()
    elif choice == '3':
        penzValtas()
    elif choice == '4':
        ujPenzFelvetel() 
    elif choice == '5':   
        penz = input('Adja meg a keresendő pénznemet: ')
        print(keresesAListában(penz))
        input()
    elif choice == '6':
        penzTörles()
        