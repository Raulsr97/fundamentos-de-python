numeros = {1:'uno', 2:'dos', 3:'tres'}
print(numeros)
print(numeros[2])

informacion = {'nombre': 'Raul',
               'apellido': 'Salinas',
               'altura': 1.65,
               'edad': 26}

print(informacion)
del informacion['edad']
print(informacion)

# Metodos de los diccionarios

claves = informacion.keys()
print(claves)
print(type(claves))


values = informacion.values()
print(values)
print(type(values))

pares = informacion.items()
print(pares)
print(type(pares))


# Ejercicio

contactos = {'Raul': {'apellido': 'Salinas',
                      'altura': 1.65,
                      'edad': 26},
             'Andrea': {'apellido': 'Miguel',
                        'altura': 1.50,
                        'edad': 24}
            } 
print(contactos['Raul'])