# El tan llamado CSV (Valores Separados por Comas) es el formato más común de 
# importación y exportación de hojas de cálculo y bases de datos.

import csv
import os
os.system("cls") 
with open('fileCSV/ejemplo1.csv') as File:
    # Extraemos los dtaos del Archivo y lo asignamos al Objet "archivo_leido"
    archivo_leido = csv.reader(File, dialect='excel', delimiter=',')
    # Ahora iteramos o recorremos el Objeto e imprimimos cada fila de datos
    for fila in archivo_leido:
        print(fila)
print()

# Usando DictReader
# Crea un objeto que opera como un reader común, pero mapea la información en cada fila aun "dict"
print()
print("Imprimiendo el Archivo con DictReader")
with open('fileCSV/ejemplo1.csv') as File:
    archivo_leido = csv.DictReader(File)
    for fila in archivo_leido:
        print(fila)


# Escribiendo a un archivo CSV
'''  Primero importamos el módulo csv, y la función writer() creará un objeto apto para 
escritura. Para iterar los datos sobre las filas, necesitaremos usar la 
función writerows(). '''

myData = [["first_name", "second_name", "Grade"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']]
 
myFile = open('example2.csv', 'w')
with myFile:
    writer = csv.writer(myFile, dialect='excel')
    writer.writerows(myData)
     
print("Escritura completada. Ya puede revisar el archivo CSV...")

''' print()
print("Impresion por liena de un archico CVS")
csv_file = open('example2.csv', 'r')
print(csv_file.readline().split('\n'))
csv_file.close() '''