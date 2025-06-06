"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    valores = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                partes = linea.split("\t")  # suponiendo tabulador como separador
                letra = partes[0]
                numero = int(partes[1])
                
                if letra not in valores:
                    valores[letra] = [numero, numero]  # [max, min]
                else:
                    if numero > valores[letra][0]:
                        valores[letra][0] = numero
                    if numero < valores[letra][1]:
                        valores[letra][1] = numero

    resultado = [(letra, valores[letra][0], valores[letra][1]) for letra in sorted(valores.keys())]
    return resultado

"""
Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
por cada letra de la columa 1.

Rta/
[('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

"""
