from data import *
from os import system
from random import randint
import time
filename = 'adat.csv'

def menu():
    system('cls')
    print('0 - Kilép')
    print('1 - Valuták listája')
    print('2 - Árfolyam')
    print('3 - Átváltás')
    print('4 - Új pénznem felvétele')
    print('5 - Keresés')
    # print('6 - Törlés')
    return input('Kérem válasszon: ')

def valutaSzam():
    system('cls')
    print('Valuták')
    for penz in penzek:
            print(f'\t{penz}')
    input('Tovább...')
def arFolyam():
    system('cls')
    print('Válasszon árfolyamot:')
    
    print(f'\t Euró árfolyam: Szeptember {eu[0]}ft , Október {eu[1]}ft, November {eu[2]}ft')
    print(f'\t Dollár árfolyam: Szeptember {usd[0]}ft , Október {usd[1]}ft, November {usd[2]}ft')
    print(f'\t Svájci-frank árfolyam: Szeptember {frank[0]}ft , Október {frank[1]}ft, November {frank[2]}ft')
    print(f'\t Vietnámi-dong árfolyam: Szeptember {dong[0]}ft , Október {dong[1]}ft, November {dong[2]}ft')
    input('Tovább...')
def penzValtas():
    system('cls')
    print('0 - eu')
    print('1 - usd')
    print('2 - frank')
    print('3 - dong')    
    ertek1 = input('Váltani kívánt pénznem: ')
    if ertek1 == '0':
         ertek2 = eu[randint(0,len(eu))-1]
    elif ertek1 == '1':
        ertek2 = usd[randint(0,len(usd))-1]
    elif ertek1 == '2':
        ertek2 = frank[randint(0,len(frank))-1]
    elif ertek1 == '3':
        ertek2 = dong[randint(0,len(dong))-1]

    mennyiseg1 = input('Kérem az átváltandó mennyiséget: ')
    print('Átváltva ennyi: ',ertek2 * int(mennyiseg1))
    time.sleep(2)

def ujPenzFelvetel():
    system('cls')
    print('Új pénznem feelvétele')
    penz = input('Valuta: ')
    ertek = float(input('Értéke: '))
    penzek.append(penz)
    ujertek.append(ertek)
    saveToFile(penz, ertek)
    print('Sikeres felvétel.')
    time.sleep(2)
def saveToFile(penz, ertek):
    file = open(filename, 'a', encoding='utf-8')
    
    file.write(f'{penz};{ertek}\n')

    file.close
def loadFromFile():
    file = open(filename, 'r', encoding='utf-8')
    for row in file:
        splitted = row.strip().split(';')
        penzek.append(splitted[0])
        ujertek.append(float(splitted[1]))
    file.close()

def keresesAListában(needle):
    system('cls')
    
    for penz in penzek:
        if penz == needle:
            return 'Létezik'
    return False
           
# def penzTörles():
#      system('cls')
#      print('Valuta törölve:')
#      penz = input('Ki legyen törölve: ')
#      index = keresesAListában(penz)
#      penzek.pop(index)
#      ujertek.pop(index)
#      saveAll()
#      print(f'{penz} törölve.')
#      input()
def saveAll():
    file = open(filename, 'w', encoding='utf-8')
    for index in range(len(penzek)):
        file.write(f'{penzek[index]};{ujertek[index]}\n')

    file.close
def Kilep():
    system('cls')
    
def Kilistazas():
    system('cls')
    print('Pénznemek listája:')
    for i in range(len(penzek)):
        print(f'\t {penzek[i]}')
    time.sleep(2)

    
    