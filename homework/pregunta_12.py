"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_12():
    resultado = {}
    with open("files/input/data.csv", "r") as file:
        for linea in file:
            columnas = linea.strip().split("\t")  # Ajusta el separador si es necesario
            clave = columnas[0]
            valores_str = columnas[4]  # ejemplo: 'jjj:12,bbb:3,ddd:9,ggg:8,hhh:2'

            # Parsear y sumar los números dentro de la columna 5
            suma_valores = 0
            for par in valores_str.split(","):
                # cada par es algo como 'jjj:12'
                _, valor = par.split(":")
                suma_valores += int(valor)

            # Acumular la suma para cada clave
            if clave in resultado:
                resultado[clave] += suma_valores
            else:
                resultado[clave] = suma_valores
    return resultado

print(pregunta_12())

"""
Genere un diccionario que contengan como clave la columna 1 y como valor
la suma de los valores de la columna 5 sobre todo el archivo.

Rta/
{'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

"""
