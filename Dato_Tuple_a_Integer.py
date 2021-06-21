#Python3 code to demonstrate working of
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