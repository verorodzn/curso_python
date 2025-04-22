'''Programa qye busca una lista de oalabras en las frases célebres de películas'''
import os
import csv
import argparse

# Función para leer el archivo CSV y devolver una lista de frases
def leer_csv(archivo):
    '''Lee un archivo CSV y devuelve una lista de frases.'''
    frases = []
    with open(archivo, 'r', encoding='utf-8') as f:
        lector = csv.reader(f)
        for fila in lector:
            if len(fila) > 0:
                frases.append(fila[0])
    return frases

# Función para buscar palabras en las frases
def buscar_palabras(frases, palabras):
    '''Busca una lsita de palabras en una lista de frases'''
    frases_encontradas = []
    for frase in frases:
        for palabra in palabras:
            if palabra.lower() in frase.lower():
                frases_encontradas.append(frase)
                break  # Si se encuentra una palabra, no es necesario seguir buscando en la misma frase
    return frases_encontradas

# Función para mostrar las frases encontradas
'''Imprime las frases encontradas en la consola'''
def mostrar_frases(frases):
    if len(frases) > 0:
        print("Frases encontradas:")
        for frase in frases:
            print(f"- {frase}")
    else:
        print("No se encontraron frases que contengan las palabras buscadas.")

    ''''for frase in frases:
        print(frase)'''

# Función principal
'''Función princial del programa'''
def main(archivo:str, lista_palabras:list):
    # Leer el archivo CSV
    frases = leer_csv(archivo)

    # Buscar las palabras en las frases
    frases_encontradas = buscar_palabras(frases, lista_palabras)

    # Mostrar las frases encontradas
    mostrar_frases(frases_encontradas)

if __name__ == "__main__":
   # Crear el parser
   parser = argparse.ArgumentParser(description="Buscar palabras en frases célebres de películas.")

   # Añadir argumentos
   parser.add_argument("palabras", nargs='+', help="Lista de palabras a buscar en las frases.")

   # Parsear los argumentos
   args = parser.parse_args()
   archivo = os.path.join(os.path.dirname(__file__), 'frases.csv')

   # Llamar a la función principal
   main(archivo, args.palabras)