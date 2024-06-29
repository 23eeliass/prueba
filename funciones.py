import random
import math


def agregar_productos():
    print("ingrese los datos del producto: ")
    nombre = input("Nombre: ")
    categoria = input("categoria: ")
    cantidad = input("cantidad: ")
    
    precio = random.randint(10,1000)

    productos[precio] ={
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad

}

print(f"Producto agregado a la lista con precio:{precio}")


def Calcular_precio_promedio_de_productos():
    if productos:
        lista_productos = [int(producto["precio"]) for producto in productos.values()]

        suma_productos = math.fsum (lista_productos)

        print(f"el precio promedio registrado es: {suma_productos}")

    else:
        print("No hay productos registrados aun.")






def main():
    while True:
        print("\n---Sistema---")
        print("1.- registrar producto")
        print("2.- Listar todos los productos")
        print("3.- Buscar productos por categoria")
        print("4.- Calcular precio promedio de los productos")
        print("5.- Salir del programa")

        opcion= input("Selecciones una opcion(1-5)")

        if opcion == '1':
            registrar_producto()
        
        elif opcion == '2':
            print("Listado de productos: ")
            for precio,producto in productos.items():
                print(f"Nombre: {producto[nombre]}")
                print(f"Categoria: {producto[categoria]}")
                print(f"Cantidad: {producto[cantidad]}")
                print(f"Precio: {producto[precio]}")
        
    
        elif opcion == '3': 
            categoria = input("ingrese la categoria del producto: ")
            encontrados = []
            for producto in productos.values():
                if producto['Categoria'].lower()== categoria.lower():
                    encontrados.append(producto)
            
            if encontrados:
                print(f"productos encontrados en la categoria '{categoria}': ")
                for productos in encontrados:
                    print(f"Nombre: {producto[nombre]}")

            else: 
                print(f"No se encontraron productos en la categoria '{categoria}'. ")

        elif opcion == '4':
                    Calcular_precio_promedio_de_productos()


        elif opcion== '5'
            print("Saliendo del programa.")
            break

        else:
            print("Opcion no valida, intente denuevo")

if_name_ == "_main_":
    main()


    


