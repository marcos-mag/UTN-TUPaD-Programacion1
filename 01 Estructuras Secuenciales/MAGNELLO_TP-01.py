#Actividad 1 ""Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”".

import math


print("Hola Mundo!")

#Actividad 2: "Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado".

nombre = input("¿Cuál es tu nombre? ")
print("Mucho gusto," + nombre + "!") #Sin uso de f string.
print(f"Mucho gusto, {nombre}!") #Usando f string.

#Actividad 3: Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.

nombre = input("Ingresa tu nombre:")
apellido = input("Ingresa tu apellido:")
edad = input ("Ingresa tu edad:")
lugar_residencia = input("Donde resides?:")
print("Tu nombre es " + nombre + " " + apellido + ", tenes " + edad + " pirulos y resides en " + lugar_residencia + ".") #Sin uso de f string.    
print(f"Tu nombre es {nombre} {apellido}, tenes {edad} pirulos y resides en {lugar_residencia}.") #Usando f string

#Actividad 4: Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

#El área de un circulo se calcula con la fórmula:  π * r^2 y su perimetro con la fórmula: 2 * π * r
#No estaba al tanto de que si ponia "π" o (pi) no me tomaba el valor, tuve que buscarlo. 
radio = float(input("¿Cuál es la longitud del radio del circulo?: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

#Actividad 5: Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

cantidad_segundos = int(input("Ingresa una cantidad de segundos: "))
cantidad_horas = cantidad_segundos /3600
print(f"{cantidad_segundos} segundos equivalen a {cantidad_horas} horas.") 

#Actividad 6: Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número

numero = int(input("Ingresa un número: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11): #Me queda la duda de porque es el rango de (1, 11) y no (1,10). Si pongo (1,10) no me imprime el 10?? Es decir, se reduce hasta 9?? Entonces lo que calcula es 11-1???
    producto = numero * i
    print(f"{numero} x {i} = {producto}")
    
#Actividad 7: Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

n1 = int(input("Ingresa el primer número entero ≠ 0: "))
n2 = int(input("Ingresa el segundo número entero ≠ 0: "))
print(f"Los números ingresados son {n1} y {n2}")
print(f"Suma: {n1 + n2}")
print(f"Resta: {n1 - n2}")
print(f"Multiplicación: {n1 * n2}")
print(f"División: {n1 / n2}")

#Actividad 8: Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal

altura = float(input("Ingresa tu altura en metros (ej: 1.73): "))
peso = float(input("Ingresa tu peso en kilogramos (ej: 70.5): "))
imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal (IMC) es: {imc}") #Estaria bueno sumar una linea mas, en la que dependiendo el valor que obtenga te da una serie de recomendaciones o clasificaciones (bajo peso, peso normal, sobrepeso, obesidad, etc). Ni idea como se hace xD

#Actividad 9: Crear un programa que pida al usuario una temperatura en grados Celsius e imprima porpantalla su equivalente en grados Fahrenheit.

celsius = float(input("Ingresa una temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")

#Actividad 10:  Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

n_1 = float(input("Ingresa el primer número: "))
n_2 = float(input("Ingresa el segundo número: "))
n_3 = float(input("Ingresa el tercer número: "))   
promedio = (n_1 + n_2 + n_3) / 3
print(f"El promedio de los tres números es: {promedio}")

#Hay cosas que tuve que buscar en internet, porque en los materiales dados no se mencionaban.