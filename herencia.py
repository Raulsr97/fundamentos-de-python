# Clase padre:

class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def hacer_sonido(self):
        print(f'{self.nombre} esta haciendo un sonido generico')
    
    def info(self):
        print(f'Este es {self.nombre}, un {self.especie}')


# Clase hija: perro

class Perro(Animal):
    def __init__(self, nombre, raza):
        # Llamamos al constructor de la clase padre
        super().__init__(nombre, 'Perro')
        self.raza = raza
    
    # Sobreescribimos el metodo hacer_sonido
    def hacer_sonido(self):
        print(f'El {self.nombre} esta ladrando')

    def info(self):
        # Extendemos la funcionalidad del metodo info
        super().info()
        print(f'Es de la raza {self.raza}')


# Crear instancias de las clases hijas

mi_perro = Perro('Tommy', 'callejero XD')

# Usamos los metodos

mi_perro.hacer_sonido()
mi_perro.info()