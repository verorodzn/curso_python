'''
Funciones auxiliares del juego Ahorcado
'''

def carga_archivo_texto(archivo:str) -> list:
    ''''
    Carga un archivo de texto y regresa una lista con el contenido del archivo
    '''
    with open(archivo, "r", encoding="utf-8") as file:
        contenido = file.readlines()
    return contenido

def carga_plantillas(nombre_plantilla:str)-> dict:
    '''
    Carga las plantillas del juego a partir de un archivo de texto
    '''
    plantillas = {}
    for i in range(6):
        plantillas[i] = carga_archivo_texto(f"./ahorcado/plantillas/{nombre_plantilla}-{i}.txt")
        return plantillas
    
def despliega_plantilla(diccionario:dict, nivel:int):
    ''''
    Despliega una plantilla del juego
    '''

    if nivel in diccionario:
        template = diccionario[nivel]
        for renglon in template:
            print(renglon)



if __name__ == "__main__":
    plantillas = carga_plantillas("plantilla")
    despliega_plantilla(plantillas, 5)
    despliega_plantilla(plantillas, 4)
    despliega_plantilla(plantillas, 3)
    despliega_plantilla(plantillas, 2)
    despliega_plantilla(plantillas, 1)
    despliega_plantilla(plantillas, 0)