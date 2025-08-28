#ACOSTA LUCERO TP2 CONDICIONALES
# 1-Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”
print("¿Sos mayor de edad?")

edad: int=int(input("Ingrese su edad: "))

if edad>17 and edad<100:
    print("Es mayor de edad")
elif edad<18 and edad>0:
    print("Es menor de edad")
else:
    print("ERROR")

# 2-Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”

print("¿Aprobado o desaprobado?")

nota: int=int(input("Ingrese su nota(0 al 10): "))

if nota>=6 and nota<10:
    print("Aprobado")
elif nota<6 and nota>=0:
    print("Desaprobado")
else:
    print("ERROR")

# 3-Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par"

print("PAR O IMPAR")

dato: int=int(input("Ingrese un número: "))

if dato%2==0:
    print(f"{dato} es par")
else:
    print(f"{dato} es impar")

# 4- Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

print("RANGO ETARIO")

edad: int=int(input("Ingrese su edad: "))

if edad<12 and edad>0:
    print("Niño/a")
elif edad<18 and edad>=12:
    print("Adolescente")
elif edad<30 and edad>=18:
    print("Adulto/a joven")
elif edad<100 and edad>=30:
    print("Adulto/a")
else:
    print("ERROR")

# 5-Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

print("CONTRASEÑA")

password: int=len(input("Ingrese contraseña: "))

if password>7 and password<15:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta (Por favor, ingrese una contraseña de entre 8 y 14 caracteres)")

# 6-escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

print("MODA,MEDIA,MEDIANA")

from statistics import mode,median,mean
import random

numero: int = [random.randint(1, 100) for i in range(50)]

moda: float= mode(numero)
mediana: float= median(numero)
media: float= mean(numero)

print(f"MODA: {moda}")
print(f"MEDIA: {media}")
print(f"MEDIANA: {mediana}")

if media>mediana and mediana>moda:
    print("Sesgo positivo o a la derecha")
elif media<mediana and mediana<moda:
    print("Sesgo negativo o a la izquierda")
elif  mediana==moda and mediana==media:
    print("Sin sesgo")
else:
    print("ERROR")

# 7-Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

print("ÚLTIMA LETRA")

dato: str=input("Ingrese una palabra o frase: ")

if dato.endswith("a") or dato.endswith("A"):
    print(f"{dato}!")
elif dato.endswith("e") or dato.endswith("E"):
    print(f"{dato}!")
elif dato.endswith("i") or dato.endswith("I"):
    print(f"{dato}!")
elif dato.endswith("o") or dato.endswith("O"):
    print(f"{dato}!")
elif dato.endswith("u") or dato.endswith("U"):
    print(f"{dato}!")
else:
    print(dato)

# 8- Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas.
# 2. Si quiere su nombre en minúsculas. 
# 3. Si quiere su nombre con la primera letra mayúscula.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.
print("CONVERSIÓN DE NOMBRE")
nombre: str=input("Ingresa tu nombre: ")
opcion: int=int(input("Elige una opción:  1.NOMBRE EN MAYÚSCULAS 2. nombre en minúsculas 3.Nombre con letra capital  "))
if opcion==1:
    print(nombre.upper())
elif opcion==2:
    print(nombre.lower())
elif opcion==3:
    print(nombre.title())
else:print("Opción incorrecta")

# 9- Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
print(" MAGNITUD  ")
magnitud: float=float(input("Ingrese magnitud: "))
if magnitud<2:
    print("MICROSISMOS. No son perceptibles. Se producen cerca de 8.000 al día.")
elif magnitud<3 and magnitud>=2:
    print("SISMOS MENORES. No son perceptibles generalmente. Se producen cerca de 1.000 al día.")
elif magnitud<4 and magnitud>=3:
    print("SISMOS MENORES. Perceptibles a menudo; raramente provocan daños. Se producen 49.000 al año.")
elif magnitud<5 and magnitud>=4:
    print("TERREMOTOS LIGEROS. Provoca el movimiento de objetos en las viviendas, pero raramente provocan daños. Se producen 6.200 al año.")
elif magnitud<6 and magnitud>=5:
    print("TERREMOTOS MODERADOS. Puede causar daños mayores en edificaciones débiles o mal construidas. En edificaciones bien diseñadas los daños son leves. Se producen 800 al año.")
elif magnitud<7 and magnitud>=6:
    print("TERREMOTOS FUERTES. Pueden destruir áreas pobladas en hasta unos 160 kilómetros a la redonda. Se producen 120 al año.")
elif magnitud<8 and magnitud>=7:
    print("TERREMOTOS MAYORES. Pueden causar serios daños en extensas zonas. Se producen 18 al año.")
elif magnitud<9 and magnitud>=8:
    print("TERREMOTOS ÉPICOS o CATASTRÓFICOS. Pueden causar graves daños en zonas de varios cientos de kilómetros. Se producen de 1 a 3 al año.")
elif magnitud<10 and magnitud>=9:
    print("TERREMOTOS ÉPICOS o CATASTRÓFICOS. Devastadores, pueden afectar a zonas de miles de kilómetros. Se producen entre 1 y 2 cada 20 años.")
elif magnitud<12 and magnitud>=10:
    print("TERREMOTOS APOCALÍPTICOS o LEGENDARIOS. Nunca registrado en la historia de la Tierra. Estimado para el choque de un meteorito rocoso de 2 kilómetros de diámetro que impacte contra nuestro planeta a 25.000 kilómetros por hora.")
elif magnitud==12:
    print("Provocaría la fractura de la Tierra por el centro.")

# 10- Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

print("ESTACIONES")

hemisferio: int=int(input("Ingrese número de hemisferio: ( 1 )- NORTE ( 2 )- SUR: "))
mes: int=int(input("Ingrese número de mes: ( 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10 - 11 -12 ): "))
dia: int=int(input("Ingrese número de día: "))

while (dia>31 or dia<1) or (mes<1 or mes>12) or (hemisferio<1 or hemisferio>2):
    hemisferio: int=int(input("Ingrese número de hemisferio: ( 1 )- NORTE ( 2 )- SUR: "))
    mes: int=int(input("Ingrese número de mes: ( 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10 - 11 -12 ): "))
    dia: int=int(input("Ingrese número de día: "))
    
if hemisferio==1:
    if mes in (12,1,2,3):
        if (mes==12 and dia<21)  :
            print(f"{dia} / {mes} en el hemisferio NORTE es: OTOÑO")
        elif (mes==3 and dia>20):
            print(f"{dia} / {mes} en el hemisferio NORTE es: PRIMAVERA")
        else:
            print(f"{dia} / {mes} en el hemisferio NORTE es: INVIERNO")
    if mes in (4,5,6):
        if (mes==6 and dia>20):
            print(f"{dia} / {mes} en el hemisferio NORTE es: VERANO")
        else:
            print(f"{dia} / {mes} en el hemisferio NORTE es: PRIMAVERA")
    if mes in (7,8,9):
        if (mes==9 and dia>20):
            print(f"{dia} / {mes} en el hemisferio NORTE es: OTOÑO")
        else:
            print(f"{dia} / {mes} en el hemisferio NORTE es: VERANO")
    if mes in (10,11):
        print(f"{dia} / {mes} en el hemisferio NORTE es: INVIERNO")
    
if hemisferio==2:
    if mes in (12,1,2,3):
        if (mes==12 and dia<21):
            print(f"{dia} / {mes} en el hemisferio SUR es: PRIMAVERA")
        elif (mes==3 and dia>20):
            print(f"{dia} / {mes} en el hemisferio SUR es: OTOÑO")
        else:
            print(f"{dia} / {mes} en el hemisferio SUR es: VERANO")
    if mes in (4,5,6):
        if (mes==6 and dia>20):
            print(f"{dia} / {mes} en el hemisferio SUR es: INVIERNO")
        else:
            print(f"{dia} / {mes} en el hemisferio SUR es: OTOÑO")
    if mes in (7,8,9):
        if (mes==9 and dia>20):
            print(f"{dia} / {mes} en el hemisferio SUR es: PRIMAVERA")
        else:
            print(f"{dia} / {mes} en el hemisferio SUR es: INVIERNO")
    if mes in (10,11):
        print(f"{dia} / {mes} en el hemisferio SUR es: VERANO")