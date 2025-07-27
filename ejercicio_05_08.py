from utils import *
from datetime import datetime

'''
    Ejercicio 5
    En este problema Se ingresa un valor numérico de 8 dígitos que
    representa una fecha con el siguiente formato: aaaammdd.

    Esto es: los 4 primeros dígitos representan el año, los siguientes 2 dígitos
    representan el mes y los 2 dígitos restantes representan el día.

    Se pide informar por separado el día, el mes y el año de la fecha ingresada.
    Para su solución se debe de hacer uso de divisiones,
    operador modulo y conversión de double a entero

    Ejercicio 8
    ingresa un valor numérico de 8 dígitos que representa una fecha
    con el siguiente formato: aaaammdd verificar si la fecha es
    correcta en sentido de numero de meses y días.
'''


def validar_fecha(cadena: str, formato: str = '%Y%m%d') -> bool:
    try:
        fecha = datetime.strptime(cadena, formato)  # Intentar convertir la cadena en un objeto datetime
        # anio, mes, dia = fecha.year, fecha.month, fecha.day # Empaquetamiento y Desempaquetamiento
        return True
    except ValueError as msg_error:
        # print(error(msg_error))

        return False


def extraer_fecha(fecha: int) -> ():  # Tupla

    # Solucion con conversion a string
    str_fecha = str(fecha)
    if len(str_fecha) == 8:
        if validar_fecha(str_fecha):
            # Desempaquetado de secuencias, Segmentación de cadenas y tuplas
            return str_fecha[:4], str_fecha[4:6], str_fecha[6:]
        else:
            print(error(f"La cadena {str_fecha} no es fecha real valida..."))
    else:
        print(error(f"La cadena {str_fecha} no esta en el formato correcto aaaammdd..."))

    # Solution sin conversion
    # Encadenamiento de comparaciones # and fecha not in [20000000, 30000000, 40000000] # %, +, -, *, /, **

    # if fecha >= 10000000 and fecha <= 99999999:
    # if 10000000 <= fecha <= 99999999: # Valida que sean 8 digitos
    #     if validar_fecha(str(fecha)):
    #         anio = fecha // 10000 # Division entera #19901210
    #         mes = (fecha % 10000) // 100
    #         dia = fecha % 100
    #         return anio, mes, dia
    return False


def menu_validar_fecha():
    # """
    # Método para validar si una fecha es valida en un formato de aaaammdd
    # """
    print(info("Validacion de fecha (aaaammdd)"))

    numero = obtener_entero(info("Ingrese una fecha en el formato aaaammdd:"))
    result = extraer_fecha(numero)
    if result:
        print(confirm(f"El numero {numero} representa la fecha {result[2]}/{result[1]}/{result[0]} que es valida"))


if __name__ == '__main__':
    menu_validar_fecha()
    # print(extraer_fecha(20240229))
    # print(extraer_fecha(2345))
    # print(extraer_fecha(20250229))
