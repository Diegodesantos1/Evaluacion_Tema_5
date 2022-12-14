<h1 align = "center"> Evaluación Tema 5</h1>

En este [repositorio](https://github.com/Diegodesantos1/Evaluacion_Tema_5) quedan resueltos los ejercicios de evaluación Tema 5

<h2 align = "center"> Ejercicio 1: Cálculos y Operaciones</h2>

![image](https://user-images.githubusercontent.com/91721855/207654234-d14efb14-d4df-41a0-a531-d3619b24625b.png)

El código empleado en operaciones es el siguiente:

```python
def suma(a, b):
    try:
        return a+b
    except TypeError:
        print("Error: Tipo de dato no válido")


def resta(a, b):
    try:
        return a-b
    except TypeError:
        print("Error: Tipo de dato no válido")


def producto(a, b):
    try:
        return a*b
    except TypeError:
        print("Error: Tipo de dato no válido")


def division(a, b):
    try:
        return a/b
    except TypeError:
        print("Error: Tipo de dato no válido")
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero")
```

El código empleado en cálculos es el siguiente:

```python
from ejercicios.operaciones import *

a, b, c, d = (10, 5, 0, "Hola")


def mainej1():
    print("{} + {} = {}".format(a, b, suma(a, b)))
    print("{} - {} = {}".format(b, d, resta(b, d)))
    print("{} * {} = {}".format(b, b, producto(b, b)))
    print("{} / {} = {}".format(a, c, division(a, c)))
```

<h2 align = "center"> Ejercicio 2: Contador</h2>

![image](https://user-images.githubusercontent.com/91721855/207654919-568ca91c-5834-466b-b3cc-99bf844bcba3.png)

El código empleado en contador es el siguiente:

```python
from io import open
import sys
import os

fichero = open("datos/contador.txt", "a+")
fichero.seek(0)
datos = fichero.readline()

if len(datos) == 0:
    datos = "0"
    fichero.write(datos)
fichero.close()
try:
    contador = int(datos)
    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            contador += 1
        elif sys.argv[1] == "dec":
            contador -= 1
    print("Contador: " + str(contador))
    fichero = open("datos/contador.txt", "w")
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
```
