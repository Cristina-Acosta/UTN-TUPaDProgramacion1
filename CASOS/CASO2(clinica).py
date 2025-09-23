print("ACOSTA CRISTINA - CASO 2 CLINICA - TURNOS - PROGRAMACIÓN UTN - COM2")

#Se pide implementar un programa que utilice listas paralelas: una lista especialidades[] para almacenar los nombres de las especialidades (e.g., "Cardiología", "Dermatología") y otra lista cupos[] para almacenar el número de cupos disponibles para cada especialidad en un día específico. Ambas listas deben compartir el mismo índice, de manera que el cupo en cupos[i] corresponda a la especialidad en especialidades[i]. El programa debe presentar un menú al usuario y utilizar un bucle while para permitirle realizar diferentes operaciones hasta que elija la opción "Salir".
#Menú:

print("\n----------     MENÚ DE LA CLÍNICA    ----------\n")
print("----------   INGRESE LA OPCIÓN QUE DESEA   ----------\n")
var_ent_opcion:int=int(input("[ 1 ]	Ingresar lista de especialidades\n[ 2 ]	Ingresar lista de cupos disponibles por especialidad\n[ 3 ]	Mostrar agenda\n[ 4 ]	Consultar cupos de una especialidad\n[ 5 ]   Listar especialidades sin cupo\n[ 6 ]	Agregar especialidad\n[ 7 ]	Actualizar cupos (reservar/cancelar)\n[ 8 ]	Ver agenda\n[ 9 ]   Salir\n"))
if var_ent_opcion<1 or var_ent_opcion>9:
    var_ent_opcion=9

lista_str_especialidades=[]
lista_ent_cupos=[]
#1.	Ingresar lista de especialidades: (Añadir especialidades a la lista)
while var_ent_opcion!=9:
    if var_ent_opcion==1:
        var_ent_cantidad:int=int(input("CANTIDAD DE ESPECIALIDADES: "))
        for i in range(var_ent_cantidad):
            var_str_especialidad:str=input(f"INGRESE ESPECIALIDAD n° {i+1}: ")
            lista_str_especialidades.append(var_str_especialidad.upper())
            print(f"AGREGASTE: {var_str_especialidad.upper()}")
        print("\n----------   INGRESE OTRA OPCIÓN QUE DESEE   ----------\n")
        var_ent_opcion:int=int(input("[ 1 ]	Ingresar lista de especialidades\n[ 2 ]	Ingresar lista de cupos disponibles por especialidad\n[ 3 ]	Mostrar agenda\n[ 4 ]	Consultar cupos de una especialidad\n[ 5 ]   Listar especialidades sin cupo\n[ 6 ]	Agregar especialidad\n[ 7 ]	Actualizar cupos (reservar/cancelar)\n[ 8 ]	Ver agenda\n[ 9 ]   Salir\n"))
        if var_ent_opcion<1 or var_ent_opcion>9:
            var_ent_opcion=9
#2.	Ingresar lista de cupos disponibles por especialidad: (Definir la cantidad de cupos para cada especialidad)
    elif var_ent_opcion==2:
        for i in range(len(lista_str_especialidades)):
            var_ent_cupos:int=int(input(f"INGRESE CUPOS DE {lista_str_especialidades[i]} : "))
            lista_ent_cupos.append(var_ent_cupos)
            print(f"{lista_ent_cupos[i]} cupos para {lista_str_especialidades[i]}")
        print("\n----------   INGRESE OTRA OPCIÓN QUE DESEA   ----------\n")
        var_ent_opcion:int=int(input("[ 1 ]	Ingresar lista de especialidades\n[ 2 ]	Ingresar lista de cupos disponibles por especialidad\n[ 3 ]	Mostrar agenda\n[ 4 ]	Consultar cupos de una especialidad\n[ 5 ]   Listar especialidades sin cupo\n[ 6 ]	Agregar especialidad\n[ 7 ]	Actualizar cupos (reservar/cancelar)\n[ 8 ]	Ver agenda\n[ 9 ]   Salir\n"))
        if var_ent_opcion<1 or var_ent_opcion>9:
            var_ent_opcion=9
#3.  Mostrar agenda: (Mostrar la disponibilidad de cupos por especialidad
    elif var_ent_opcion==3:
        print("\n----------   AGENDA   ----------\n")
        for i in range(len(lista_str_especialidades)):
            print(f"{lista_str_especialidades[i]} : {lista_ent_cupos[i]} cupos disponibles ")
        print("\n----------   INGRESE OTRA OPCIÓN QUE DESEE   ----------\n")
        var_ent_opcion:int=int(input("[ 1 ]	Ingresar lista de especialidades\n[ 2 ]	Ingresar lista de cupos disponibles por especialidad\n[ 3 ]	Mostrar agenda\n[ 4 ]	Consultar cupos de una especialidad\n[ 5 ]   Listar especialidades sin cupo\n[ 6 ]	Agregar especialidad\n[ 7 ]	Actualizar cupos (reservar/cancelar)\n[ 8 ]	Ver agenda\n[ 9 ]   Salir\n"))
        if var_ent_opcion<1 or var_ent_opcion>9:
            var_ent_opcion=9
#4.	Consultar cupos de una especialidad: (Verificar la disponibilidad de una especialidad específica)
    elif var_ent_opcion==4:
        var_str_consulta:str=input("INGRESE ESPECIALIDAD: ")
        for i in range(len(lista_str_especialidades)):
            if lista_str_especialidades[i]==var_str_consulta.upper():
                print (f"{lista_str_especialidades[i]} tiene {lista_ent_cupos[i]} cupos disponibles")
        print("\n----------   INGRESE OTRA OPCIÓN QUE DESEE   ----------\n")
        var_ent_opcion:int=int(input("[ 1 ]	Ingresar lista de especialidades\n[ 2 ]	Ingresar lista de cupos disponibles por especialidad\n[ 3 ]	Mostrar agenda\n[ 4 ]	Consultar cupos de una especialidad\n[ 5 ]   Listar especialidades sin cupo\n[ 6 ]	Agregar especialidad\n[ 7 ]	Actualizar cupos (reservar/cancelar)\n[ 8 ]	Ver agenda\n[ 9 ]   Salir\n"))
        if var_ent_opcion<1 or var_ent_opcion>9:
            var_ent_opcion=9
#5.	Listar especialidades sin cupo: (Identificar las especialidades que están llenas)
    elif var_ent_opcion==5:
        print("\nESPECIALIDADES SIN CUPO\n")
        for i in range(len(lista_str_especialidades)):
            if lista_ent_cupos[i]==0:
                print(f"{lista_str_especialidades[i]} no tiene cupos disponibles")
        print("\n----------   INGRESE OTRA OPCIÓN QUE DESEE   ----------\n")
        var_ent_opcion:int=int(input("[ 1 ]	Ingresar lista de especialidades\n[ 2 ]	Ingresar lista de cupos disponibles por especialidad\n[ 3 ]	Mostrar agenda\n[ 4 ]	Consultar cupos de una especialidad\n[ 5 ]   Listar especialidades sin cupo\n[ 6 ]	Agregar especialidad\n[ 7 ]	Actualizar cupos (reservar/cancelar)\n[ 8 ]	Ver agenda\n[ 9 ]   Salir\n"))
        if var_ent_opcion<1 or var_ent_opcion>9:
            var_ent_opcion=9
#6.	Agregar especialidad: (Sumar una nueva especialidad a la lista)
    elif var_ent_opcion==6:
        print("\n NUEVA ESPECIALIDAD \n")
        var_str_especialidad:str=input(f"INGRESE NUEVA ESPECIALIDAD : ")
        lista_str_especialidades.append(var_str_especialidad.upper())
        var_ent_cupos:int=int(input(f"INGRESE CUPOS DE {var_str_especialidad.upper()} : "))
        lista_ent_cupos.append(var_ent_cupos)
        print(f"INGRESASTE {var_ent_cupos} cupos para {var_str_especialidad.upper()}")
        print("\n----------   INGRESE OTRA OPCIÓN QUE DESEE   ----------\n")
        var_ent_opcion:int=int(input("[ 1 ]	Ingresar lista de especialidades\n[ 2 ]	Ingresar lista de cupos disponibles por especialidad\n[ 3 ]	Mostrar agenda\n[ 4 ]	Consultar cupos de una especialidad\n[ 5 ]   Listar especialidades sin cupo\n[ 6 ]	Agregar especialidad\n[ 7 ]	Actualizar cupos (reservar/cancelar)\n[ 8 ]	Ver agenda\n[ 9 ]   Salir\n"))
        if var_ent_opcion<1 or var_ent_opcion>9:
            var_ent_opcion=9
#7.	Actualizar cupos (reservar/cancelar): (Modificar la disponibilidad al reservar o cancelar citas)
    elif var_ent_opcion==7:
        print("\n----------   MODIFICAR AGENDA   ----------\n")
        var_str_especialidad=input("INGRESE ESPECIALIDAD QUE DESEA MODIFICAR: ")
        for i in range(len(lista_str_especialidades)):
            if lista_str_especialidades[i]==var_str_especialidad.upper():
                lista_ent_cupos[i]=int(input("INGRESE CANTIDAD DE CUPOS DISPONIBLES: "))
                print(f"{lista_str_especialidades[i]} : {lista_ent_cupos[i]} cupos")
        print("\n----------   INGRESE OTRA OPCIÓN QUE DESEE   ----------\n")
        var_ent_opcion:int=int(input("[ 1 ]	Ingresar lista de especialidades\n[ 2 ]	Ingresar lista de cupos disponibles por especialidad\n[ 3 ]	Mostrar agenda\n[ 4 ]	Consultar cupos de una especialidad\n[ 5 ]   Listar especialidades sin cupo\n[ 6 ]	Agregar especialidad\n[ 7 ]	Actualizar cupos (reservar/cancelar)\n[ 8 ]	Ver agenda\n[ 9 ]   Salir\n"))
        if var_ent_opcion<1 or var_ent_opcion>9:
            var_ent_opcion=9
#8.	Ver agenda: (Mostrar la agenda completa)
    elif var_ent_opcion==8:
        print("\n----------   AGENDA   ----------\n")
        print("ESPECIALIDADES   |   CUPOS DISPONIBLES   ")
        for i in range(len(lista_str_especialidades)):
            print(f"{lista_str_especialidades[i]}   :   {lista_ent_cupos[i]} cupos ")
        print("\n----------   INGRESE OTRA OPCIÓN QUE DESEE   ----------\n")
        var_ent_opcion:int=int(input("[ 1 ]	Ingresar lista de especialidades\n[ 2 ]	Ingresar lista de cupos disponibles por especialidad\n[ 3 ]	Mostrar agenda\n[ 4 ]	Consultar cupos de una especialidad\n[ 5 ]   Listar especialidades sin cupo\n[ 6 ]	Agregar especialidad\n[ 7 ]	Actualizar cupos (reservar/cancelar)\n[ 8 ]	Ver agenda\n[ 9 ]   Salir\n"))
        if var_ent_opcion<1 or var_ent_opcion>9:
            var_ent_opcion=9

#9.	Salir: (Terminar el programa)
print("\n---------- SALISTE DEL PROGRAMA ----------")