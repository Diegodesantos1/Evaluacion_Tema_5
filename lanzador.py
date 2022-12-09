import os
from introducir.numero import solicitar_introducir_numero_extremo
from ejercicios.calculos import mainej1
from ejercicios.contador import mainej2
from ejercicios.reloj import mainej4
from colorama import Fore


def lanzador():
    eleccion = solicitar_introducir_numero_extremo(
        Fore.CYAN + "\n\nBienvenido al lanzador de ejercicios.\n1: Operaciones\n2: Contador\n3: Gestor\n4: Reloj\n5: Salir\n", 1, 5)
    print(Fore.RESET)
    if eleccion == 1:
        os.system("cls")
        mainej1()
        lanzador()
    elif eleccion == 2:
        os.system("cls")
        mainej2()
        lanzador()
    elif eleccion == 3:
        os.system("cls")
        pass
    elif eleccion == 4:
        mainej4()
    elif eleccion == 5:
        exit()


lanzador()
