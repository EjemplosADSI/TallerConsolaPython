from utils import *

''' 
    Ejercicio 1
    
    En este problema, los datos de entrada son los dos valores enteros que ingresará
    el usuario a través del teclado (los llamaremos a y b) y la salida será su
    cociente (un número flotante). Ahora bien, existe la posibilidad de que el
    usuario ingrese como segundo valor el número 0 (cero). En este caso, no podremos
    mostrar el cociente ya que la división por cero es una indeterminación, así que
    tendremos que emitir un mensaje informando las causas por las cuales no se podrá
    efectuar la operación.
'''


def calcular_cociente(numero_1: int, numero_2: int) -> float:
    """

    :param numero_1:
    :param numero_2:
    :return:
    """
    if numero_2 == 0:
        print(error("La división por cero es una indeterminación"))
        return 0
    else:
        return round(numero_1 / numero_2, 2)


def menu_cociente():
    """
    Metodo para calcular el cociente de dos numeros
    """
    print("")
    print(info("Calculadora de cociente: "))

    numero_1 = obtener_entero(info("Ingrese el primer numero: "))
    numero_2 = obtener_entero(info("Ingrese el segundo numero: "))

    resultado = calcular_cociente(numero_1, numero_2)
    print(confirm(f"El resultado del cociente es: {resultado}"))


if __name__ == '__main__':
    a = 5
    b = 6
    print(calcular_cociente(a, b))
