""" Como vemos, esta librería nos permite recorrer el archivo y los valores en un csv sin
necesidad de separar los valores. CSV también cuenta con una opción para escribir 
un archivo. Vamos ahora a leer el archivo y escribirlo en otro archivo adicionando 
una columna al final con el valor "Nuevo". """
import csv

def testIOcsv():
    archivo =  open('sesion20/matrizAsignacion.csv', mode='r', encoding='utf-8-sig' ) 
    nuevoArchivo = open('sesion20/archivoResultado.csv', mode='w', encoding='utf-8-sig', newline="" )
    
    lector = csv.reader(archivo) #Retorna un objeto con las filas del csv para ser leidas
     
    escritor = csv.writer(nuevoArchivo) #Retorna un objeto para escribir en csv
    
    for fila in lector: #Este va a recorrer cada fila del lector (Trabaja como una lista)
        fila.append("Nuevo")        # Agrega nva posic a la Lista con valor "Nuevo"
        escritor.writerow(fila) # Este escribe cada fila en el archivo destino "archoResultado.csv"

testIOcsv()
