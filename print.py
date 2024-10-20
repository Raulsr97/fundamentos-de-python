# 1 Uso practico del print, imprimir un string
print('Hola Mundo')

# 2 Uso de la coma en print: al usar una coma se añade un espacio automaticamente entre cada valor
print('hola', 'mundo', 'mundial')

# 3 concatenar cadenas con el signo + unira los valores sin ningun espacio
print('hola' + 'mundo')

# 4 Uso de sep: permite especificar como separar los elementos al imprimir
print('nunca', 'pares', 'de', 'aprender', sep=' *')

# 5 Uso de end: cambia lo que se imprime al final de la llamada a print
print('nunca', end=' ')
print('pares de aprender')

# 6 Impresion de variables.
frase = 'Nunca pares de aprender'
autor = 'platzi'

print('frase:', frase, 'autor:', autor)

# 7 Uso de formato con f-strings: permiten instertar expresiones dentro de cadenas de texto
print(f'FRASE: {frase}, AUTOR: {autor}')

# 8 Impresion con formato especifico: puedes controlar el formato de los numeros al imprimir
valor = 3.14159
print('Valor: {:.2f}'.format(valor))

# 9 Saltos de linea y caracteres especiales
print('hola\nmundo')

print('hola soy \'Raul\'')

