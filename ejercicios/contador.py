from io import open
import sys
import os

fichero = open("contador.txt", "a+")
fichero.seek(0)
contenido = fichero.readline()

if len(contenido) == 0:
    contenido = "0"
    fichero.write(contenido)
fichero.close()
try:
    contador = int(contenido)
    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            contador += 1
        elif sys.argv[1] == "dec":
            contador -= 1
    print("Contador: " + str(contador))
    fichero = open("contador.txt", "w")
    fichero.write(str(contador))
    fichero.close()
except:
    print("Error: Fichero corrupto.")


def mainej2():
    eleccion = str(input(
        "\n\n¿Qué quieres hacer?\ninc = incrementar\ndec = decrementar\nsal = salir\n"))
    if eleccion == "inc":
        os.system("python ejercicios/contador.py inc")
        mainej2()
    elif eleccion == "dec":
        os.system("python ejercicios/contador.py dec")
        mainej2()
    elif eleccion == "sal":
        pass
