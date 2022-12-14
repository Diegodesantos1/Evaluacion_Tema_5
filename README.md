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
