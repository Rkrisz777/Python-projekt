from data import *
from os import system
def menu():
    system('cls')
    print('0 - Kilép')
    print('1 - Valuták száma')
    print('2 - Árfolyam')
    print('3 - Átváltás')
    print('4 - Új pénznem felvétele')
    print('5 - Listázás')
    print('6 - Törlés')
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
    print('Euró-Forint')
    
    
