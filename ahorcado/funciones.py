'''
funciones auxiliares del juego Ahorcado
'''
import string
import unicodedata
from random import choice
def carga_archivo_texto(archivo:str)->list:
    '''
    Carga un archivo de texto y devuelve una lista con las oraciones del archivo
    '''
    with open(archivo, 'r',encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones
def carga_plantillas(nombre_plantilla:str)->dict:
    '''
    Carga las plantillas del juego apartir de un archivo de texto
    '''
    plantillas = {}
    for i in range(6):
        plantillas[i] = carga_archivo_texto(f'./plantillas/{nombre_plantilla}-{i}.txt')
    return plantillas
def despliega_plantilla(diccionario:dict, nivel:int):
    '''
    Despliega una plantilla del juego
    '''
    if nivel in diccionario:
        template = diccionario[nivel]
        for renglon in template:
            print(renglon)
def obten_palabras(lista:list)->list:
    '''
    Obtiene las palabras de un texto
    '''
    texto = ' '.join(lista[120:])
    palabras = texto.split()
    # convertimos a minusculas
    minusculas = [palabra.lower() for palabra in palabras]
    set_palabras = set(minusculas)
    # removemos signos de puntuación y caracteres especiales
    set_palabras = {palabra.strip(string.punctuation) for palabra in set_palabras}
    # removemos números, paréntesis, corchetes y otros caracteres
    set_palabras = {palabra for palabra in set_palabras if palabra.isalpha()}
    # removemos acentos
    set_palabras = {unicodedata.normalize('NFKD', palabra).encode('ascii', 'ignore').decode('ascii') for palabra in set_palabras}
    return list(set_palabras)

def adivina_letra(abc:dict, palabra:str, letras_adivinadas:set, turnos:int):
                letras_adivinadas.add(letra)
            else:
                turnos -= 1
    return turnos

if __name__ == '__main__':
    plantillas = carga_plantillas('plantilla')
@@ -84,5 +86,7 @@ def adivina_letra(abc:dict, palabra:str, letras_adivinadas:set, turnos:int):
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    t = 5 # oportunidades
    adivina_letra(abcdario, p, adivinadas, t)
    adivina_letra(abcdario, p, adivinadas, t)
    t = adivina_letra(abcdario, p, adivinadas, t)
    print(t)
    t = adivina_letra(abcdario, p, adivinadas, t)
    print(t)