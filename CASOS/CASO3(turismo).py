print("ACOSTA CRISTINA - PROGRAMACIÓN I - TUP COM2 - Turismo – Excursiones y cupos")

#Se pide construir un menú que utilice listas paralelas: una lista excursiones[] para almacenar los nombres de las excursiones (ej., "City Tour", "Trekking Montaña") y otra lista cupos[] para almacenar la cantidad de cupos disponibles para cada excursión. Ambas listas deben compartir el índice, de manera que la cantidad de cupos en cupos[i] corresponda a la excursión en excursiones[i]. El programa debe usar un bucle while para presentar un menú al usuario, permitiéndole realizar diferentes operaciones hasta que elija la opción "Salir".
lista_str_excursiones=[]
lista_ent_cupos=[]
var_ent_opcion=0
while var_ent_opcion!=9:
    if var_ent_opcion==0:
        print("\n---------- MENÚ EMPRESA DE TURISMO ----------\n")
        var_ent_opcion:int=int(input("INGRESE LA OPCIÓN QUE DESEE: \n[ 1 ] Ingresar excursiones\n[ 2 ] Ingresar cupos por excursión\n[ 3 ] Mostrar oferta/cupos\n[ 4 ] Consultar cupo por nombre\n[ 5 ] Ver sin cupo\n[ 6 ] Agregar excursión\n[ 7 ] Actualizar cupos\n[ 8 ] Ver todas excursiones\n[ 9 ] SALIR\n"))
    elif var_ent_opcion==1:
        print("\n---------- EXCURSIONES -----------\n")
        var_ent_cantidad:int=int(input("INGRESE CANTIDAD DE EXCURSIONES: "))
        for i in range(var_ent_cantidad):
            var_str_excursiones:str=input(f"INGRESE EXCURSIÓN n°{i+1}: ")
            lista_str_excursiones.append(var_str_excursiones.upper())
            print(f"AGREGASTE: {var_str_excursiones.upper()}")
        print("Listo!\n")
        var_ent_opcion=0
    elif var_ent_opcion==2:
        print("\n----------     CUPOS    -----------\n")
        for i in range(len(lista_str_excursiones)):
            var_ent_cupos:int=int(input(f"INGRESE CANTIDAD DE CUPOS DE LA EXCURSIÓN {lista_str_excursiones[i]}: "))
            lista_ent_cupos.append(var_ent_cupos)
            print(f"AGREGASTE {var_ent_cupos} CUPOS PARA {lista_str_excursiones[i]}")
        print("\nListo!\n")
        var_ent_opcion=0
    elif var_ent_opcion==3:
        print("\n---------- EXCURSIONES DISPONIBLES -----------\n")
        for i in range(len(lista_str_excursiones)):
            print (f"{lista_str_excursiones[i]} : {lista_ent_cupos[i]} cupos disponibles")
        var_ent_opcion=0
    elif var_ent_opcion==4:
        print("\n---------- CONSULTAR    CUPO -----------\n")
        var_str_excursiones=input("INGRESE NOMBRE DE EXCURSIÓN: ")
        for i in range(len(lista_str_excursiones)):
            if lista_str_excursiones[i]==var_str_excursiones.upper():
                print(f"{lista_str_excursiones[i]} : {lista_ent_cupos[i]} cupos disponibles")
        var_ent_opcion=0
    elif var_ent_opcion==5:
        print("\n---------- EXCURSIONES SIN CUPO -----------\n")
        for i in range(len(lista_str_excursiones)):
            if lista_ent_cupos[i]==0:
                print(f"{lista_str_excursiones[i]} no tiene cupos disponibles")
        var_ent_opcion=0
    elif var_ent_opcion==6:
        print("\n---------- AGREGAR EXCURSIÓN -----------\n")
        var_str_excursiones=input("INGRESE NUEVA EXCURSIÓN: ")
        lista_str_excursiones.append(var_str_excursiones.upper())
        var_ent_cupos=int(input(f"INGRESE CUPOS DISPONIBLES PARA LA EXCURSIÓN {var_str_excursiones}: "))
        lista_ent_cupos.append(var_ent_cupos)
        print(f"AGREGASTE {var_ent_cupos} cupos para {var_str_excursiones}")
        var_ent_opcion=0
    elif var_ent_opcion==7:
        print("\n---------- ACTUALIZAR CUPO -----------\n")
        var_str_excursiones=input("INGRESE EXCURSIÓN QUE DESEA MODIFICAR: ")
        for i in range(len(lista_str_excursiones)):
            if var_str_excursiones.upper()==lista_str_excursiones[i]:
                var_ent_cupos=int(input("INGRESE CANTIDAD DE CUPO DISPONIBLE: "))
                lista_ent_cupos[i]=var_ent_cupos
                print(f"MODIFICASTE {lista_str_excursiones[i]} : {lista_ent_cupos[i]} cupos disponibles")
        var_ent_opcion=0
    elif var_ent_opcion==8:
        print("\n---------- EXCURSIONES DISPONIBLES -----------\n")
        for i in range(len(lista_str_excursiones)):
            print (f"{lista_str_excursiones[i]} : {lista_ent_cupos[i]} cupos disponibles")
        var_ent_opcion=0
print("SALISTE DEL PROGRAMA")
