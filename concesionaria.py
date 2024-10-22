class Car:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.available = True

    def sale(self):
        if self.available:
            self.available == False
            print(f'El auto {self.marca} {self.año} ha sido vendido')
        else:
            print(f'El auto {self.marca} {self.año} ya no esta disponible')

class Client:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.purchased_car = []

    def buy(self, car):
        if car.available:
            car.sale()
            self.purchased_car.append(car)
            print(f'haz comprado el auto: {car.marca} {car.año}')
        else:
            print(f'el auto que seleccionaste ya no esta disponible')

class Store:
    def __init__(self):
        self.cars = []
        self.clients = []

    def add_car(self, car):
        self.cars.append(car)
        print(f'El carro {car.marca} {car.año} ha sido agregado')
    
    def register_client(self, client):
        self.clients.append(client)
        print(f'El usuario {client.name} ha sido registrado')

    def show_available_cars(self):
        print('Autos disponibles')
        for car in self.cars:
            if car.available:
                print(f'{car.marca} {car.año}')


    
# Crear autos:

car1 = Car('Audi', 'R8', '2024')
car2 = Car('volkswagen', 'Jetta', '2021')

# Crear clientes:

cliente1 = Client('Raul', '001')

# Crear tienda:

tienda = Store()

# Agregar autos a la tienda:

tienda.add_car(car1)
tienda.add_car(car2)
tienda.show_available_cars()

# Registrar cliente:

tienda.register_client(cliente1)

# Comprar un auto:

cliente1.buy(car1)

tienda.show_available_cars()

cliente1.buy(car1)