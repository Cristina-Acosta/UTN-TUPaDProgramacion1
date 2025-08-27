#ACOSTA LUCERO TP1 SECUENCIALES
# 1-crear un programa que imprima "Hola Mundo!"

print("Hola Mundo!")

# 2-Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”.

nombre: str=input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

# 3-Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.

nombre: str=input("Ingrese su nombre: ")
apellido: str=input("Ingrese su apellido: ")
edad: int=int(input("Ingrese su edad: "))
residencia: str=input("Ingrese su residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia} ")

# 4-Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

import math
radio: int=int(input("Ingrese radio: "))
area: int= round(math.pi * (radio**2))
print(f"El área del círculo con radio {radio} es : {area}")

#5-Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos: int=int(input("Ingrese cantidad de SEGUNDOS: "))
minutos: int=(segundos/60)
print(f"{segundos} segundos equivalen a {minutos} MINUTOS")

#6-Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

num: int=int(input("Ingrese un número: "))

for i in range(11):
    resultado: int=num*i
    if resultado<10:
        print(f" {num} * {i} = 0{resultado}")
    else:
        print(f" {num} * {i} = {resultado}")

#7- Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre porpantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1: int=int(input("INGRESE NÚMERO 1 ( diferente de 0 ): "))
num2: int=int(input("INGRESE NÚMERO 2 ( diferente de 0 ): "))
print(f"SUMA: {num1} + {num2} = {num1+num2}")
print(f"DIVISIÓN: {num1} / {num2} = {num1/num2}")
print(f"MULTIPLICACIÓN: {num1} * {num2} = {num1*num2}")
print(f"RESTA: {num1} - {num2} = {num1-num2}")

#8- Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
print("CALCULA TU INDICE DE MASA CORPORAL")
altura: float=float(input("INGRESE ALTURA en metros: "))
peso: float=float(input("INGRESE PESO en kilos: "))
print(f"IMC(peso/altura^2) = {peso/(altura**2)}")

#9- Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

print("CONVERTIDOR DE CELSIUS A FAHRENHEIT")
celsius: float=float(input("INGRESE GRADOS CELSIUS: "))
fahrenheit: float= (celsius * 9/5)+32
print(f"{celsius}°C = {fahrenheit}°F")

#10- Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

print("PROMEDIOS")
num: float=0
for i in range(3):
        num+=int(input(f"INGRESE NÚMERO {i+1}: "))

promedio: float=num//3
print(f"PROMEDIO = {promedio}")