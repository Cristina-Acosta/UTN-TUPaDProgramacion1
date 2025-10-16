#ACOSTA CRISTINA - TUP COM2 - TP6 FUNCIONES

#1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.
print("-----------------      MENSAJE     ----------------")

#funciones
def imprimir_hola_mundo(mensaje):
    print(mensaje)
#main
mensaje:str="Hola Mundo!"
imprimir_hola_mundo(mensaje)
print("|--------------------------------------------------|")
#2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.
#funciones
print("-----------------      SALUDO     ----------------")

def saludar_usuario(nombre):
    print(f"Hola {nombre.capitalize()}!")
#main
nombre:str=input("INGRESE NOMBRE: ")
saludar_usuario(nombre)
print("|--------------------------------------------------|")
#3. Crear una función llamada informacion_personal(nombre, apellido,edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
print("-----------------      PERSONAL     ----------------")
#funciones
def informacion_personal(nombre, apellido,edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
#main
nombre:str=input("NOMBRE: ")
apellido:str=input("APELLIDO: ")
edad:str=input("EDAD: ")
residencia:str=input("RESIDENCIA: ")
informacion_personal(nombre, apellido,edad, residencia)
print("|--------------------------------------------------|")

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
print("-----------------      CÍRCULO     ----------------")
#funciones
import math
def calcular_area_circulo(radio):
    area:int=math.pi * (radio ** 2)
    return area
def calcular_perimetro_circulo(radio):
    perimetro:int=2*math.pi*radio
    return perimetro
#main
radio:int=int(input("INGRESE RADIO: "))
print (f"ÁREA: {calcular_area_circulo(radio)}\nPERÍMETRO: {calcular_perimetro_circulo(radio)}")
print("|--------------------------------------------------|")
#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
print("-----------------      TIEMPO     ----------------")
#FUNCIONES
def segundos_a_horas(tiempo):
    return tiempo//60
#MAIN
segundos:int=int(input("INGRESE CANTIDAD DE SEGUNDOS: "))
minutos:float=round(segundos_a_horas(segundos),1)
horas:float=round(segundos_a_horas(minutos),1)
print(f"{segundos} segundos = {minutos} minutos = {horas} horas")
print("|--------------------------------------------------|")
#6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.
print("-----------------      TABLA     ----------------")
#FUNCIONES
def tabla_multiplicar(numero):
    for i in range(1,10+1):
        print(f"{numero} x {i} = {numero*i}")
#MAIN
numero:int=int(input("INGRESE NÚMERO: "))
tabla_multiplicar(numero)
print("|--------------------------------------------------|")
#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
print("-----------------      + - x /     ----------------")
#FUNCIONES
def operaciones_basicas(a, b):
    tupla=()
    tupla=a+b,a-b,a*b,a//b
    return tupla
#MAIN
num1:int=int(input("INGRESE NÚMERO 1: "))
num2:int=int(input("INGRESE NÚMERO 2: "))
tupla=(operaciones_basicas(num1,num2))
print(f"{num1}+{num2}={tupla[0]}\n{num1}-{num2}={tupla[1]}\n{num1}x{num2}={tupla[2]}\n{num1}/{num2}={tupla[3]}")
print("|--------------------------------------------------|")
#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
print("-----------------      I  M  C     ----------------")
#FUNCIONES
def calcular_imc(peso,altura):
    IMC:float=peso/(altura**2)
    print(f"IMC: {round(IMC,2)}")
#MAIN
peso:float=float(input("INGRESE PESO: "))
altura:float=float(input("INGRESE ALTURA: "))
calcular_imc(peso,altura)
print("|--------------------------------------------------|")
#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
print("-----------------     °C  ->  °F     ----------------")
#FUNCIONES
def celsius_a_fahrenheit(celsius):
    return (celsius*9/5) + 32
#MAIN
celsius:float=float(input("INGRESE ° CELSIUS: "))
Fahrenheit:float=celsius_a_fahrenheit(celsius)
print(f"{celsius}° C = {Fahrenheit}° F")
print("|--------------------------------------------------|")
#10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.Solicitar los números al usuario y mostrar el resultado usando esta función.
print("-----------------     PROMEDIOS     ----------------")
#FUNCIONES
def calcular_promedio(a, b, c):
    return (a+b+c)/3
#MAIN
lista=[]
for i in range(3):
    lista.append(float(input(f"| INGRESE NÚMERO {i+1}: ")))
promedio:float=calcular_promedio(lista[0], lista[1], lista[2])
print(f"| PROMEDIO: {round(promedio,2)}")
print("|--------------------------------------------------|")