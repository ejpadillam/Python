# JSON, acrónimo de JavaScript Object Notation, es un formato de texto ligero
# para el intercambio de datos.
# En Python el formato JSON se puede procesar gracias al paquete json. 
# Este paquete contiene el código que permite transformar los archivos JSON 
# en diccionarios o viceversa.

import json
from typing import Dict

# Estructura JSON contenida en el codigo fuente y pasarla a un archivo .JSON

json_data = {
    "product": "Python book",
    "overall": 4.0,
    "text": "Nice book"
}

with open('writed_json.json', 'w') as jsonFile:
    json.dump(json_data, jsonFile)      # Convertir de python (Dicc) a JSON
    jsonFile.close()