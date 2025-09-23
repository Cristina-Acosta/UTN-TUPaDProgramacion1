print("\nACOSTA CRISTINA - TP5 LISTAS - PROGRAMACIÓN 1 - TUP COM2 -\n")

#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
print("\n---------- 100 NÚMEROS MULTIPLOS DE 4 ----------\n")
lista_numeros_a1=[]
for numero in range(1,101):
    if numero%4==0:
        lista_numeros_a1.append(numero)
print(lista_numeros_a1)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.
print("\n---------- LISTA DE 5 COSAS IMPRIMIENDO LA 4 ----------\n")

lista_cosas_a2=["COMPRAS","CAFÉ","FAMILIA","TORTITAS CON CHICHARRÓN","BICICLETA"]
print(lista_cosas_a2[-2])

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. 
print("\n---------- AGREGAR 3 PALABRAS ----------\n")

lista_vacia_a3=[]
print("INGRESA 3 PAÍSES\n")
for cosas in range(3):
    lista_vacia_a3.append(input(f"INGRESA PAÍS N° {cosas+1}: "))
print(f"Los paises ingresados son: {" ".join(lista_vacia_a3)}")

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,respectivamente. Imprimir la lista resultante por pantalla.
print("\n---------- LISTA ANIMALES ----------\n")
animales = ["perro", "gato", "conejo", "pez"]
print(animales)
animales[1],animales[-1]="loro","oso"
print(animales)

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
print("\n---------- numeros.remove(max(numeros)) ----------\n")
print("max(numeros)encontrará se pocisionará en el 22(máximo valor) y remove eliminará el 22 de la lista")

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
print("\n----------     NÚMEROS DEL 10 AL 30     ----------\n")
lista_numeros_a6=list(range(10,31,5))
print(lista_numeros_a6[0:2])

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

print("\n---------- 100 NÚMEROS MULTIPLOS DE 4 ----------\n")
autos = ["sedan", "polo", "suran", "gol"]
print(autos)
autos[1:3]="bora","fox"
print(autos)
#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.
print("\n----------     LISTA DE NÚMEROS DOBLES     ----------\n")
dobles=[]
for doble in range(5,16,5):
    dobles.append(doble*2)
print(dobles)

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
print("\nAgregar \"jugo\" a la lista del tercer cliente usando append.\n")
print(compras)
compras[2].append("JUGO")
print(compras)
print("\nReemplazar \"fideos\" por \"tallarines\" en la lista del segundo cliente.\n")
print(compras)
compras[1][1]="TALLARINES"
print(compras)
print("\nEliminar \"pan\" de la lista del primer cliente.\n")
print(compras)
compras[0].remove("pan")
print(compras)

print("\nImprimir la lista resultante por pantalla\n")
print(compras)

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# Posición lista_anidada[0]: 15
# Posición lista_anidada[1]: True
# Posición lista_anidada[2][0]: 25.5
# Posición lista_anidada[2][1]: 57.9
# Posición lista_anidada[2][2]: 30.6
# Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.
print("\n---------- LISTA    ANIDADA ----------\n")
lista_anidada_a10=[15,True,[25.5,57.9,30.6],False]
print(lista_anidada_a10)
