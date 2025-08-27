#ACOSTA LUCERO TP2 CONDICIONALES
# 1-Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

edad: int=int(input("Ingrese su edad: "))

if edad>17 and edad<100:
    print("Es mayor de edad")
elif edad<18 and edad>0:
    print("Es menor de edad")
else:
    print("ERROR")

# 2-Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”

nota: int=int(input("Ingrese su nota: "))

if nota>=6 and nota<10:
    print("Aprobado")
elif nota<6 and edad>=0:
    print("Desaprobado")
else:
    print("ERROR")

# 3-Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par"

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

password: int=len(input("Ingrese contraseña: "))

if password>7 and password<15:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta (Por favor, ingrese una contraseña de entre 8 y 14 caracteres)")

# 6-escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
