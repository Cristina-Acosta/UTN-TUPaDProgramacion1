print("ACOSTA CRISTINA - CASO 1 BIBLIOTECA - PROGRAMACIÓN UTN - COM2")


#Se pide desarrollar un programa con una interfaz basada en menú que utilice listas paralelas (una para títulos[] y otra para ejemplares[]). Cada título debe estar vinculado a su número correspondiente de copias utilizando el mismo índice en ambas listas. Se debe utilizar un bucle while para navegar por las opciones del menú hasta que el usuario elija salir.Ejemplo:títulos[] = ["El Señor de los Anillos", "Orgullo y Prejuicio", "Matar un Ruiseñor"] ejemplares[] = [5, 3, 7]
# En este ejemplo, "El Señor de los Anillos" tiene 5 copias, "Orgullo y Prejuicio" tiene 3 copias, y "Matar un Ruiseñor" tiene 7 copias.
# Opciones del Menú:
print("\n----------     MENÚ DE LA BIBLIOTECA    ----------\n")
print("----------   INGRESE LA OPCIÓN QUE DESEA   ----------\n")
var_ent_opcion:int=int(input("[ 1 ]	Ingresar lista de títulos\n[ 2 ]	Ingresar lista de ejemplares disponibles (por título)\n[ 3 ]	Mostrar catálogo con stock:\n[ 4 ]	Consultar disponibilidad de un título específico:\n[ 5 ]   Listar agotados (0 ejemplares)\n[ 6 ]	Agregar título\n[ 7 ]	Actualizar ejemplares (préstamo/devolución)\n[ 8 ]	Ver catálogo\n[ 9 ]   Salir\n"))
while var_ent_opcion<1 and var_ent_opcion>9:
    var_ent_opcion=3
lista_str_titulos=[]
lista_ent_ejemplares=[]
while var_ent_opcion!=9:
# 1.	Ingresar lista de títulos:
# Permite al usuario introducir los títulos de los libros en la biblioteca.
# Ejemplo: El usuario introduce "1984", "Rebelión en la Granja".
    if var_ent_opcion==1:
        var_ent_cantidad:int=int(input("¿Cuántos títulos deseas ingresar?  "))
        for i in range(var_ent_cantidad):
            var_str_nuevo=input(f"INGRESE TITULO {i+1}: ")
            lista_str_titulos.append(var_str_nuevo.capitalize())
            print(f"Nuevo título: {var_str_nuevo}")
        print("----------   INGRESE OTRA OPCIÓN   ----------\n")
        var_ent_opcion:int=int(input("[ 1 ]	Ingresar otra lista de títulos\n[ 2 ]	Ingresar lista de ejemplares disponibles (por título)\n[ 3 ]	Mostrar catálogo con stock:\n[ 4 ]	Consultar disponibilidad de un título específico:\n[ 5 ]   Listar agotados (0 ejemplares)\n[ 6 ]	Agregar título\n[ 7 ]	Actualizar ejemplares (préstamo/devolución)\n[ 8 ]	Ver catálogo\n[ 9 ]   Salir\n"))
        while var_ent_opcion<1 and var_ent_opcion>9:
            var_ent_opcion=3
# 2.	Ingresar lista de ejemplares disponibles (por título):
# Permite al usuario introducir el número de copias disponibles para cada título de libro.
# Ejemplo: Si el título es "1984", el usuario podría introducir "4" (lo que significa que hay 4 copias).
    elif var_ent_opcion==2:
        for i in lista_str_titulos:
            var_ent_ejemplar:int=int(input(f"INGRESE EJEMPLARES DISPONIBLES DE {i}: "))
            lista_ent_ejemplares.append(var_ent_ejemplar)
            print(f"{i} : {var_ent_ejemplar} copias")
        print("----------   INGRESE OTRA OPCIÓN   ----------\n")
        var_ent_opcion:int=int(input("[ 1 ]	Ingresar lista de títulos\n[ 2 ]	Ingresar lista de ejemplares disponibles (por título)\n[ 3 ]	Mostrar catálogo con stock:\n[ 4 ]	Consultar disponibilidad de un título específico:\n[ 5 ]   Listar agotados (0 ejemplares)\n[ 6 ]	Agregar título\n[ 7 ]	Actualizar ejemplares (préstamo/devolución)\n[ 8 ]	Ver catálogo\n[ 9 ]   Salir\n"))
        while var_ent_opcion<1 and var_ent_opcion>9:
            var_ent_opcion=3
# 3.	Mostrar catálogo con stock
# Muestra una lista de todos los títulos y el número de copias disponibles para cada uno.
    elif var_ent_opcion==3:
        for i in range(len(lista_str_titulos)):
            print(f"{lista_str_titulos[i]} : {lista_ent_ejemplares[i]} copias\n")
        print("----------   INGRESE OTRA OPCIÓN   ----------\n")
        var_ent_opcion:int=int(input("[ 1 ]	Ingresar lista de títulos\n[ 2 ]	Ingresar lista de ejemplares disponibles (por título)\n[ 3 ]	Mostrar catálogo con stock:\n[ 4 ]	Consultar disponibilidad de un título específico:\n[ 5 ]   Listar agotados (0 ejemplares)\n[ 6 ]	Agregar título\n[ 7 ]	Actualizar ejemplares (préstamo/devolución)\n[ 8 ]	Ver catálogo\n[ 9 ]   Salir\n"))
        while var_ent_opcion<1 and var_ent_opcion>9:
            var_ent_opcion=3

# 4.	Consultar disponibilidad de un título específico:
# Permite al usuario introducir un título y ver cuántas copias están disponibles.
# Ejemplo: El usuario introduce "Orgullo y Prejuicio", y el programa muestra "3 copias disponibles".
    elif var_ent_opcion==4:
        var_str_consulta:str=input("INGRESA TÍTULO QUE DESEAS CONSULTAR: ")
        for i in range(len(lista_str_titulos)):
            if lista_str_titulos[i]==var_str_consulta.capitalize():
                print(f"{lista_str_titulos[i]} : {lista_ent_ejemplares[i]} copias")
        print("----------   INGRESE OTRA OPCIÓN   ----------\n")
        var_ent_opcion:int=int(input("[ 1 ]	Ingresar lista de títulos\n[ 2 ]	Ingresar lista de ejemplares disponibles (por título)\n[ 3 ]	Mostrar catálogo con stock:\n[ 4 ]	Consultar disponibilidad de un título específico:\n[ 5 ]   Listar agotados (0 ejemplares)\n[ 6 ]	Agregar título\n[ 7 ]	Actualizar ejemplares (préstamo/devolución)\n[ 8 ]	Ver catálogo\n[ 9 ]   Salir\n"))
        while var_ent_opcion<1 and var_ent_opcion>9:
            var_ent_opcion=3

# 5.	Listar agotados (0 ejemplares):
# Muestra una lista de todos los títulos que tienen 0 copias disponibles.
    elif var_ent_opcion==5:
        for i in range(len(lista_ent_ejemplares)):
            if lista_ent_ejemplares[i]==0:
                print(f"{lista_str_titulos[i]} : {lista_ent_ejemplares[i]} copias")
            else:
                print("HAY STOCK DE TODOS")
        print("----------   INGRESE OTRA OPCIÓN   ----------\n")
        var_ent_opcion:int=int(input("[ 1 ]	Ingresar lista de títulos\n[ 2 ]	Ingresar lista de ejemplares disponibles (por título)\n[ 3 ]	Mostrar catálogo con stock:\n[ 4 ]	Consultar disponibilidad de un título específico:\n[ 5 ]   Listar agotados (0 ejemplares)\n[ 6 ]	Agregar título\n[ 7 ]	Actualizar ejemplares (préstamo/devolución)\n[ 8 ]	Ver catálogo\n[ 9 ]   Salir\n"))
        while var_ent_opcion<1 and var_ent_opcion>9:
            var_ent_opcion=3

# 6.	Agregar título:
# Permite al usuario añadir un nuevo título al catálogo y especificar el número inicial de copias.
    elif var_ent_opcion==6:
        var_str_nuevo=input("INGRESE TITULO NUEVO: ")
        lista_str_titulos.append(var_str_nuevo.capitalize())
        var_ent_nuevo=int(input("INGRESE CANTIDAD DE COPIAS: "))
        lista_ent_ejemplares.append(var_ent_nuevo)
        print(f"Nuevo título: {var_str_nuevo} : {var_ent_nuevo} copias")
        print("----------   INGRESE OTRA OPCIÓN   ----------\n")
        var_ent_opcion:int=int(input("[ 1 ]	Ingresar otra lista de títulos\n[ 2 ]	Ingresar lista de ejemplares disponibles (por título)\n[ 3 ]	Mostrar catálogo con stock:\n[ 4 ]	Consultar disponibilidad de un título específico:\n[ 5 ]   Listar agotados (0 ejemplares)\n[ 6 ]	Agregar título\n[ 7 ]	Actualizar ejemplares (préstamo/devolución)\n[ 8 ]	Ver catálogo\n[ 9 ]   Salir\n"))
        while var_ent_opcion<1 and var_ent_opcion>9:
            var_ent_opcion=3

# 7.	Actualizar ejemplares (préstamo/devolución):
# Permite al usuario actualizar el número de copias cuando un libro es prestado (préstamo) o devuelto (devolución).
    elif var_ent_opcion==7:
        var_str_modificar:str=input("INGRESA TÍTULO QUE DESEAS MODIFICAR: ")
        for i in range(len(lista_str_titulos)):
            if lista_str_titulos[i]==var_str_modificar.capitalize():
                lista_ent_ejemplares[i]=int(input("INGRESE CANTIDAD DE COPIAS DISPONIBLES: "))
                print(f"{lista_str_titulos[i]} : {lista_ent_ejemplares[i]} copias")
        print("----------   INGRESE OTRA OPCIÓN   ----------\n")
        var_ent_opcion:int=int(input("[ 1 ]	Ingresar lista de títulos\n[ 2 ]	Ingresar lista de ejemplares disponibles (por título)\n[ 3 ]	Mostrar catálogo con stock:\n[ 4 ]	Consultar disponibilidad de un título específico:\n[ 5 ]   Listar agotados (0 ejemplares)\n[ 6 ]	Agregar título\n[ 7 ]	Actualizar ejemplares (préstamo/devolución)\n[ 8 ]	Ver catálogo\n[ 9 ]   Salir\n"))
        while var_ent_opcion<1 and var_ent_opcion>9:
            var_ent_opcion=3


# 8.	Ver catálogo:
# Muestra el catálogo entero de los títulos de libros.

    elif var_ent_opcion==8:
        for i in range(len(lista_str_titulos)):
            print(f"{lista_str_titulos[i]} : {lista_ent_ejemplares[i]} copias")
        print("----------   INGRESE OTRA OPCIÓN   ----------\n")
        var_ent_opcion:int=int(input("[ 1 ]	Ingresar lista de títulos\n[ 2 ]	Ingresar lista de ejemplares disponibles (por título)\n[ 3 ]	Mostrar catálogo con stock:\n[ 4 ]	Consultar disponibilidad de un título específico:\n[ 5 ]   Listar agotados (0 ejemplares)\n[ 6 ]	Agregar título\n[ 7 ]	Actualizar ejemplares (préstamo/devolución)\n[ 8 ]	Ver catálogo\n[ 9 ]   Salir\n"))
        while var_ent_opcion<1 and var_ent_opcion>9:
            var_ent_opcion=3
# 9.	Salir:
# Sale del programa.
    elif var_ent_opcion==9:
        print("FIN")
print("\n-------  GRACIAS POR UTILIZAR EL PROGRAMA    -------")