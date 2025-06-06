"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    suma_por_letra = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                partes = linea.split("\t")
                valor_col2 = int(partes[1])
                letras_col4 = partes[3].split(",")

                for letra in letras_col4:
                    if letra in suma_por_letra:
                        suma_por_letra[letra] += valor_col2
                    else:
                        suma_por_letra[letra] = valor_col2

    return dict(sorted(suma_por_letra.items()))

    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
