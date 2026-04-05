#Actividad 1: Crear una lista con las notas de 10 estudiantes. 
    #● Mostrar la lista completa. 
    #● Calcular y mostrar el promedio. 
    #● Indicar la nota más alta y la más baja
Notas = [7.5, 8, 6, 9.5, 5, 8.5, 7, 6.5, 9, 10]
print("Notas del parcial: \n")
for i in range (10):
    print ("  Nota del estudiante", i+1, ":", Notas[i], "\n")

Promedio = sum(Notas) / len(Notas)
print ("Promedio de notas:", Promedio, "\n")

Nota_mas_alta = max(Notas)
Nota_mas_baja = min(Notas)
print (f"La nota mas alta es: {Nota_mas_alta} y la nota mas baja es: {Nota_mas_baja}")

#Actividad 2: Pedir al usuario que cargue 5 productos en una lista. 
    #● Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
    #● Preguntar al usuario qué producto desea eliminar y actualizar la lista.

Productos = []
for i in range (5):
    Producto = input("Ingrese el nombre del producto: ")
    Producto = Producto.capitalize()
    Productos.append(Producto)
    Productos_ordenados = sorted(Productos)
print ("Productos ordenados alfabéticamente: \n")
for i in range (5):
    print ("  Producto", i+1, ":", Productos_ordenados[i], "\n")    

#Eliminar uno de los productos 
Pregunta = input("¿Desea eliminar un producto? (si/no): ")
if Pregunta.lower() == "si":
    Producto_a_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
    if Producto_a_eliminar in Productos:
        Productos.remove(Producto_a_eliminar)
        print ("Producto eliminado. Lista actualizada: \n")
        for i in range (len(Productos)):
                print ("  Producto", i+1, ":", Productos[i], "\n")
    else:    
        input ("El producto no se encuentra en la lista, por favor ingrese un producto válido: ")

else: 
    print ("No se desea eliminar ningún producto de la lista.")


#Actividad 3:Generar una lista con 15 números enteros al azar entre 1 y 100. 
    #● Crear una lista con los pares y otra con los impares. 
    #● Mostrar cuántos números tiene cada lista

import random

Numeros = [random.randint(1, 100) for _ in range(15)] #Curioso descubrimiento el uso de "_" en el bucle for. 
Pares = [n for n in Numeros if n % 2 == 0]
Impares = [n for n in Numeros if n % 2 != 0]

print("Números generados:", Numeros, "\n")
print("Números pares:", Pares)
print("Cantidad de números pares:", len(Pares), "\n")
print("Números impares:", Impares)
print("Cantidad de números impares:", len(Impares), "\n")
#Uso mucho el"\n" porque considero que hace mucho mas comodo leer al usuario. 

#Actividad 4:Dada una lista con valores repetidos:
    #● Crear una nueva lista sin elementos repetidos. 
    #● Mostrar el resultado.

Datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
Lista_sin_repetidos = list(set(Datos)) #Esto lo tuve que buscar, no se me ocurrio una forma de hacerlo, y las ideas que tenia se me hacian muy extensas. 
print (f"Lista final: {Lista_sin_repetidos}")

#Actividad 5: Crear una lista con los nombres de 8 estudiantes presentes en clase. 
    #● Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
    #● Mostrar la lista final actualizada. 

Estudiantes_Presentes = ["Sol", "Marcos", "Luciana", "Fiorella", "Agustin", "Sofia", "Lucia", "Sasha"]
print ("Estudiantes presentes en clase: \n")
for i in range (len(Estudiantes_Presentes)):
    print ("  Estudiante", i+1, ":", Estudiantes_Presentes[i], "\n")
while True:
    Pregunta = input ("¿Queres agregar un nuevo estudiante o elimnar uno existente? Agregar (1) Eliminar (2) Esc (3): ")

    if Pregunta == "1":
        Nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
        Nuevo_estudiante = Nuevo_estudiante.capitalize()
        Estudiantes_Presentes.append(Nuevo_estudiante)
        print ("Estudiante agregado. Lista actualizada: \n")
        for i in range (len(Estudiantes_Presentes)):
            print ("  Estudiante", i+1, ":", Estudiantes_Presentes[i], "\n")

    #Aca para que no termine de ejecutarse el programa cuando ponen mal el nombre del estudiante a eliminar, hice un bucle while que se repite hasta que el usuario ingrese un nombre correcto.
    elif Pregunta == "2":
        Estudiante_a_eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ")
        while Estudiante_a_eliminar not in Estudiantes_Presentes:
            Estudiante_a_eliminar = input("El estudiante no se encuentra en la lista, por favor ingrese un estudiante válido: ")
        Estudiantes_Presentes.remove(Estudiante_a_eliminar)
        print ("Estudiante eliminado. Lista actualizada: \n")
        for i in range (len(Estudiantes_Presentes)):
            print ("  Estudiante", i+1, ":", Estudiantes_Presentes[i], "\n")   

    elif Pregunta == "3":
        print ("No se desea realizar ninguna acción.")
        break

    else:
        print ("Opción no válida, por favor ingrese una opción correcta: ")

#Actividad 6: Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero). 

Numeros = [2, 69, 8, 22, 25, 96, 666]
print ("Lista original:", Numeros, "\n")
Ultimo_numero = Numeros[-1]
for i in range (len(Numeros)-1, 0, -1):
    Numeros[i] = Numeros[i-1]
Numeros[0] = Ultimo_numero
print ("Lista rotada hacia la derecha:", Numeros)
#Actividad 7: Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana. 
    #● Calcular el promedio de las mínimas y el de las máximas. 
    #● Mostrar en qué día se registró la mayor amplitud térmica

print ("Temperaturas de esta semana: \n")
Temperaturas =[
    [31, 22], 
    [23, 12], 
    [13, 12], 
    [15, 13], 
    [19, 13], 
    [25, 17], 
    [28, 18]
    ]

for fila in Temperaturas:
    print(fila)
print()

Minimas = [Temperaturas[i][1] for i in range (len(Temperaturas))]
Maximas = [Temperaturas[i][0] for i in range (len(Temperaturas))]
Promedio_minimas = sum(Minimas) / len(Minimas)  
Promedio_maximas = sum(Maximas) / len(Maximas)  

print (f"Promedio de temperaturas mínimas: {Promedio_minimas:.2f} \n")
print (f"Promedio de temperaturas máximas: {Promedio_maximas:.2f} \n")

Mayor_amplitud = 0
Dia_mayor_amplitud = 0
for i in range (len(Temperaturas)):
    Amplitud = Temperaturas[i][0] - Temperaturas[i][1]
    if Amplitud > Mayor_amplitud:
        Mayor_amplitud = Amplitud
        Dia_mayor_amplitud = i + 1
        
#Generamos los dias de la semana
    if Dia_mayor_amplitud == 1:
        Dia_mayor_amplitud = "Lunes"
    elif Dia_mayor_amplitud == 2:
        Dia_mayor_amplitud = "Martes"   
    elif Dia_mayor_amplitud == 3:
        Dia_mayor_amplitud = "Miércoles"
    elif Dia_mayor_amplitud == 4:
        Dia_mayor_amplitud = "Jueves"
    elif Dia_mayor_amplitud == 5:
        Dia_mayor_amplitud = "Viernes"
    elif Dia_mayor_amplitud == 6:
        Dia_mayor_amplitud = "Sábado"
    elif Dia_mayor_amplitud == 7:
        Dia_mayor_amplitud = "Domingo"  

print (f"Mayor amplitud térmica: {Mayor_amplitud} \n")
print (f"Día con mayor amplitud térmica: {Dia_mayor_amplitud} \n")  
#Actividad 8: Crear una matriz con las notas de 5 estudiantes en 3 materias. 
    #● Mostrar el promedio de cada estudiante. 
    #● Mostrar el promedio de cada materia.


import random

Estudiantes = 5  #Filas
Materias = 3     #Coiumnas
#Podria ser al revez, pero como hago mis registros por estudiante, me parecio mas comodo asi.

Notas = [[0] * Materias for _ in range (Estudiantes)]

for i in range (Estudiantes):
    for j in range (Materias):
        Notas[i][j] = random.randint(1, 10) #Genero notas al azar entre 1 y 10 para cada estudiante y materia.

print("\nNotas de los estudiantes: \n")
for i in range (Estudiantes):
    print(f"  Estudiante {i+1}: {Notas[i]} \n")

#Promedio de cada estudiante.
print ("-------Promedio de cada estudiante------- \n")
for i in range (Estudiantes):
    Promedio_estudiante = sum(Notas[i]) / Materias
    print (f"  Estudiante {i+1}: {Promedio_estudiante:.2f} \n") 

#Pmedio de cada materia.
print ("-------Promedio de cada materia------- \n")
for j in range (Materias):
    Promedio_materia = sum(Notas[i][j] for i in range (Estudiantes)) / Estudiantes
    print (f"  Materia {j+1}: {Promedio_materia:.2f} \n")

##Actividad 9: Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
#    #● Inicializarlo con guiones "-" representando casillas vacías. 
#    #● Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
#    #● Mostrar el tablero después de cada jugada


Filas = 3
Columnas = 3
Tablero = [["-"] * Columnas for _ in range(Filas)]
Turno = 0

for Movimiento in range(9):
    jugador = "X" if Turno % 2 == 0 else "O"
    print(f"Turno de {jugador}")

    while True:
        Fila = int(input("Ingrese fila (1-3): ")) - 1
        Columna = int(input("Ingrese columna (1-3): ")) - 1
        print()

        if Fila < 0 or Fila >= Filas or Columna < 0 or Columna >= Columnas:
            print("Posición inválida. Debe ser entre 1 y 3.")
        elif Tablero[Fila][Columna] != "-":
            print("Esa casilla ya está ocupada. Elige otra.")
        else:
            break

    Tablero[Fila][Columna] = jugador

    for fila_tablero in Tablero:
        for celda in fila_tablero:
            print(celda, end=" ")
        print()
    print()

    Turno += 1

print("Juego terminado.")
#Lo que me costo sacar este, no se me venian las ideas. Pero buen resultado. 
#Actividad 10: Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
    #● Mostrar el total vendido por cada producto. 
    #● Mostrar el día con mayores ventas totales. 
    #● Indicar cuál fue el producto más vendido en la semana.

import random
Productos = 4
Dias = 7
Ventas = [[0] * Dias for _ in range(Productos)]

for i in range(Dias):
    for j in range(Productos):
        Ventas[j][i] = random.randint(0, 999) 
        #Ventas[j][i] = int(input(f"Ingrese las ventas del producto {j+1} para el día {i+1}: ")) #Con esot lo podria hacer de manera mnaul. 

#Total de ventas de cada producto.
print("\nTotal vendido por cada producto: \n")
for j in range(Productos):
    Total_producto = sum(Ventas[j][i] for i in range(Dias))
    print(f"  Producto {j+1}: {Total_producto} \n")

#Producto más vendido en la semana.
Total_ventas_producto = [sum(Ventas[j][i] for i in range(Dias)) for j in range(Productos)]
Producto_mas_vendido = Total_ventas_producto.index(max(Total_ventas_producto)) + 1
print(f"  Producto más vendido en la semana: Producto {Producto_mas_vendido} \n")

#Dia con mayores ventas totales.
Total_ventas_dia = [sum(Ventas[j][i] for j in range(Productos)) for i in range(Dias)]
Dia_mayores_ventas = Total_ventas_dia.index(max(Total_ventas_dia)) + 1
if Dia_mayores_ventas == 1:
    Dia_mayores_ventas = "Lunes"
elif Dia_mayores_ventas == 2:
    Dia_mayores_ventas = "Martes"  
elif Dia_mayores_ventas == 3:  
    Dia_mayores_ventas = "Miércoles"
elif Dia_mayores_ventas == 4:
    Dia_mayores_ventas = "Jueves"
elif Dia_mayores_ventas == 5:
    Dia_mayores_ventas = "Viernes"
elif Dia_mayores_ventas == 6:
    Dia_mayores_ventas = "Sábado"
elif Dia_mayores_ventas == 7:
    Dia_mayores_ventas = "Domingo"
print(f"  Día con mayores ventas totales: Día {Dia_mayores_ventas} \n")
#Actividad 11:  Crear una lista con los nombres de 10 estudiantes. 
    #● Solicitar al usuario que ingrese un nombre a buscar. 
    #● Indicar si el nombre se encuentra en la lista. 
    #● Mostrar la posición en la que aparece. 
    #● Si no se encuentra, informar que no está en la lista. 

Nombres = [
    "Sofia",
    "Agustina",
    "Luaciana",
    "Fiorella",
    "Marcos",
    "Sasha",
    "Lucia",
    "Francisco",
    "Federico",
    "Agustin"
]
print ("Lista de estudiantes: \n")
for i in range (len(Nombres)):
    print ("  Estudiante", i+1, ":", Nombres[i], "\n")

Nombre_a_buscar = input("Ingrese el nombre del estudiante a buscar: ")
if Nombre_a_buscar in Nombres:
    Posicion = Nombres.index(Nombre_a_buscar) + 1
    print (f"El nombre {Nombre_a_buscar} se encuentra en la lista en la posición {Posicion}.")
else:
    print (f"El nombre {Nombre_a_buscar} no se encuentra en la lista.")

#Actividad 12:  Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista. 
    #● Mostrar la lista original. 
    #● Mostrar la lista ordenada de menor a mayor. 
    #● Mostrar la lista ordenada de mayor a menor. 
    #● Investigar el uso de sorted() y del parámetro reverse. 

Numeros = []
for i in range (8):
    Numero = int(input("Ingrese un número entero: "))
    Numeros.append(Numero)

#def bubble_sort_asc(lista):
#    n = len(lista)
#    for i in range(n):
#        for j in range(n - i - 1):
#            if lista[j] > lista[j + 1]:
#                lista[j], lista[j + 1] = lista[j + 1], lista[j]
#    return lista

#def bubble_sort_desc(lista):
#    n = len(lista)
#    for i in range(n):
#        for j in range(n - i - 1):
#            if lista[j] < lista[j + 1]:
#                lista[j], lista[j + 1] = lista[j + 1], lista[j]
#    return lista

#numeros_asc = bubble_sort_asc(Numeros.copy())
#numeros_desc = bubble_sort_desc(Numeros.copy())

#print("Lista ordenada de menor a mayor:", numeros_asc)
#print("Lista ordenada de mayor a menor:", numeros_desc)

print("Lista original:", Numeros)
print("Lista ordenada de menor a mayor:", sorted(Numeros))
print("Lista ordenada de mayor a menor:", sorted(Numeros, reverse=True)) 
##Es mucho mas corto, queda mas limpio, y es mas eficiente que el bubble sort. 

#Actividad 13; Dada la siguiente lista de puntajes de un videojuego: 
    #● Mostrar el puntaje más alto y el más bajo. 
    #● Mostrar la lista ordenada de mayor a menor (ranking). 
    #● Indicar en qué posición del ranking se encuentra el puntaje 990.

Puntajes = [450, 1200, 875, 990, 300, 1500, 640] 
print("Puntajes del videojuego:", Puntajes, "\n")
Puntaje_mas_alto = max(Puntajes)
Puntaje_mas_bajo = min(Puntajes)
print (f"Puntaje más alto: {Puntaje_mas_alto} \n")
print (f"Puntaje más bajo: {Puntaje_mas_bajo} \n")
Puntajes_ordenados = sorted(Puntajes, reverse=True)
print("Ranking de puntajes (de mayor a menor):", Puntajes_ordenados, "\n")
if 990 in Puntajes_ordenados:
    Posicion_990 = Puntajes_ordenados.index(990) + 1
    print (f"El puntaje 990 se encuentra en la posición {Posicion_990} del ranking.")

#Buen trabajo, se me hizo medio largo, pero se descubrieron cosas nuevas, tengo algunas dudas aun, pero cuando haga mis apuntes seguro las soplo.