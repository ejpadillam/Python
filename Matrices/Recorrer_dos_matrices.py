
# Recorrer dos matrices y comparar los datos de las listas internas

matriz_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matriz_2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

for tupla in zip(matriz_1, matriz_2):
    print(tupla[0][0], tupla[1][0])








"""for i in range (0, 3):  # Recorre cada fila
    for j in range (0, 3): # Recorre cada elemente de esa fila (Columna)
        print(matriz[i][j], end=', ') # Imprime valor de la fila, y sus elementos internos"""