"""# Matriz (Array , Arreglo)
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


    MatrizComp = [
    [0, 1, 2, 3, 4, 5, 6], 
    [1, 2, 3, 4, 5]

] # Matriz de comparacion

print(MatrizComp)
print(" ")
print(MatrizComp[0])
print(MatrizComp[1])
print(MatrizComp[0][6])
print(MatrizComp[1][2])

MatrizComp[1][2].replace("Texto ingresado")
print(MatrizComp[1])

"""

############# Reemplazar, actualizar o cambiar los datos de las filas en una Matriz - Array - Arreglo

b = [           # Matriz b
    [22,56,33], # Indice: Fila: 0, Columnas: 0, 1, 2
    [21,58,33], # Indice: Fila: 1, Columnas: 0, 1, 2
    [20,51,39]  # Indice: Fila: 2, Columnas: 0, 1, 2
]

for i in range(0, 3):      # Recorre las filas 0, 1, 2
    for j in range(0, 3):  # Recorre de cada fila, las columnas 0, 1, 2
        valor = b[i][j]
        if valor <= 50:
            b[i][j] = 0
        else:
            b[i][j] = 1

print(b)         #  Se imprime la matriz actualizada.















