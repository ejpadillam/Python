with open('persona.txt', 'r') as dict_file:
    dict_text = dict_file.read()
    dict_from_file = eval(dict_text)  # Evalua la cedena de Caracteres del Archivo para ser leida en Python

print(dict_from_file)

file = open('personas.txt', 'r')
peoples = {}            # Se crea un Diccionario vacio
for line in file:       # Se recorren las lineas del Archivo
    #print("Valor de Line", line)
    personas = line.rstrip().split(';')
    pers = {"id": (personas[0]), 
            "nombre": (personas[1]), 
            "apellido": (personas[2]), 
            "nacim": (personas[3]) }
    peoples = pers
    print("personas: ", peoples)
