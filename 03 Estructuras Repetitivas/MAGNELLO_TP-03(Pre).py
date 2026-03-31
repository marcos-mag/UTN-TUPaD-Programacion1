#Actividad 1: Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for numero in range(101):
    print(numero)  

#Actividad 2: Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = int(input("Ingrese un número entero: "))
contador_digitos = 0
numero_absoluto = abs(numero)  # Para manejar números negativos

if numero_absoluto == 0:
    contador_digitos = 1
else:
    while numero_absoluto > 0:
        numero_absoluto //= 10
        contador_digitos += 1

print(f"El {numero} tiene {contador_digitos} dígitos.")

#Actividad 3: Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

valor1 = int(input("Ingrese el primer valor entero: "))
valor2 = int(input("Ingrese el segundo valor entero: "))    
suma = 0
for numero in range(min(valor1, valor2) + 1, max(valor1, valor2)):
    suma += numero
print(f"La suma de los números enteros entre {valor1} y {valor2} es: {suma}")       

#Actividad 4: Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

suma_acumulada = 0
while True:
    numero = int(input("Ingrese un número entero (0 para finalizar): "))
    if numero == 0:
        break
    suma_acumulada += numero
print(f"El total acumulado es: {suma_acumulada}")

#Actividad 5: Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numero_aleatorio = random.randint(0, 9)
intentos = 0
while True:
    intento_usuario = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    if intento_usuario == numero_aleatorio:
        print(f"¡Felicidades! Has adivinado el número {numero_aleatorio} en {intentos} intentos.")
        break
    elif intento_usuario < numero_aleatorio:
        print("El número es mayor. Inténtalo de nuevo.")
    else:
        print("El número es menor. Inténtalo de nuevo.")

#Actividad 6: Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

print("Números pares entre 0 y 100 en orden decreciente:")
for numero in range(100, -1, -2):
    print(numero)

#Actividad 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario

numero_usuario = int(input("Ingrese un número entero positivo: "))
if numero_usuario >= 0:
    suma = 0
    for i in range(numero_usuario + 1):
        suma += i
    print(f"La suma de todos los números entre 0 y {numero_usuario} es: {suma}")
else:
    print("Por favor, ingrese un número entero positivo.")

#Actividad 8: Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cantidad_numeros = 100  
contador_pares = 0
contador_impares = 0
contador_negativos = 0
contador_positivos = 0

for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i+1}: "))
    if numero % 2 == 0:
        contador_pares += 1
    elif numero % 2 != 0:
        contador_impares += 1
    if numero < 0:
        contador_negativos += 1
    elif numero > 0:
        contador_positivos += 1

print("Resultados:")
print(f"Números pares: {contador_pares}")
print(f"Números impares: {contador_impares}")
print(f"Números negativos: {contador_negativos}")
print(f"Números positivos: {contador_positivos}")

#Actividad 9: Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

cantidad_numeros = 100
suma_total = 0

print(f"Ingrese {cantidad_numeros} números enteros:")
for i in range(cantidad_numeros):
    numero = int(input(f"Número {i+1}: "))
    suma_total += numero
media = suma_total / cantidad_numeros
print(f"La media de los {cantidad_numeros} números ingresados es: {media}")

#Actividad 10: Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

#numero = int(input("Ingrese un número entero: "))
#numero_absoluto = abs(numero)
#numero_invertido = int(str(numero_absoluto)[::-1])
#print(f"El número invertido es: {numero_invertido}")

#Cuando ingreso un numero negativo, el programa invierte el orden de los dígitos pero no muestra el signo negativo. 

numero = int(input("Ingrese un número entero: "))
numero_absoluto = abs(numero)
numero_invertido = 0 

while numero_absoluto > 0:
    digito = numero_absoluto % 10
    numero_invertido = numero_invertido * 10 + digito
    numero_absoluto //= 10
if numero < 0:
    numero_invertido = -numero_invertido
print(f"El número invertido es: {numero_invertido}")