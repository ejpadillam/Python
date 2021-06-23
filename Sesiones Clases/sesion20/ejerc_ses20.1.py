""" Python también cuenta con librerías adicionales para el manejo de archivos. 
Entre ellos se incluyen la librería pandas e incluso la librería csv exclusiva 
para archivos separados por comas. Vamos a ver ejemplos usando estas librerías.

En este caso vamos a leer la información de un archivo matrizAsignacion.csv e imprimirlo. """

import csv

def testCSV():
    archivo =  open('sesion20/matrizAsignacion.csv', mode='r', encoding='utf-8-sig' ) 
    lector = csv.reader(archivo) #Retorna un objeto con las filas del csv
    
    for fila in lector: #Este va a recorrer cada Fila
        print(fila)
        for i in fila:  #Este recorre cada Valor en cada Fila [i] representa cada elemento separado por ,
            print(i, end=" " )
        print("\n")

testCSV()
