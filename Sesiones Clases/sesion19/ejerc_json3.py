import json

# Leer un archivo JSON cuya estructura tiene un Objeto "Clients" y anidados varios JSON's
# con sus pares Clave - Valor (* No olvides validarlo *)

with open('data.json') as file:
    data = json.load(file)
    for client in data['clients']:
        print('First name:', client['First name'])
        print('Last name:', client['Last name'])
        print('Age:', client['Age'])
        print('Amount:', client['Amount'])
        print('')