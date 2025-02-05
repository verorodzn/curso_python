'''
Este archivo es el piunto de entrada a la aplicación. Aquí se importan las funciones de tablero.py y se ejecutan en un ciclo while.
'''

import tablero

def main():
    numeros = [str(i) for i in range(1,10)]
    dsimbolos = {x:x for x in numeros}
    g = tablero.juego(dsimbolos)

    if g is not None:
        print(f'El ganador es {g}')
    else:
        print('Empate')

if __name__ == '__main__':
    main()