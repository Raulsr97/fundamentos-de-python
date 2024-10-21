add = lambda a, b: a + b
print(add(10,4))

multiply = lambda a, b: a * b
print(multiply(10,2))

# Cuadrado de cada número

numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers))

print('Cuadrados', squared_numbers)

# Obtener numeros pares

even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print('Pares: ', even_numbers)