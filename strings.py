# Creando una cadena
cadena = 'Hola mundo'
print(cadena)

# Concatenando una cadena
cadena1 = 'Hola'
cadena2 = 'mundo'

print(cadena1 + ' ' + cadena2)

# Multiplicacion de cadenas
cadena3 = 'Hola' * 3
print(cadena3)

# Acceder a caracteres

cadena4 = 'fdsrwe'
print(cadena4[2])

# slicing: permite obtener subcadenas, sintaxis [inicio:fin], inicio es inclusivo y el final es exclusivo

cadena5 = 'python'
print(cadena5[0:3])

# Metodos utiles para manipular cadenas

# upper(): convierte la cadena a mayusculas

cadena6 = 'hola'
print(cadena6.upper())

# lower(): convierte la cadena a minusculas

cadena7 = 'HOLA'
print(cadena7.lower())

# replace(): remplaza partes de la cadena por otra

cadena8 = 'hola javascript'.replace('javascript', 'python')
print(cadena8)

# split(): divide la cadena en una lista de palabras

cadena9 = 'hello world'.split()
print(cadena9)

# join(): Une los elementos de una lista en una cadena usando un separador

''.join(['hola', 'espacio'])



# Buscar en cadenas

# find(): Devuelve el indice de la primera aparicion de una subcadena, si no la acepta devuelve -1

cadena10 = 'hello mundo'

print(cadena10.find('mundo'))
print(cadena10.find('hola'))

# in: verifica si una subcadena esta adentro de la otra

print('mundo' in cadena10)
print('hola' in cadena10)


#Eliminar espacios
# strip(): Elimina espacios en blanco al inicio y al final

cadena11 = '  hola agua   '
print(cadena11.strip())
