#!/usr/bin/env python
# importamos el módulo. En próximas entregas explicaremos su uso
import datetime


def file_manipulation(name, mode):
  try:
    file = open(name, mode)
    return file
  except OSError as err:
    print("Error: {0}".format(err))
  return

# Si ejecutamos el códgio varias veces, comprobaremos la diferencia entre write y append
fecha = str(datetime.datetime.now())

fileWrite = 'write.txt'
fileAppend = 'append.txt'

print ('-----------------------------------')
print ('Escritura de un archivo (APPEND) - Puntero al final del fichero y añade el contenido')
f = file_manipulation(fileAppend, 'a')
print ('Fichero ' + f.name +' esta cerrado: ' + str(f.closed))
print ('Fichero ' + f.name +' se abrio en modo: ' + f.mode)     # Abierto en modo Añadir -a
f.write(fecha + '\n')       # Añadimos la Fecha y hora 
f.close()                   # y lo cerramos
print ('Cerramos el fichero ' + f.name)
print ('Fichero ' + f.name +' esta cerrado: ' + str(f.closed))
print ('Fichero ' + f.name +' se abrio en modo: ' + f.mode)
print ('-----------------------------------')
print ('-----------------------------------')
print ('Abrimos para leer el contenido')
print ('Lectura de un archivo que SI existe')
f = file_manipulation(fileAppend, 'r')
print ('Fichero ' + f.name +' esta cerrado: ' + str(f.closed))
print ('Fichero ' + f.name +' se abrio en modo: ' + f.mode)
content = f.read();     # Leemos Todo el contenido del Archivo y loasignamos a la Var "content"
print ('Contenido del fichero: ' + f.name)
print (content)     # Imprimimos el Contenido
f.close()           # y lo cerramos

#--------------------------------------------------------------------
f = file_manipulation(fileAppend, 'a')
f.write(input("Texto: ") + '\n')       # Añadimos Texto nuevo por teclado.
f.close()                   # y lo cerramos
#--------------------------------------------------------------------

print ('Cerramos el fichero: ' + f.name)
print ('Fichero ' + f.name +' esta cerrado: ' + str(f.closed))
print ('Fichero ' + f.name +' se abrio en modo: ' + f.mode)
print ('-----------------------------------')
print ('-----------------------------------')

print ('Abrimos un fichero y lo leemos linea a linea - (archivos grandes normalmente)')
f = file_manipulation(fileAppend, 'r')
print ('Fichero ' + f.name +' esta cerrado: ' + str(f.closed))
print ('Fichero ' + f.name +' se abrio en modo: ' + f.mode)
lineF = f.readlines()
for line in lineF:
  print(line)
  
f.close()
print ('Cerramos el fichero: ' + f.name)
print ('Fichero ' + f.name +' esta cerrado: ' + str(f.closed))
print ('Fichero ' + f.name +' se abrio en modo: ' + f.mode)
print ('-----------------------------------')