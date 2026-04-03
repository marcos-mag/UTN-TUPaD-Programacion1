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

if Pregunta.lower() == "no":
    pass


#Actividad 3: