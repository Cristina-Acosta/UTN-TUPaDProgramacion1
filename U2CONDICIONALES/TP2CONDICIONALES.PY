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