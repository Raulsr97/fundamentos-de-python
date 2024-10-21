# numbers = [1, 2, 3, 4, 5, 6]

# for i in numbers:
#     print('Aqui i es igual a: ', i)

# for i in range(3, 10):
#     print(i)

# fruits = ['manzana', 'pera', 'uva', 'naranja', 'tomate']

# for fruit in fruits:
#     print(fruit)
#     if fruit == 'naranja':
#         print('naranja encontrada')


# Programa para escribir numeros del uno al 10

# for i in range(1, 11):
#     print(i)

# Suma los numeros del 1 al 100

# total = 0

# for i  in range(1, 101):
#     total += 1
#     print(total)

# Contar vocales en una palabra: pide al usuario una palabra y usa un bucle for para saber cuantas vocales tiene.

# palabra_usuario = input('Agrega una palabra, te dire cuantas vocales tiene: ').lower()

# vocales = ['a', 'e', 'i', 'o', 'u']

# contador = 0

# for letra in palabra_usuario:
#     if letra in vocales:
#         contador += 1
# print(f'Tu palabra tiene {contador} vocales!')


# Tablas de multiplicar: escribe un programa que escriba las tablas de mutiplicar del 1 al 10.

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} X {j} = {i*j}')
# print('')

# Numeros primos del 1 al 100: 

# for num in range(2, 101): # Recorre los numeros del 2 al 100
#     es_primo = True # Supone que el numero es primo
#     for i in range(2, num): # Verifica si el numero es divisible por algun numero entre 2 y num-1
#         if num % i == 0: # Si numero es divisible entre i no es primo
#             es_primo = False
#         break # Termina el bucle si se encuentra un numero divisor
#     if es_primo: # Si es primo sigue siendo true e imprime el numero
#         print(num)


# Factorial de un numero: Pide al usuario un numero y calcula su factorial utilizando un ciclo while

# numero = int(input('Ingresa un número: '))

# factorial = 1

# while numero > 1:
#     factorial *= numero
#     numero -= 1
# print(f'El factorial es: {factorial}')


# INVERTIR UN CADENA: escribe un programa que invierta una cadena sin usar slicing.

# cadena = input('Escribe una palabra: ')
# invertida = ''

# for letra in cadena:
#     invertida = letra + invertida
# print(f'Palabra invertida: {invertida}')


# PIRAMIDE DE NUMEROS:

for i in range(1, 6):
    print(str(i) * i)

# IMPRIMIR LOS ELEMENTOS UNICOS DE UNA LISTA:

numeros = [1, 2, 2, 3, 4, 4, 5]

unicos = []

for numero in numeros:
    if numeros.count(numero) == 1:
        unicos.append(numero)
print(unicos)