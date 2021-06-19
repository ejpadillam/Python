# Matriz (Array , Arreglo)
# Es una coleccion o conjunto de elementos formados
# por filas y columnas

# Matriz unidimencional (longitud 6) - vertical
for i in range(7):
    print(i)

print('\n')
# Matriz unidimencional (longitud 6) - Horizontal 
for i in range(7):
    print(i, end=" ")

print('\n')

# Matriz bidimencional (longitud 6x6)
# for anidado
for i in range(1, 7):
    for j in range(1, 7):
        print(0, end = ' ')
    print(' ')

print('\n')

# Impresion de posiciones de la matriz bidimencional (longitud 6x6)
for i in range(1, 7):
    for j in range(1, 7):
        print(f'({i}, {j})', end = ' ')
    print(' ')

print('\n')  

# Ejercicio: Colorcar 1 en la diagonal
for i in range(1, 7):
    for j in range(1, 7):
        if i == j:
            print(1, end = ' ')
        else:
            print(0, end = ' ')
    print(' ')

















