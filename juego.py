# Juego piedra, papel o tijera
# Reglas del juego:
# -Piedra gana a tijera
# -Tijera gana papel
# -Papel gana a piedra

# import random

# opciones = ['piedra', 'papel', 'tijera']

# while True:
#     # El jugador elige una opcion
#     jugador = input('Elige: piedra, papel o tijera: ').lower()

#     # Validar la opcion del jugador
#     if jugador not in opciones:
#         print('Opcion no valida, inténtalo de nuevo')
#         continue
    
#     # La computadora elige una opción aleatoria
#     computadora = random.choice(opciones)

#     print(f'La computadora eligio: {computadora}')

#     # Condiciones para validar al ganador
#     if jugador == computadora:
#         print('Es un empate!')
#     elif (jugador == 'piedra' and computadora == 'tijera') or \
#          (jugador == 'tijera' and computadora == 'papel') or \
#          (jugador == 'papel' and computadora == 'piedra'):
#         print('Ganaste!')
#     else:
#         print('Perdiste :(')

#     jugar_de_nuevo = input('¿Quieres jugar de nuevo? (si/no): ').lower()

#     if jugar_de_nuevo != 'si':
#         break


import random

options = ['piedra', 'papel', 'tijera']

while True:
    player = input('Elige piedra, papel o tijera: ').lower()

    if player not in options:
        print('Elige una opcion valida')
        continue


    computer = random.choice(options)

    print(f'la computadora eligio: {computer}')

    if player == computer:
        print('empate!')
    elif (player == 'piedra' and computer == 'tijera') or \
         (player == 'tijera' and computer == 'papel') or \
         (player == 'papel' and computer == 'piedra'):
         print('Ganaste')
    else:
        print('perdiste')

    jugar_de_nuevo = input('Quieres jugar de nuevo? (si/no): ')

    if jugar_de_nuevo != 'si':
        break

              