
# Recorrer dos matrices y comparar los datos de las listas internas - #############################################################

matriz_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matriz_2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

for tupla in zip(matriz_1, matriz_2):
    print(tupla[0][0], tupla[1][0])

###############################################################################################################################

for i in range (0, 3):  # Recorre cada fila
    for j in range (0, 3): # Recorre cada columna
        print(matriz_1[i][j], end=', ') # Imprime valor de la fila, y sus elementos internos

print(" ")

listados = ['31', '1', '3', '2', '5', '26', '3', '3', '1', '14', '2', '1', 
'21', '423', '2', '0', '0', '0', '2', '0', '0', '0', '0', '0', '0', '0', 
'3', '9']
print(max(listados))




################################################################################################################################



