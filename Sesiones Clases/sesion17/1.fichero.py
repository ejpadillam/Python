
import datetime

# Definimos una función. 
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
print ('Lectura de un archivo que NO existe')
file_manipulation('noExiste.txt', 'r')
print ('-----------------------------------')