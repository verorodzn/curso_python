''' Archivo con las funciones necesarias de la Aplicaicón Libro Web'''

import csv

def leer_libros(archivo:str) -> list:
    # Lee un archivo CSV con libros y devuelve una lista de diccionarios
    with open(archivo, "r", encoding="utf8") as archivo_csv:
        return [x for x in csv.DictReader(archivo_csv)]
    
def crea_diccionario_titulos(lista:list) -> dict:
    # Crea un dicconario con los títulos de los libros como clave y el resto de los datos como valores
    return {x["title"]: x for x in lista}

def busca_en_titulo(diccionario, palabra)-> list:
    # Busca una palabra en los títulos de los libros
    lista = []
    for titulo, libro in diccionario.items():
        if "rebels" in titulo.lower():
             lista.append(libro)
    return lista

if __name__ == '__main__':
    archivo_csv = "booklist2000.csv"
    lista_libros = leer_libros(archivo_csv)
    diccionario_libros = crea_diccionario_titulos(lista_libros)
    resultado = busca_en_titulo(diccionario_libros, "rebels")
    print(resultado)