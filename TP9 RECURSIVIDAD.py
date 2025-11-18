#factorial
def factorial(num):
    if num==0:
        return 1
    else: return num*factorial(num-1)
while True:
    try:
        valor=int(input("Ingrese número positivo: "))
        if valor>1:
            break
    except: Exception
print(factorial(valor))
#fibonacci
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
while True:
    try:
        valor=int(input("Ingrese número: "))
        if valor>1:
            break
    except: Exception
print(f"Fibonacci hasta la posición {valor}:")
for i in range(valor + 1):
    print(fibonacci(i), end=" ")
#3 potencia
def potencia(base, exponente):
    if exponente==0:
        return 1   
    else:
        return base*potencia(base,exponente-1)  
while True:
    try:
        base=float(input("Ingrese la base: "))
        exponente = int(input("Ingrese exponente (entero no negativo): "))
        if exponente>=0:
            break
    except: Exception
resultado = potencia(base, exponente)
print(f"{base} elevado a {exponente} es: {resultado}")
#4 es_palindromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0]!=palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])
while True:
    try:
        texto = input("Ingrese una palabra: ").lower().strip()
        if texto.isalpha():
            break
    except: Exception

if es_palindromo(texto):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
#suma_digitos
def suma_digitos(num):
    if num<10:
        return num
    return (num%10) + suma_digitos(num//10)
while True:
    try:
        valor=int(input("Ingrese número: "))
        if valor>0:
            break
    except: Exception
print(suma_digitos(valor))  
#contar_bloques
def contar_bloques(num):
    if num==1:
        return 1
    return num+contar_bloques(num-1)
while True:
    try:
        valor=int(input("Ingrese número: "))
        if valor>0:
            break
    except: Exception
print(contar_bloques(valor))
