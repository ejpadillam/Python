"""
Funciones

La verdad es que hemos venido trabajando con funciones desde que empezamos con archivos .py 
En Python, definimos una función con la siguiente estructura

def funcion(parametros)

Recuerda que los parametros son opcionales!
"""

# Contabilizar los pacientes para vacunacion por covid con edad >= 50 años 
# de acuerdo a la cantidad de dosis dispuesta para ello
# Los que no cumplan esa condicion, no serán vacunados

from datetime import date

def calcular_edad(fecha_nacimiento):
    fecha_actual = date.today()
    result = fecha_actual.year - fecha_nacimiento.year
    return result



cantDosis = int(input("Ingrese la cantidad de dosis disponibles: "))
cantPac = 0
NoVacun = 0
edad = 0
while cantDosis > 0:
    dia = int(input("Ingrese dia de nacimiento: "))
    mes = int(input("Ingrese mes de nacimiento: "))
    año = int(input("Ingrese año de nacimiento: "))
    fechaNac = date(year = año, month = mes, day = dia)
    edad = calcular_edad(fechaNac)
    
    print()

    if edad >= 50:
        cantDosis -= 1
        cantPac += 1
        print("El(La) paciente tiene ", edad, " años de edad - PERMITIDO(A) VACUNAR")
        print()
        print("Cantidad de dosis disponibles: ", cantDosis)
        print()
        print("Cantidad de pacientes Vacunados: ", cantPac)
        print("########################################################################")
    else:
        print("No cumple con la condicion de edad para ser vacunado(a), SIGUIENTE!!!")

    print()
    NoVacun += 1

print("Cantidad de dosis agotadas")
print("Total pacientes vacunados", cantPac)
print("Cantidad personas no aptas: ", NoVacun)





#Actividad 1
#Usted es cajero en un supermercado de su ciudad. Su trabajo es imprimir cada uno de los productos de su cliente, su precio y calcular el total a pagar.
#
#Diseña un programa con las siguiente características:
#
#    1. Que tenga una función caja que solicite al usuario nombre y precio de cada producto.
#    2. Una variable total que vaya sumando el precio de los artículos
#    3. Una función adicional llamada imprimaProducto(nombre, precio) que reciba el nombre y
#        el precio de cada producto y los imprima.
#    4. Que después de llamar a imprimaProducto le pregunte al usuario si tiene o no más artículos a ingresar. 
        #Si no tiene, el programa debe detenerse.
#    5. Si no hay más artículos, que imprima el total de la compra

#    Al final de tus funciones, puedes simplement llamar a la función caja para probar


# -----------------definicion dee funciones----------------------

def imprimaProducto(nombre, precio):
    print("Producto: (", nombre, ") - Precio: ($", precio ,")")


def caja():
    nombre = input("Digite nombre de producto: ")
    precio = int(input("Digite el precio del producto: "))
    total = precio

    imprimaProducto(nombre, precio)
    print()

    continuar = True
    while continuar:
        seguir = input("Desea ingresar mas productos. (Si -s / No -n): ")
        if seguir == "Si" or seguir == "s" :
            nombre = input("Digite nombre de producto: ")
            precio = int(input("Digite el precio del producto: "))
            total += precio
            imprimaProducto(nombre, precio)
            print()
        else:
            continuar = False
            #break   # tambien se puede cortar la ejecucion con break.
    print()
    print("Total precio de los productos es: ", total)
    print()

# ------------------Programa principal----------------------

caja()



#Actividad 2
#
#Escribamos una función numAleatorio() que retorne un número aleatorio entre 100 y 130, 
#excepto los números 110, 115 y 120 .
#
#Adicionalmente, una función numeros que imprima diez números aleatorios 
#(retornados por la función numAleatorio()) alternando par, impar, comenzando por par.

from random import random, randrange
import os

def numAleatorio():
    num = 0
    while True:
        num = randrange(100, 130)
        if num != 110 or num != 115 or num != 120:
            break
    return num

def numeros():
    par = True
    for i in range(1, 10+1):
        numero = numAleatorio()
        if numero % 2 == 0 and par == True:
            print(numero)
            par = False
        elif numero % 2 != 0 and par == False:
            print(numero)
            par = True

numeros()    # Llamado a la funcion principal







