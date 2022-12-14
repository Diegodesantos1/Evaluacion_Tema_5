<h1 align = "center"> Evaluación Tema 5</h1>

En este [repositorio](https://github.com/Diegodesantos1/Evaluacion_Tema_5) quedan resueltos los ejercicios de evaluación Tema 5

<h2 align = "center"> Ejercicio 1: Cálculos y Operaciones</h2>

![image](https://user-images.githubusercontent.com/91721855/207655563-595d378f-242a-4064-b2d7-74405fb63963.png)

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

![image](https://user-images.githubusercontent.com/91721855/207655474-e2c61855-b098-4f70-80f4-21acd795ff48.png)


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

<h2 align = "center"> Ejercicio 3: Gestor</h2>

![image](https://user-images.githubusercontent.com/91721855/207655415-ae7785a2-9700-479c-be18-a3da0bc79f51.png)

El código empleado en el gestor es el siguiente:

```python
from io import open
import pickle


class Personaje:

    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

    def __str__(self):
        return "{} : {} vida, {} ataque, {} defensa, {} alcance".format(self.nombre, self.vida, self.ataque, self.defensa, self.alcance)


class Gestor:

    personajes = []

    def __init__(self):
        self.cargar()

    def agregar(self, p):
        for personaje_temporal in self.personajes:
            if personaje_temporal.nombre == p.nombre:
                return
        self.personajes.append(p)
        self.guardar()

    def borrar(self, nombre):
        for personaje_temporal in self.personajes:
            if personaje_temporal.nombre == nombre:
                self.personajes.remove(personaje_temporal)
                self.guardar()
                print("\nPersonaje {} borrado".format(nombre))
                return

    def mostrar(self):
        if len(self.personajes) == 0:
            print("El gestor está vacío")
            return
        for p in self.personajes:
            print(p)

    def cargar(self):
        fichero = open("datos/personajes.pkl", "ab+")
        fichero.seek(0)
        try:
            self.personajes = pickle.load(fichero)
        except:
            print("El fichero está vacío")
            pass
        finally:
            fichero.close()
            print("Se han cargado {} personajes".format(len(self.personajes)))

    def guardar(self):
        fichero = open("datos/personajes.pkl", "wb")
        pickle.dump(self.personajes, fichero)
        fichero.close()


def mainej3():
    gestor = Gestor()
    gestor.agregar(Personaje("Caballero", 4, 2, 4, 2))
    gestor.agregar(Personaje("Guerrero", 2, 4, 2, 4))
    gestor.agregar(Personaje("Arquero", 2, 4, 1, 8))
    gestor.mostrar()
    gestor.borrar("Arquero")
    gestor.mostrar()
```

<h2 align = "center"> Ejercicio 4: Reloj</h2>

![image](https://user-images.githubusercontent.com/91721855/207656726-1542f25e-9fa1-4570-81d2-0c58f663737f.png)

El código empleado en el reloj es el siguiente:

```python
import datetime
import time
import os


def mainej4():

    while True:
        os.system('cls')
        tiempo = datetime.datetime.now()
        print(tiempo.hour, ":", tiempo.minute, ":", tiempo.second)
        time.sleep(1)
```
