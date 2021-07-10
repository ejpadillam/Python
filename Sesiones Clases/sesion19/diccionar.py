''' Un Diccionario es una estructura de datos y un tipo de dato en Python con características 
especiales que nos permite almacenar cualquier tipo de valor como enteros, cadenas, listas 
e incluso otras funciones. Estos diccionarios nos permiten además identificar cada elemento
 por una clave (Key).

Para definir un diccionario, se encierra el listado de valores entre llaves. 
Las parejas de clave y valor se separan con comas, y la clave y el valor se separan 
con dos puntos. '''

diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript'] }

#Podemos acceder al elemento de un Diccionario mediante la clave de este elemento, 
# como veremos a continuación:

print(diccionario['nombre']) #Carlos
print (diccionario['edad']) #22
print (diccionario['cursos'])  #['Python','Django','JavaScript']

#También es posible insertar una lista dentro de un diccionario. 
# Para acceder a cada uno de los cursos usamos los índices:

print (diccionario['cursos'][0])  #Python
print (diccionario['cursos'][1])  #Django
print (diccionario['cursos'][2])  #JavaScript

# Para recorrer todo el Diccionario, podemos hacer uso de la estructura for:

for key in diccionario:
  print (key, ":", diccionario[key])
  print(diccionario.get(key))

#     --------------  METODOS MANEJO DICCIONARIOS ---------------------

#keys() Retorna una lista de elementos, los cuales serán las claves de nuestro diccionario.
llaves = diccionario.keys()
print(llaves)

#values() -Retorna una lista de elementos, que serán los valores de nuestro diccionario.

vals = diccionario.values()
print(vals)

#get() Recibe como parámetro una clave, devuelve el valor de la clave. Si no lo encuentra,
#  devuelve un objeto none.

valor_key = diccionario.get("nombre")
print(valor_key)

#pop() - Recibe como parámetro una clave, elimina esta y devuelve su valor. 
# Si no lo encuentra, devuelve error.
valor=diccionario.pop("nombre")
print(valor)
print(diccionario)

#setdefault() - Funciona de dos formas. En la primera como get()
key = diccionario.setdefault("cursos")
print(key)
# Agrega un nuevo par -llave/valor
nvo = diccionario.setdefault("horas", 160)
print(nvo)
print(diccionario)

#update() -Recibe como parámetro otro diccionario. Si se tienen claves iguales, 
# actualiza el valor de la clave repetida; si no hay claves iguales, este par clave-valor 
# es agregado al diccionario.

dic1 = {"a" : 1, "b" : 2, "c" : 3 , "d" : 4}
dic2 = {"c" : 6, "b" : 5, "e" : 9 , "f" : 10}
dic1.update(dic2)
print(dic1)