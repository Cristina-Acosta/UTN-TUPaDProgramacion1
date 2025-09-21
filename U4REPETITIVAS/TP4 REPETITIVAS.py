#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

print("\n----------    DEL  0 AL 100    ----------\n")
for i in range(0,101):
    print("[ ",i," ]")

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

print("\n----------CANTIDAD DE DÍGITOS  ----------\n")
var_str_num:str=(input("INGRESE UN NÚMERO ENTERO: "))
var_ent_cantidad:int=len(var_str_num)
print(f"CANTIDAD DE DÍGITOS INGRESADOS: {var_ent_cantidad}")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
print("\n---------- SUMA    DE  VALORES ----------\n")
var_ent_num1:int=int(input("INGRESE VALOR 1: "))
var_ent_num2:int=int(input("INGRESE VALOR 2: "))

if var_ent_num1<var_ent_num2:
    var_ent_sumatoria:int=0
    print(f"OK, SUMAREMOS LOS NÚMEROS ENTRE {var_ent_num1} y {var_ent_num2}")
    for i in range(var_ent_num1,var_ent_num2+1):
        print(f"{var_ent_sumatoria} + {i} = {var_ent_sumatoria+i} ")
        var_ent_sumatoria+=i
    print(f"TOTAL: {var_ent_sumatoria}")
elif var_ent_num2<var_ent_num1:
    var_ent_sumatoria:int=0
    print(f"OK, SUMAREMOS LOS NÚMEROS ENTRE {var_ent_num2} y {var_ent_num1}")
    for i in range(var_ent_num2,var_ent_num1+1):
        print(f"{var_ent_sumatoria} + {i} = {var_ent_sumatoria+i} ")
        var_ent_sumatoria+=i
    print(f"TOTAL: {var_ent_sumatoria}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
print("\n----------SUMA DE DÍGITOS EN SECUENCIA----------\n")

var_ent_sumatoria_a4:int=0
var_ent_bandera_a4:int=1
while var_ent_bandera_a4!=0:
    var_ent_num_a4:int=int(input("INGRESA NÚMERO QUE DESEAS SUMAR o [ 0 ] PARA VER EL ACUMULADO:  "))
    if var_ent_num_a4==0:
        var_ent_bandera_a4=0
    var_ent_sumatoria_a4+=var_ent_num_a4
print(f"TOTAL {var_ent_sumatoria_a4}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
print("\n----------   NÚMERO ALEATORIO----------\n")

import random
var_ent_numaleatorio_a5:int=int(random.randrange(1,10))
var_ent_num_a5:int=int(input("ADIVINA EL NÚMERO\nINGRESA UN NÚMERO ENTRE 1 Y 10: "))
while var_ent_num_a5!=var_ent_numaleatorio_a5:
    print("\n¡FALLASTE!\n")
    var_ent_num_a5:int=int(input("¡INTENTA DE NUEVO!\nINGRESA UN NÚMERO ENTRE 1 Y 10: "))
print(f"¡ACERTASTE! el número es {var_ent_numaleatorio_a5}")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
print("\n----------   NÚMEROS PARES   ----------\n")

for i in range(98,0,-2):
    print(f"[ {i} ]")

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
print("\n----------   SUMA ACUMULADA DE DÍGITOS----------\n")
var_ent_sumatoria_a7:int=0
var_ent_num_a7:int=int(input("INGRESE NÚMERO POSITIVO QUE DESEA SUMAR: "))
while var_ent_num_a7<0:
    var_ent_num_a7:int=int(input("EL NÚMERO DEBE SER POSITIVO: "))
for i in range(0,var_ent_num_a7+1):
    var_ent_sumatoria_a7+=i
    print(f"{var_ent_sumatoria_a7} + {i} = {var_ent_sumatoria_a7+i} ")
    var_ent_sumatoria_a7+=i
print(f"TOTAL: {var_ent_sumatoria_a7}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
print("\n----------   100   NÚMEROS   ----------\n")

var_ent_pares_a8:int=0
var_ent_impares_a8:int=0
var_ent_positivo_a8:int=0
var_ent_negativo_a8:int=0

for i in range(1,101):
    var_ent_num_a8:int=int(input(f"INGRESA NÚMERO {i}: "))
    if var_ent_num_a8%2==0:
        var_ent_pares_a8+=1
    else:
        var_ent_impares_a8+=1
    if var_ent_num_a8>=0:
        var_ent_positivo_a8+=1
    else:
        var_ent_negativo_a8+=1
print(f"DE LOS 100 NÚMEROS INGRESADOS {var_ent_pares_a8} SON PARES")
print(f"DE LOS 100 NÚMEROS INGRESADOS {var_ent_impares_a8} SON IMPARES")
print(f"DE LOS 100 NÚMEROS INGRESADOS {var_ent_positivo_a8} SON POSITIVOS")
print(f"DE LOS 100 NÚMEROS INGRESADOS {var_ent_negativo_a8} SON NEGATIVOS")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).
print("\n---------- MEDIA 100 NÚMEROS ----------\n")
var_ent_sumatoria_a9:int=0
for i in range(1,101):
    var_ent_num_a9:int=int(input(f"INGRESÁ NÚMERO {i}: "))
    var_ent_sumatoria_a9+=var_ent_num_a9
print(f"LA MEDIA ES: {var_ent_sumatoria_a9//100}")
#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
print("\n---------- INVERTIR EL ORDEN ----------\n")

var_ent_num_a10:int=int(input("INGRESE NÚMERO QUE DESEA INVERTIR: "))
var_ent_digito_a10:int=0
var_ent_num2_a10:int=0
print(f"{var_ent_num_a10} = ",end="")
while var_ent_num_a10!=0:
    var_ent_digito_a10=var_ent_num_a10%10
    var_ent_num2_a10=(var_ent_num2_a10*10)+var_ent_digito_a10
    var_ent_num_a10//=10
print(f"{var_ent_num2_a10}")