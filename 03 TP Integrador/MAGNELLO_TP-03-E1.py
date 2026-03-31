#E1-Caja-del-kiosco
#Objetivo: Simular una compra con validaciones y cálculo de total. 
#Requisitos:  
    #1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while). 
    #2. Pedir cantidad de productos a comprar (número entero positivo, validar con .isdigit() en while). 
    #3. Por cada producto (usar for): 
        #o Pedir precio (entero, validar .isdigit()). 
        #o Pedir si tiene descuento S/N (validar con while, aceptar s o n en cualquier mayuscula/minuscula). 
        #o Si tiene descuento: aplicar 10% al precio de ese producto. 
    #4. Al final mostrar:  
        #o Total sin descuentos 
        #o Total con descuentos 
        #o Ahorro total 
        #o Promedio por producto (usar float y formatear con :.2f, ejem: x = 3.14159 print(f"{x:.2f}")) 
#Validaciones obligatorias 
    #• Sin try/except. 
    #• No aceptar vacío en nombre (si queda vacío, es error). 
    #• Cantidad > 0 (si ingresa 0, volver a pedir). 

#Primero pedimos el nombre del cliente..

Cliente = input("Ingrese el nombre del Cliente: ")
while not Cliente.isalpha() or Cliente == "":
    print("Error: El nombre debe contener solo letras y no puede estar vacío.") #La consigna se referia a esto con "No aceptar vacio en nombre (si queda vacio, es error)". Verdad? o fue una mala interpretacion mia?
    Cliente = input("Ingrese el nombre del Cliente: ")

#Ahora toca lo relacionado a los productos. Cantidad, precio, descuento. 
Producto = 0

Cantidad_productos = input("Ingrese la cantidad de productos a comprar: ")
while not Cantidad_productos.isdigit() or int(Cantidad_productos) <= 0:
    print("Error: La cantidad debe ser un número entero positivo.")
    Cantidad_productos = input("Ingrese la cantidad de productos a comprar: ")
Cantidad_productos = int(Cantidad_productos)

Total_sin_descuento = 0
Total_con_descuento = 0

productos_info = ""  #No se me ocurrio otra forma de poder hacer esto, osea si, podia haber usado listas, pero aun no trabajamos ese concepto. 

for i in range(1, Cantidad_productos + 1):
    Precio_producto = input(f"Ingrese el precio del producto {i}: ")
    while not Precio_producto.isdigit():
        Precio_producto = input(f"Error, Ingrese un precio valido {i}: ")
    Precio_producto = int(Precio_producto)

    Descuento = input(f"¿El producto {i} tiene descuento? (S/N): ")
    Descuento = Descuento.lower()
    while Descuento != "s" and Descuento != "n":
        Descuento = input(f"Error, ¿El producto {i} tiene descuento? (S/N): ")
        Descuento = Descuento.lower()
    
    # :O
    productos_info += f"Producto {i} - Precio: ${Precio_producto:.2f} - Descuento: {'Sí' if Descuento == 's' else 'No'}"
    
    Total_sin_descuento += Precio_producto    

    if Descuento == "s":
        Precio_con_descuento = Precio_producto * 0.9  
    else:
        Precio_con_descuento = Precio_producto
    
    Total_con_descuento += Precio_con_descuento

Ahorro = Total_sin_descuento - Total_con_descuento
Promedio = Total_con_descuento / Cantidad_productos

print (f"Cliente: {Cliente}")
print (f"Cantidad de productos: {Cantidad_productos}")
print(productos_info)
print (f"Total sin descuentos: ${Total_sin_descuento:.2f}")
print (f"Total con descuentos: ${Total_con_descuento:.2f}")
print (f"Ahorro total: ${Ahorro:.2f}")
print (f"Promedio por producto: ${Promedio:.2f}")


#Tengo muchas dudas, por lo pronto lo mas prudente que se me ocurrio fue ir paso a paso y trabajar las cosas por secciones, pero no se si es la mejor forma de hacerlo. 
#Por lo pronto, creo que es un buen inicio (No se cuantas horas llevo con esto, pero quedo jajajaja)
