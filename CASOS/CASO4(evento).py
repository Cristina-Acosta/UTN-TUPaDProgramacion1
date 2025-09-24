print(" ACOSTA CRISTINA - TUP COM2 - PROGRAMACIÓN I - CASO EVENTOS (entradas por show)")
#Se pide crear un menú que emplee listas paralelas: una lista shows[] para almacenar los nombres de los shows (e.g., "Concierto de Rock", "Obra de Teatro", "Festival de Jazz") y otra lista entradas[] para almacenar la cantidad de entradas disponibles para cada show. Ambas listas deben estar relacionadas por el índice, de manera que la cantidad de entradas en entradas[i] corresponda al show en shows[i]. El programa debe usar un bucle while para permitirle al usuario realizar diferentes operaciones hasta que elija la opción "Salir".
lista_str_shows=[]
lista_ent_entradas=[]
var_ent_opcion:int=0
while var_ent_opcion!=9:
    if var_ent_opcion==0:
        print("\n----------  MENÚ    EVENTOS  ----------\n")
        print("\n---------- ELIGE UNA OPCIÓN ----------\n")

        var_ent_opcion=int(input("[ 1 ]Ingresar shows\n[ 2 ]Ingresar entradas por show\n[ 3 ]Mostrar shows/entradas\n[ 4 ]Consultar entradas de un show\n[ 5 ]Listar shows agotados\n[ 6 ]Agregar show\n[ 7 ]Actualizar entradas\n[ 8 ]Ver todos los shows\n[ 9 ] SALIR \n"))
        if var_ent_opcion<0 or var_ent_opcion>9:
            var_ent_opcion=0
    elif var_ent_opcion==1:
        print("\n----- INGRESE SHOWS DISPONIBLES -----\n")
        var_ent_cantidad:int=int(input("INGRESE CANTIDAD DE SHOWS DISCPONIBLES: "))
        for i in range(var_ent_cantidad):
            var_str_show:str=input(f"INGRESE SHOW n°{i+1}: ")
            lista_str_shows.append(var_str_show.upper())
            print(f"AGREGASTE: {var_str_show.upper()}")
        var_ent_opcion=0
    elif var_ent_opcion==2:
        print("\n----- INGRESE ENTRADAS DISPONIBLES -----\n")
        for i in range(len(lista_str_shows)):
            var_ent_cantidad=int(input(f"INGRESE ENTRADAS DISPONIBLES SHOW: {lista_str_shows[i]}  "))
            lista_ent_entradas.append(var_ent_cantidad)
            print(f"AGREAGASTE {var_ent_cantidad} ENTRADAS PARA {lista_str_shows[i]}")
        var_ent_opcion=0
    elif var_ent_opcion==3:
        print("\n----- SHOWS DISPONIBLES -----\n")
        for i in range(len(lista_str_shows)):
            print(f"{lista_str_shows[i]} :  {lista_ent_entradas[i]}")
        var_ent_opcion=0
    elif var_ent_opcion==4:
        print("\n----- CONSULTAR ENTRADAS -----\n")
        var_str_show=input("INGRESE NOMBRE DEL SHOW: ")
        for i in range(len(lista_str_shows)):
            if lista_str_shows[i]==var_str_show.upper():
                print(f"{lista_str_shows[i]} tiene {lista_ent_entradas[i]} entradas disponibles")
        var_ent_opcion=0
    elif var_ent_opcion==5:
        print("\n-----  SHOWS  AGOTADOS  -----\n")
        for i in range(len(lista_str_shows)):
            if lista_ent_entradas[i]==0:
                print(f"{lista_str_shows[i]} : {lista_ent_entradas[i]} entradas disponibles")
        var_ent_opcion=0
    elif var_ent_opcion==6:
        print("\n----- AGREGAR   SHOW -----\n")
        var_str_show=input("INGRESE NOMBRE DE SHOW NUEVO: ")
        lista_str_shows.append(var_str_show.upper())
        var_ent_cantidad=int(input(f"INGRESE ENTRADAS DISPONIBLES PARA {var_str_show.upper()} : "))
        lista_ent_entradas.append(var_ent_cantidad)
        print(f"AGREGASTE {var_ent_cantidad} ENTRADAS PARA {var_str_show.upper()} !")
        var_ent_opcion=0
    elif var_ent_opcion==7:
        print("\n----- MODIFICAR  ENTRADAS -----\n")
        var_str_show=input("INGRESA NOMBRE DE SHOW A MODIFICAR: ")
        for i in range(len(lista_str_shows)):
            if var_str_show.upper()==lista_str_shows[i]:
                lista_ent_entradas[i]=int(input("INGRESE CANTIDAD DE ENTRADAS DISPONIBLES: "))
        print(f"Listo! {lista_str_shows[i]} tiene {lista_ent_entradas[i]} entradas disponibles")
        var_ent_opcion=0
    elif var_ent_opcion==8:
        print("\n----- SHOWS  DISPONIBLES -----\n")
        for i in range(len(lista_str_shows)):
            print(f"{lista_str_shows[i]} : {lista_ent_entradas[i]} entradas")
        var_ent_opcion=0
print("SALISTE DEL PROGRAMA")