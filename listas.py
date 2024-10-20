to_do = [
    'Dirigirnos al hotel',
    'Ir a almozar',
    'Visitar un museo',
    'Volver al hotel'
]
print(to_do)

numeros = [1, 3, 4, 'cinco']
print(numeros)
print(type(numeros))

mix = ['uno', 2, 3.14, True, [1, 2, 3]]
print(mix)
print(len(mix))
print('primer elemento:', mix[0])
print('ultimo elemento: ', mix[-1])
print(mix[1:3])
print(mix[:2])
print(mix[2:])

string = 'hola mundo'
print('primer elemento:', string[0])
print('ultimo elemento: ', string[-1])

# Metodos

# añadir un nuevo elemento 
mix.append(False)
print(mix)

mix.append(['a', 'b'])
print(mix)

# Añadir un nuevo elemento en un lugar especifico
mix.insert(1, ['c', 'd']) 
print(mix)

# Buscar la posicion de un elemento (si hay varios elementos con el mismo valor devuelve la primer posicion encontrada)
print(mix.index(True))

# Consultar el elemento mayor y menor de una lista

numeros_1 = [1, 2, 3, 4, 5]
print('Mayor:', max(numeros_1))
print('Menor:', min(numeros_1))

# Eliminar elementos de una lista o la lista completa

del numeros_1[-1]
print(numeros_1)

del numeros_1[:1]
print(numeros_1)

del numeros_1
print(numeros_1)