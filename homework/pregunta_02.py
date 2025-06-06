"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    conteo = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()  # eliminar saltos de línea
            if linea:
                partes = linea.split("\t")  # suponiendo que el separador es tabulador
                letra = partes[0]
                if letra in conteo:
                    conteo[letra] += 1
                else:
                    conteo[letra] = 1

    # Convertimos el diccionario en lista de tuplas y ordenamos alfabéticamente
    resultado = sorted(conteo.items())

    return resultado
"""

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
