x = 10
if x > 5:
    print('X es mayor')
elif x == 5:
    print('X es igual a 5')
else:
    print('X es menor')

a = 15
b = 20

if a > 10 and b > 15:
    print('a es mayor a 10 y b es mayor a 15')

if a > 10 or b > 15:
    print('a es mayor a 10 y b es mayor a 15')

if not x > 10:
    print('x no es mayor que 10')


# if anidados

is_member = True
age = 18

if is_member:
    if age >= 18:
        print('Adelante tienes acceso')
    else:
        print('Lo siento no puedes ingresar porque eres menor de edad')
else: 
    print('Lo siento no puedes ingresar porque no eres miembro')

# if is_member and age >= 18:
#     print('Adelante tienes acceso')
# else:
#     print('Lo siento no puedes ingresar')
