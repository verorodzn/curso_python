'''
tablero.py: Dibuja el tablero del juego del gato
'''

import random

def dibuja_tablero(simbolos:dict):
    '''
    Dibuja el tablero del juego del gato
    '''
    print(f'''
    {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
    ---------
    {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
    ---------
    {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
    ''')

def ia(simbolos:dict):
    '''
    Estrategia d ela computadora
    '''
    ocupado = True
    while ocupado is True:
        x = random.choice(list(simbolos.keys()))
        if simbolos[x] not in ['X', 'O']:
            simbolos[x] = 'O'
            ocupado = False

def usuario(simbolos:dict):
    '''
    Estrategia del usuario
    '''
    ocupado = True
    lista_numeros = [str(i) for i in range (1,10)] # Lista de números del 1 al 9
    while ocupado is True:
        x = input("Elija un número del 1 al 9: ")
        if x in lista_numeros:
            if simbolos[x] not in ['X', 'O']:
                simbolos[x] = 'X'
                ocupado = False
            else:
                print("Esa casilla ya está ocupada")

if __name__ == '__main__':
    numeros = [str(i) for i in range(1,10)]
    dsimbolos = {x:x for x in numeros}
    dibuja_tablero(dsimbolos)
    ia(dsimbolos)
    dibuja_tablero(dsimbolos)
    usuario(dsimbolos)
    dibuja_tablero(dsimbolos)