"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    agrupado = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                partes = linea.split("\t")
                letra = partes[0]
                numero = int(partes[1])

                if numero not in agrupado:
                    agrupado[numero] = [letra]
                else:
                    agrupado[numero].append(letra)

    resultado = sorted(agrupado.items())  # ordenamos por los valores numéricos de columna 2
    return resultado
"""
Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
contiene un valor posible de la columna 2 y una lista con todas las letras
asociadas (columna 1) a dicho valor de la columna 2.

Rta/
[(0, ['C']),
    (1, ['E', 'B', 'E']),
    (2, ['A', 'E']),
    (3, ['A', 'B', 'D', 'E', 'E', 'D']),
    (4, ['E', 'B']),
    (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
    (6, ['C', 'E', 'A', 'B']),
    (7, ['A', 'C', 'E', 'D']),
    (8, ['E', 'D', 'E', 'A', 'B']),
    (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

"""
