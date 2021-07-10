import json

jsonData = '{"name": "Frank", "age": 39}'
jsonToPython = json.loads(jsonData)         # Pasando un JSON a Diccionario
print(jsonToPython)

# -----------------------------------------------------------------------------------

pythonDictionary = {'name':'Bob', 'age':44, 'isEmployed':True}
dictionaryToJson = json.dumps(pythonDictionary)            # Convertir Dicciona a JSON
print(dictionaryToJson)

#----------------------------------------------------------------------------------

with open("test.json") as jsonFile:     # Abrimos el arch "test.json" con open()
    jsonObject = json.load(jsonFile)    # Cargamos el archivo a un Objeto tipo JSON
    jsonFile.close()    # Cerramos el archivo

for valor in jsonObject:     
    print(jsonObject[valor])    # Imprimims los "valores" de cada "Llave"
print()

product = jsonObject['product']  # craeamos variablespara guardar las diferentes valores decada llave
hd = jsonObject['hd']   
ram = jsonObject['ram']
cant = jsonObject['cant']
desc = jsonObject['desc']

print(product)      # Impimimos los valores
print(hd)
print(ram)
print(cant)
print(desc)

#---------------------------------------------------------------------------
#     ****     MINIFICACION DE ARCHIVOS JSOSN    *****
#--------------------------------------------------------------------------
''' EJEMPLO JSON MINIFICADO
En muchas ocasiones se trabaja con archivos JSON donde todos los espacios y saltos de línea
 han sido eliminados buscando ocupar el mínimo espacio posible. 
 Esta técnica se llama “minificado”. Minificar es conseguir que un fichero sea menos pesado
 modificando ciertos elementos: espacios innecesarios, saltos de línea, tabulaciones, 
 comentarios, etc ... Al minificar el fichero se vuelve confuso a la hora de ser leído o
 interpretado por humanos, pero los computadores leen la información de forma más rápida
 y los archivos ocupan menos espacio. '''

#Ejemplo (todo este texto es una sola línea sin espacios):

{"marcadores":[{"latitude":40.416875,"longitude":-3.703308,"city":"Madrid","description":"PuertadelSol"},{"latitude":40.417438,"longitude":-3.693363,"city":"Madrid","description":"PaseodelPrado"},{"latitude":40.407015,"longitude":-3.691163,"city":"Madrid","description":"EstacióndeAtocha"}]}
