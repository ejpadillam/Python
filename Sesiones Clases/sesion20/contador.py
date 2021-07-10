'''
El programa creará un archivo llamado contador.txt que almacenará un contador de visitas
Si contador.txt no existe o está vacío lo crearemos con el número 0. Si existe simplemente 
   leeremos el valor del contador.
Si se envía el argumento inc, se incrementará el contador en uno y se mostrará por pantalla.
Si se envía el argumento dec, se decrementará el contador en uno y se mostrará por pantalla.
Si no se envía ningún argumento, se mostrará el contador.
'''
import os

def contador_vist(argum):
    fichero = open("contador.txt", "r+")
    fichero.seek(0)
    contenido=fichero.readline()
    if len(contenido) == 0:
        contenido = "0"
        fichero.write(contenido)
        print(contenido)
    else: 
        contenido = int(contenido)
        if argum != "":
            fichero.close()
            fichero=open("contador.txt", "r+")
        if argum == "":
            print("Cant Visitas", contenido)
            return
        
        if argum == "inc":
            contenido += 1
            fichero.write(str(contenido))

        if argum == "dec":
            contenido -= 1
            fichero.write(str(contenido))

    print("Cant Visitas", contenido)
    fichero.close()

seguir = True
while seguir:
    os.system("cls")
    argumento = input("Indique un argumento inc/dec: ")
    contador_vist(argumento)
    res = input("Desea continuar (S/N).? ")
    if (res != "S") and (res != "s"):
        seguir = False
print("Hasta pronto...")