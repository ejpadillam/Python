#Escribir un programa que guarde en una variable el diccionario 
# {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y
#  muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("Introduce una divisa: ")
print(divisa.title())
if divisa.title() in monedas:
    print(monedas[divisa.title()])
else:
    print("La divisa no está.")


#-----------------------------------------------------
#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio
#  de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar 
# un mensaje informando de ello.

''' Fruta	Precio
    Plátano	3500
    Manzana	6000
    Pera	5500
    Naranja	4800 '''

frutas = {'Plátano': 3500,
          'Manzana': 6000, 
          'Pera': 5500, 
          'Naranja': 4800}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '$')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")

#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información 
# sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
#  que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el 
# contenido del diccionario.
persona = {}
continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    seguir = input('¿Quieres añadir más información (S/N)? ')
    if seguir == "S" or seguir=="s":
        continuar=True
    else:
        continuar=False
        print("Hasta pronto..")