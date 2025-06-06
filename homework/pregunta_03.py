"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    suma_por_letra = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                partes = linea.split("\t")  # suponiendo tabulador como separador
                letra = partes[0]
                valor = int(partes[1])
                if letra in suma_por_letra:
                    suma_por_letra[letra] += valor
                else:
                    suma_por_letra[letra] = valor

    resultado = sorted(suma_por_letra.items())
    return resultado
print(pregunta_03())
