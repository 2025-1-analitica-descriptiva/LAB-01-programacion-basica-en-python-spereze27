"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    agrupado = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                partes = linea.split("\t")
                letra = partes[0]
                numero = int(partes[1])

                if numero not in agrupado:
                    agrupado[numero] = set()
                agrupado[numero].add(letra)  # usamos set para evitar repeticiones

    # Convertimos el diccionario en lista de tuplas con las letras ordenadas
    resultado = []
    for numero in sorted(agrupado.keys()):
        letras_ordenadas = sorted(agrupado[numero])
        resultado.append((numero, letras_ordenadas))

    return resultado

"""
Genere una lista de tuplas, donde el primer elemento de cada tupla
contiene  el valor de la segunda columna; la segunda parte de la tupla
es una lista con las letras (ordenadas y sin repetir letra) de la
primera  columna que aparecen asociadas a dicho valor de la segunda
columna.

Rta/
[(0, ['C']),
    (1, ['B', 'E']),
    (2, ['A', 'E']),
    (3, ['A', 'B', 'D', 'E']),
    (4, ['B', 'E']),
    (5, ['B', 'C', 'D', 'E']),
    (6, ['A', 'B', 'C', 'E']),
    (7, ['A', 'C', 'D', 'E']),
    (8, ['A', 'B', 'D', 'E']),
    (9, ['A', 'B', 'C', 'E'])]

"""
