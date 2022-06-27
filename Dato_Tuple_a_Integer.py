"""#Python3 code to demonstrate working of
# Convert Tuple to integer
# Using reduce() + lambda
import functools

# initialize tuple
test_tuple = (1, 4, 5)

# printing original tuple 
print("The original tuple : " + str(test_tuple))

# Convert Tuple to integer
# Using reduce() + lambda
res = functools.reduce(lambda sub, ele: sub * 10 + ele, test_tuple)

# printing result
print("Tuple to integer conversion : " + str(res))
print(type(res))

print('\n')

##################################################################################################


# Python3 code to demonstrate working of
# Convert Tuple to integer
# Using int() + join() + map()

# initialize tuple
test_tuple = (1, 4, 5)
print("Tipo de dato actual: ", type(test_tuple))

# printing original tuple 
print("The original tuple : " + str(test_tuple))

# Convert Tuple to integer
# Using int() + join() + map()
res = int(''.join(map(str, test_tuple)))

# printing result
print("Tuple to integer conversion : " + str(res))
print("Tipo de dato resultante: ", type(res))

print(" ")


arreglo = [3,6,8,1,2,0,7,2,9]
i = 0
impar = 0
while (i < len(arreglo)) and (arreglo[i] != 0):
    if (arreglo[i] % 2) == 1:
        impar += 1
    i += 1

print(i)
print(impar)


print(" ")

x = 5
y = 3
z = 2
a = 6
b = 4
c = 1


x = x + y   #beta
a = x + b   #épsilon
y = y * a   #gama
b = b / c   #delta
y = y - z   #alfa


print(a)
"
print(" ")




x = 3
y = 9
z = 5

if y % x == 0:
    if y >= z:
        x *= x
    else:
        z *= z
else:
    if z >= x:
        if y >= z:
            y *= y
    else:
        z *= z

if y % x == 0:
    x += 3
else:
    y *= 2

print("Linea x =", x)
print("Linea y =", y)
print("Linea z =", z)


prologo = 1
secuela = 3
epilogo = 5
epilogo = secuela
secuela = prologo * epilogo
prologo = epilogo
epilogo = secuela
prologo = secuela + epilogo
epilogo = prologo / secuela
secuela = prologo

print(secuela)

r = 5
h = 9
area = 2*3.14*r**2 + 2*3.14*r*h

print(area)


"""
def fun (x):
    if x % 2 == 0:
        return 1
    else:
        return 2

print(fun(fun(2)))







