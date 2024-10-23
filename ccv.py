import csv

# Leer un archivo
'''with open ('./products_updated.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)'''

# Mostrar informacion por columnas

'''with open('./products_updated.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto: {row['name']}, Precio: {row['price']}")'''


# Agregando un producto

new_product = {
    'name': 'wireless charger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accesories',
    'entry_date': '2024-10-23'
} 

# Abriendo el documento en modo apendice
with open('./products_updated.csv', mode='a', newline='') as file:
    #Creación del escritor
    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())
    #Escribir una fila en el archivo
    csv_writer.writerow(new_product)