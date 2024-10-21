# Ejemplo de iterador:

# #Crear una lista
# my_list = [1, 2, 3, 4]

# #Obtener el iterador de la lista
# my_iter = iter(my_list)

# #Usar el iterador
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))


# ITERAR USANDO UN BUCLE WHILE:

mi_lista = [5, 10, 15, 20]

mi_iterador = iter(mi_lista)

while True:
    try:
        elemento = next(mi_iterador)
        print(elemento)
    except StopIteration:
        break
     