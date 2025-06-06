"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    conteo_por_mes = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                partes = linea.split("\t")  # suponiendo tabulador como separador
                fecha = partes[2]
                mes = fecha.split("-")[1]  # extrae el mes (MM)
                if mes in conteo_por_mes:
                    conteo_por_mes[mes] += 1
                else:
                    conteo_por_mes[mes] = 1

    resultado = sorted(conteo_por_mes.items())
    return resultado

print(pregunta_04())

"""
La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
cantidad de registros por cada mes, tal como se muestra a continuación.

Rta/
[('01', 3),
    ('02', 4),
    ('03', 2),
    ('04', 4),
    ('05', 3),
    ('06', 3),
    ('07', 5),
    ('08', 6),
    ('09', 3),
    ('10', 2),
    ('11', 2),
    ('12', 3)]

"""
