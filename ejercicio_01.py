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


def calcular_cociente():
    """
    Metodo para calcular el cociente de dos numeros
    """
    print("")
    print(info("Calculadora de cociente: "))

    print(info("Ingrese el primer numero:"))
    numero_1 = texto_es_numero(input())

    print(info("Ingrese el segundo numero:"))
    numero_2 = texto_es_numero(input())

    if numero_2 == 0:
        print(error("La división por cero es una indeterminación"))
    else:
        resultado = numero_1 / numero_2
        print(confirm(f"El resultado del cociente es: {round(resultado, 2)}"))


if __name__ == '__main__':
    calcular_cociente()
