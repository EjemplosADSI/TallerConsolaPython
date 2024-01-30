# This is a sample Python script.
import ejercicio_01
import ejercicio_02
import ejercicio_03
from utils import *


def menu():
    while True:
        print(texto_color("----- Menu Principal ----", "magenta"))
        print(advertencia("Seleccione un ejercicio a ejecutar:"))
        print(advertencia("1) Cociente de 2 Numeros:"))
        print(advertencia("2) Numero par o impar"))
        print(advertencia("3) Radio del Circulo"))
        print(advertencia("30) Salir"), end="\n", sep="-")

        opcion = obtener_flotante("")
        if opcion == 1:
            ejercicio_01.menu_cociente()
        elif opcion == 2:
            ejercicio_02.menu_par()
        elif opcion == 3:
            ejercicio_03.menu_radio_circulo()
        elif opcion == 30:
            print(info("Programa finalizado..."))
            exit(0)
        else:
            print(error("Opción no encontrada debe estar entre 1 y 30"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(info("Bienvenido al desarrollo del taller de logica de programación con python"))
    print(info("Nombres: Diego Alonso Ojeda Medina"))
    print(info("Ficha: 2670142"), end="\n")
    menu()
