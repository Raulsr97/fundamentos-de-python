# Definición: Se crean usando funciones con yield en lugar de return.
# Pausas y reanuda: Cada vez que el generador encuentra un yield, se pausa y devuelve el valor. Cuando se llama de nuevo, retoma justo después de ese yield.
# Iteración eficiente: Los generadores son útiles cuando necesitas generar una secuencia de valores grandes o infinitos sin cargar todo en la memoria.

def contador():
    n = 1
    while n <= 3:
        yield n
        n += 1
    
generador = contador()

print(next(generador)) # Imprime 1
print(next(generador)) # Imprime 2
print(next(generador)) # Imprime 3

# Ahorro de memoria: No es necesario almacenar la secuencia completa en memoria.
# Procesamiento perezoso: Solo se calcula el siguiente valor cuando es necesario.

# EJERCICIO 1: GENERADOR QUE DEVUELVA LOS PRIMEROS 10 NUMEROS PARES

def pares():
    n = 0
    while n < 20:
        yield n 
        n += 2

for num in pares():
    print(num)
    