"""
Mientras Que

Como vimos anteriormente, en Python, el ciclo Mientras Que se maneja con "while". 

La opción break, puede parar el ciclo aunque la condición sea real. Por ejemplo:
"""

"""def ejemplo1():
    i = 1
    while i < 6:
        print(i)
        if i == 3:
            break
        i += 1 
ejemplo1()

def actividad1():
    print("actividad1")"""
    # Continuemos integrando los conceptos que hemos visto hasta el momento. 
    # Ahora vamos a elaborar un algoritmo que pida un número al usuario, 
    # e imprima todos los números pares desde 2 hasta el número pero que termine el proceso si llega al 10.

"""numero = int(input("Ingrese un valor: "))
cont = 2
while cont < numero:
    print(cont)
    if cont == 20:
        break
    cont += 2"""




"""
La opción continue, puede continuar el ciclo y saltarse cuando sea verdadera. Por ejemplo:
"""
"""def ejemplo2():
    i = 1
    while i < 6:
        if i == 3:
            i += 1 
            continue
        print(i)
        i += 1 """

#ejemplo2()

#def actividad2():
#    print("actividad2")

#Escribe el código un ciclo para obtener la cantidad de dígitos de un número ingresado
#  por el usuario pero saltarse si el digito es 4.

numero = int(input("Ingrese un numero: "))  #Numero a ingresar

digitos = 0 #Acumulador de digitos

while numero > 0:           #Validar numero sea positivo y mayor a cero para iniciar el ciclo, si es igual o menor a cero, termina ciclo
    if numero % 10 == 4:    #Validamos que el numero ingresado tenga residuo 4 para no contarlo como digito
        numero //= 10       #Tenga residuo 4 o no, de todas formas dividimos el numero entre 10 para reducirle un digito y da un Entero como resultado.
        continue
    digitos += 1
    numero //= 10

print("La cantidad de digitos del numero ingresado es: ", digitos)









