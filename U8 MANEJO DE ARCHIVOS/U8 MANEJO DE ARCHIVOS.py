#ACOSTA CRISTINA - TUP1 COM2 - U8
#ACTIVIDAD 1
with open("productos.txt","w+") as productos:
    productos.write("nombre,precio,cantidad\n")
    productos.write("lapicera,120,30\n")
    productos.write("corrector,150,15\n")
    productos.write("goma,105,10\n")
#ACTIVIDAD 2    
with open("productos.txt","r+") as productos:
    contenido=productos.read()
    print(contenido)

with open("productos.txt","r") as lineas:
    for linea in lineas:
        producto=linea.strip().split(",")
        print (producto)
#ACTIVIDAD 3
salir=False
while salir==False:
        opcion:int=int(input("INGRESE: \n\t1- AGREGAR NUEVO PRODUCTO\n\t2- NO AGREGAR NUEVO PRODUCTO\n\t"))
        match opcion:
            case 1: 
                    with open("productos.txt","a") as productos:
                        productos.write(input("Ingrese producto:\n")+",")
                        productos.write(input("Ingrese precio:\n")+",")
                        productos.write(input("Ingrese cantidad:\n"))
                    with open("productos.txt","r")as productos:
                        contenido=productos.read()
                        print(contenido)
            case 2:
                salir=True
            case _:
                print("Opción incorrecta")
print("fin")
#ACTIVIDAD 5
productos=[]
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad":cantidad
        })
print("Productos cargados correctamente:")
for producto in productos:
    print(producto)
#ACTIVIDAD 5
nombre = input("Ingrese el nombre del producto que desea buscar: ")

for producto in productos:
    if producto["nombre"].lower() == nombre.lower():
        print(f"Producto encontrado: {producto}")
#ACTIVIDAD 6

with open("productos.txt", "w") as archivo:
    for producto in productos:
        linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        archivo.write(linea)
print(productos)