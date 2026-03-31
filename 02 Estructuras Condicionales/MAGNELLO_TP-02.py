#Actividad 1: Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

edad = int(input("Por favor, ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Que haces en este sitio?")

#Actividad 2: Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”

nota = float(input("Por favor, ingrese su nota: ")) # "FLOAT" para permitir notas con decimales.
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Acticidad 3:  Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par

numero = int(input("Por favor, ingrese un número par: "))
if numero % 2 == 0:         #Entiendo que lo que se esta haceindo en esta linea, es dividir el numero ingresado por 2 y ver si el resto es 0. Correcto?
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Actividad 4: Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de lassiguientes categorías pertenece: "Niño/a: menor de 12 años. - Adolescente: mayor o igual que 12 años y menor que 18 años - Adulto/a joven: mayor o igual que 18 años y menor que 30 años - Adulto/a: mayor o igual que 30 años."

edad = int(input("Por favor, ingrese su edad: "))
if edad < 12: 
    print("Niño/a")
elif 12 <= edad < 18: #Si pongo directamente edad <18 estarian bien, no? ya que el 12 estaria contenido aqui tambien. 
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a") 

#Actividad 5: Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"

contraseña = input("Por favor, ingrese una contraseña (entre 8 y 14 caracteres): ")
longitud = len(contraseña)
if 8 <= longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Actividad 6: Escribir un programa que solicite al usuario el consumo mensual de energía eléctrica en kilovatios (kWh) e indique la categoría del consumo según el siguiente criterio: Menor que 150 kWh: “Consumo bajo” - Entre 150 y 300 kWh (inclusive): “Consumo medio”. - Mayor que 300 kWh: “Consumo alto”. Además, si el consumo supera los 500 kWh, mostrar un mensaje adicional que diga: “Considere medidas de ahorro energético”. El programa debe imprimir por pantalla la categoría correspondiente.

consumo = float(input("Por favor, ingrese su consumo mensual de energía eléctrica en kWh: "))
if consumo < 150:
    print("Consumo bajo")   
elif 150 <= consumo <= 300:
    print("Consumo medio")
elif consumo > 300:
    print("Consumo alto")
    if consumo > 500:
        print("Considere medidas de ahorro energético")

#Actividad 7:  Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla. 

entrada = input("Por favor, ingrese una frase o palabra: ")
if entrada[-1] in ("AEIOUaeiou"):
    print(f"{entrada}!")
else:
    print(entrada)

#Acticidad 8: Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. - 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. - 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 

nombre = input("Por favor, ingrese su nombre: ")
opcion = int(input("1 - Nombre en mayúsculas, 2 - Nombre en minúsculas, 3- Primera letra mayúscula: "))
#if opcion == 1:
#    print(nombre.upper())      
#elif opcion == 2:
#    print(nombre.lower())
#elif opcion == 3:
#    print(nombre.capitalize())
#else:
#    print("Opción no válida, por favor ingrese 1, 2 o 3.")

if opcion == 1:
    nombre_mayusculas = nombre.upper()
    print(nombre_mayusculas)
elif opcion == 2:
    nombre_minusculas = nombre.lower()
    print(nombre_minusculas)
elif opcion == 3:
    nombre_title = nombre.title()
    print(nombre_title)
else:
    print("Opción no válida, por favor ingrese 1, 2 o 3.")

#Actividad 9: Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:

magnitud = float(input("Por favor, ingrese la magnitud del terremoto en la escala de Richter: "))
if magnitud < 3:
    print("Muy leve (inperceptable).")   
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
elif 7 <= magnitud:
    print("Extremo (puede causar graves daños a gran escala).")

#Actividad 10: Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano
hemisferio = input("Por favor, ingrese en cuál hemisferio se encuentra (N/S): ")
hemisferio = hemisferio.upper()  #Convertir a mayusculas para evitar errores de ingreso.
mes = int(input("Por favor, ingrese el mes del año (1-12): "))
dia = int(input("Por favor, ingrese el día del mes en números: "))
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or(mes in (1,2)) or (mes == 3 and dia <=20):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <=20):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <=20):
        print("Verano")
    elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <=20):
        print("Otoño")
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or(mes in (1,2)) or (mes == 3 and dia <=20):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <=20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <=20):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <=20):
        print("Primavera")
