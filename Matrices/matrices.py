# Matriz (Array , Arreglo)
# Es una coleccion o conjunto de elementos formados
# por filas y columnas

# Matriz unidimencional (longitud 7) - vertical
for i in range(8):
    print(i)

print('\n')
# Matriz unidimencional (longitud 7) - Horizontal 
for i in range(8):
    print(i, end=" ")

print('\n')

# Matriz bidimencional (longitud 7)
# for anidado
for i in range(3):
    for j in range(7):
        print(0 +1 , end = ' ')
    print(' ')

print('\n')

# Impresion de posiciones de la matriz bidimencional (longitud 6x7)
for f in range(8):
    for c in range(8):
        print(f'({f}, {c})', end = ' ')
    print(' ')

print('\n')  


# Looping using Indexes
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range (0, 3):  # Recorre cada fila
    for j in range (0, 3): # Recorre cada elemente de esa fila (Columna)
        print(matriz[i][j], end=', ') # Imprime valor de la fila, y sus elementos internos

print('\n')

# Ejercicio: Colorcar 1 en la diagonal
for i in range(1, 8):
    for j in range(1, 8):
        if i == j:
            print(1, end = ' ')
        else:
            print(0, end = ' ')
    print(' ')

















