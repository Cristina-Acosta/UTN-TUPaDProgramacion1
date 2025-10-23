#ACOSTA CRISTINA - TUP COM2 - TP7 DATOS COMPLEJOS
#1) Dado el diccionario precios_frutas 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

#Añadir las siguientes frutas con sus respectivos precios:
#Naranja = 1200 Manzana = 1500 Pera = 2300
print("-----------------      AÑADIR     ----------------")

precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500 
precios_frutas["Pera"]=2300
print(precios_frutas)
print("|--------------------------------------------------|")

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: Banana = 1330 Manzana = 1700 Melón = 2800

print("-----------------      ACTUALIZAR     ----------------")
precios_frutas["Banana"]=1330
precios_frutas["Manzana"]=1700 
precios_frutas["Melón"]=2800
print(precios_frutas)
print("|--------------------------------------------------|")

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

print("-----------------      LISTA     ----------------")
lista_frutas=precios_frutas.keys()
print(lista_frutas)
print("|--------------------------------------------------|")
#4) Escribí un programa que permita almacenar y consultar números telefónicos.
agenda={}
# Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.

print("-----------------      CONTACTOS     ----------------")
for contacto in range (5):
    nombre=input(f"INGRESE NOMBRE DEL CONTACTO {contacto+1}: ")
    num=input(f"INGRESE NÚMERO DE {nombre}: ")
    agenda[nombre.upper()]=num
print(agenda)
# Luego, pedí un nombre y mostrale el número asociado, si existe.
buscar=input("Ingrese nombre: ")
print(agenda.get(buscar.upper()))
print("|--------------------------------------------------|")
#5) Solicita al usuario una frase e imprime: 
from collections import Counter
frase=input("INGRESE UNA FRASE BONITA: ")
# Las palabras únicas (usando un set). 
palabras= frase.lower().split()
print(palabras)
palabras_unicas=set(palabras)
print(palabras_unicas)
# Un diccionario con la cantidad de veces que aparece cada palabra
print("-----------------      ACTUALIZAR     ----------------")
cantidad=Counter(palabras)
print(cantidad)
print("|--------------------------------------------------|")

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.Luego, mostrá el promedio de cada alumno.
print("-----------------      ACTUALIZAR     ----------------")

for nombres in range (3):
    nombre=""
    lista_nota=[]
    promedio=0
    nombre=input(f"INGRESE NOMBRE DEL ALUMNO {nombres+1}: ")
    for notas in range(3):
        nota=int(input(f"Ingrese nota {notas+1}: "))
        promedio+=nota
        lista_nota.append(nota)
    tupla_nota=tuple(lista_nota)
    promedio//=3
    clase={"alumno":nombre,"notas":tupla_nota,"promedio":promedio}
    print(clase)
print("|--------------------------------------------------|")
#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2: 
# Mostrá los que aprobaron ambos parciales.

print("-----------------      PARCIALES     ----------------")
from collections import Counter
parcial1={10,4,6,8,5,7,4}
parcial2={9,3,7,9,7,5,8}
# Mostrá los que aprobaron solo uno de los dos.
UNO=list(parcial1|parcial2)
print(UNO)
aprobados=Counter(n for n in UNO if n>5)
print(aprobados)
print("|--------------------------------------------------|")

# Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
print("-----------------      ACTUALIZAR     ----------------")

print("|--------------------------------------------------|")

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
print("-----------------      PRODUCTOS     ----------------")
productos={"remeras":20,"pantalones":15,"shortes":17,"camisas":11,"gorras":19}

# Consultar el stock de un producto ingresado.
busqueda:str=input("Ingrese producto: ").lower()
print(f"STOCK DE \"{busqueda}\": {productos.get(busqueda,"NO EXISTEN")} UNIDADES")
print(productos)
# Agregar unidades al stock si el producto ya existe.
modificar:str=input("Ingrese producto del stock que desea modificar o crear:\n ").lower()
if modificar in productos:
    productos[modificar]=int(input("Ingrese stock: "))
# Agregar un nuevo producto si no existe.
else:
    productos[modificar]=int(input("Ingrese stock de nuevo producto: "))
print(productos)

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.
print("-----------------      AGENDA     ----------------")
agenda={{"lunes",15}:"teatro",{"martes",15}:"cine",{"miércoles",15}:"recital",{"jueves",15}:"karaoke",{"viernes",15}:"baile",{"sábado",15}:"bingo"}
buscar=input("Ingrese día: ")
print("|--------------------------------------------------|")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# Las capitales sean las claves.
# Los países sean los valores.

print("-----------------      CAPITALES     ----------------")
capitales={}
paises={"Argentina":"Buenos Aires","Chile":"Santiago de Chile","Uruguay":"Montevideo","Brasil":"Río de Janeiro","Bolivia":"Sucre","Paraguay":"Asunción"}
print(paises)
for pais,capital in paises.items():
    capitales[capital]=pais
print(capitales)


print("|--------------------------------------------------|")
