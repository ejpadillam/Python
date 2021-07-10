"""
Vectores/Listas

Como vimos en la parte teórica, los vectores son una estructura de dato organizada que nos permite 
almacenar información. Una de las implementaciones más utilizadas es Python son las listas (List). 

Nota: En Python hay algunas diferencias menores entre un arreglo (array) y una lista, 
pero por ahora vamos a asumir que son lo mismo.

Vamos a ver una definición de esta estructura en Python. Para crear una lista, utilizamos los corchetes 
y separamos los valores de nuestra estructura con una coma. 

Por ejemplo, en la siguiente instrucción estamos creando una lista llamada a con los valores 1, 3, 2, 5, 2.
"""

def ejemplo1():
    a = [1, 3, 2, 5, 2]
    print(a)

ejemplo1()

#Las listas no necesariamente tienen que ser de números, también pueden ser de texto:
def ejemplo2():
    nombres = ["María", "Juan", "Andrés"]
    print(nombres)

ejemplo2()

#Aquí van algunas funciones útiles cuando trabajamos con listas.
#    append(x) - inserta un nuevo valor x al final de la lista
#    remove(x) - remueve el primer valor X de la lista
#    pop([i]) - remueve el valor en la posición i. pop() remueve el último valor de la lista
#    len(x) - permite calcular el tamaño de una lista
#
# Ahora, veamoslas en acción
def ejemplo3():
    nombres = ["María", "Juan","Andrés"]
    nombres.append("Jorge")
    print(nombres)
    print(len(nombres))

    nombres.remove("Juan")
    print(nombres)
    print(len(nombres))

    nombres.pop(2)
    print(nombres)
    print(len(nombres))

ejemplo3()

#Actividad 1

# Usando el conocimiento de ciclos, crea una funcion numeros que tenga una lista con los numeros pares del 1 al 10 
# y usa un ciclo para que los imprima

def numeros():
    num_pares = [2, 4, 6, 8, 10]    # Definir e inicializar de vector manualmente
    for i in num_pares:             # Recorre las posiciones 
        print(i)                    # Imprime cada posicion recorrida en el "for"


def numeros1():
    num_pares = [i for i in range(2, 10+1, 2)]  #Compresion: Otra manera de definir e inicializar vector automaticamente
    for i in num_pares:
        print(i)

numeros()
print()
numeros1()


#actividad1()

#Actividad 2
#
#Escribamos un programa que nos permita crear una lista de 6 números aleatorios entre 1 y 20 en Python, y 
#creemos dos funciones que reciban la lista como parámetro de la siguiente forma:
#
#    mayor(x) - Una función que imprima el número mayor valor de una lista x
#    primos(x) - Una función que imprima los números de la lista que son números primos

#actividad2()

from random import randrange   # Se trae por importacion la libreria de aleatorios

def aleatorios():
    lista = []                              # Se define el vector
    for i in range(6):                      # Realiza un ciclo de 6 repeticiones
        lista.append(randrange(1, 20))      # En cada ciclo o repeticion, en la lista se añadirá un numero aleatorio entre 1 y 20.
    print(lista)                            # Imprime el resultado de la lista
    mayor(lista)                            # Define el numero mayor de esa lista aleatoria
    primos(lista)

def mayor(lista):
    print("Funcion para definir numero mayor dentro de una lista")
    mayor = 0
    for i in lista:
        if i > mayor:
            mayor = i
    print("El numero Mayor en la lista es: ", mayor)



def primos(list_val):
    print("Funcion para hayar numeros primos dentro de una lista")
    primo = True
    for i in list_val:
        for j in range(2, i):
            if i % j == 0:
                primo = False
                print("No hay numeros primos")
                break
    if primo:
        print("Numeros primos en la lista: ", i)


aleatorios()                                # Llama a la funcion aleatorio que este a su vez, llama a la funcion mayor                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                )




######################## Alimentar e imprimir arreglo automaticamente ##########################################

N = int(input("Ingrese la cantidad de posiciones para el vector: "))

valores = []                 #Se declara o define un vector vacio
for i in range(0, N):         #Se realiza rango de posiciones automaticamente
    valores.append(i)           #Se rellena vector de nanera automatica con la variable del rango

for i in range(0, N):           # Nuevamente se realiza rango para consultar la posicion de 0 hasta "N"
    print(valores[i])           #Se imprime la posicion consultada y asignada en la variable "i" del rango


print()
############################## Alimentar arreglo por teclado e imprimir ###########################################################

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8]
for i in range(0, N):
    numeros[i] = int(input(f"Digite dato a ingresar en la posición [{i}]: "))

for i in range(0, 5):
    print(numeros[i], end=", ")


##############################  ################################










