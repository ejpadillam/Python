
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
fileWrite1 = 'file1.txt'
fileAppend = 'append.txt'

print ('-----------------------------------')
print ('Escritura de un archivo (WRITE) - Puntero al principio del fichero y borra el contenido')
f = file_manipulation(fileWrite, 'w')
print ('Fichero ' + f.name +' esta cerrado: ' + str(f.closed))
print ('Fichero ' + f.name +' se abrio en modo: ' + f.mode)         # Abierto en Modo Escritura -w
f.write(fecha)  # Creamos el archivo y Escribinmos la fecha y hora de su creacion dentro de el
f.close()       # Cerramos el archico
print ('Cerramos el fichero ' + f.name)
print ('Fichero ' + f.name +' esta cerrado: ' + str(f.closed))  # Archivo cerrado -True
print ('Fichero ' + f.name +' se abrio en modo: ' + f.mode)     # Fue abierto en modo Escrit -w
print ('-----------------------------------')
print ('-----------------------------------')
print()
print ('Abrimos para leer el contenido')
print ('Lectura de un archivo que SI existe')
f = file_manipulation(fileWrite1, 'r')           # Abrimos archivo en modo Lectura -r
print ('Fichero ' + f.name +' esta cerrado: ' + str(f.closed))  # Archivo abiero -NO cerrado
print ('Fichero ' + f.name +' se abrio en modo: ' + f.mode)  # Abierto en modo LEctura -r
content = f.read();     # Se lee el contenido del archivo
print ('Contenido del fichero: ' + f.name)   # Y se muestra
print (content)     # Se imprime el contenido
print()
f.close()
print ('Cerramos el fichero: ' + f.name)
print ('Fichero ' + f.name +' esta cerrado: ' + str(f.closed))
print ('Fichero ' + f.name +' se abrio en modo: ' + f.mode)
print ('-----------------------------------')