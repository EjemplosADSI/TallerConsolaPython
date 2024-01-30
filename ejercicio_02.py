from utils import *

'''
Ejercicio 2
    En este problema tenemos un único dato de entrada: un valor numérico
    entero que deberá ingresar el usuario. La salida del algoritmo será
    informar si el usuario ingresó un valor par o impar.
    Sabemos que un número par es aquel que es divisible por 2 o, también,
    que un número es par si el valor residual que se obtiene al dividirlo
    por 2 es cero. Según lo anterior, podremos informar que el número
    ingresado por el usuario es par si al dividirlo por 2 obtenemos un resto
    igual a cero. De lo contrario, informaremos que el número es impar.
'''


def numero_es_par(numero: int) -> bool:
    return numero % 2 == 0


def menu_par():
    """
    Metodo para calcular el cociente de dos numeros
    """
    print(info("Validar numero par o impar: "))

    numero = obtener_entero(info("Ingrese el numero a validar: "))

    # print(confirm("El numero es: " + ("par" if numero_es_par(numero) else "impar")))
    print(confirm(f"El numero es: {numero_es_par(numero) and 'par' or 'impar'}"))


if __name__ == '__main__':
    a = 7
    print(numero_es_par(False))  # Bolean (1 True, 2 False)
    print(numero_es_par(0o123))  # Octal 83 Decimal
    print(numero_es_par(0x123))  # Hexa 291 Decimal
    print(numero_es_par(a))
    a = 1_827_838_945_867
    print(numero_es_par(a))
    menu_par()
