from utils import *
import math

'''
Ejercicio 3
    En este problema debemos de definir una constante con el valor de PI 
    como 3,1416 y tenemos un único dato de entrada dado por el usuario: 
    un valor numérico que puede ser entero o flotante que indicara el 
    radio de un círculo. La salida del algoritmo será el área del circulo 
    teniendo en cuenta que A=PI*r^2. Si el usuario ingresó valor negativo 
    o cero tendremos que emitir un mensaje informando las causas por las 
    cuales no se podrá efectuar la operación.
'''


def calcular_area(numero: int | float) -> bool | float:
    # PI = 3.1416 # Definir una constante

    if numero < 0:
        print(error("El numero debe ser mayor a cero"))
        return False
    else:
        return round(math.pi * math.pow(numero, 2), 2)


def menu_radio_circulo():
    """
    Método para calcular el radio de un círculo
    """
    print(info("Calculadora de area de un circulo: "))

    numero = obtener_flotante(info("Ingrese el valor del radio del circulo: "))
    result = calcular_area(numero)
    if result:
        print(confirm(f"Para un circulo de {numero} de radio el area es: {result}"))
    else:
        print(error(f"Para un circulo de {numero} no se puede calcular el area"))
    # print(confirm("El numero es: " + ("par" if numero_es_par(numero) else "impar")))


if __name__ == '__main__':
    data = calcular_area(13.234567)
    if data:
        print(f"se pudo {data}")
    else:
        print("No se pudo")
