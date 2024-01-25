# This is a sample Python script.
from utils import error, info, advertencia, texto_es_numero
import ejercicio_01


def menu():
    while True:
        print("")
        print("----- Menu Principal ----")
        print(advertencia("Seleccione un ejercicio a ejecutar:"))
        print(advertencia("1) Cociente de 2 Numeros:"))
        print(advertencia("2) Numero par o impar"))
        print(advertencia("30) Salir"))
        print("")

        opcion = texto_es_numero(input())
        if opcion == 1:
            ejercicio_01.calcular_cociente()
        elif opcion == 2:
            print("Entre a 2")
        elif opcion == 30:
            print(info("Programa finalizado..."))
            exit(0)
        else:
            print(error("Opción no encontrada debe estar entre 1 y 30"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(info("Bienvenido al desarrollo del taller de logica de programación con python"))
    print(info("Nombres: Diego Alonso Ojeda Medina"))
    print(info("Ficha: 2670142"))
    print("")
    menu()

