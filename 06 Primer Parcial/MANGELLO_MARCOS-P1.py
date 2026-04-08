#Contexto del Problema: Una ferretería local necesita digitalizar el control de sus productos para evitar pérdidas de
#stock. Actualmente, manejan sus datos de forma manual y requieren un programa que permita gestionar las herramientas a la venta y 
#sus unidades disponibles en tiempo real.

###############################################################################################################################################################
#Requerimientos Técnicos (Restricciones Estrictas):
#Estructuras permitidas: 
# Solo se pueden utilizar estructuras secuenciales, condicionales (if, elif, else), bucles (while, for) y la estructura de selección para el menú.
#Estructura de Datos: 
# Uso exclusivo de listas paralelas (herramientas[] y existencias[]). La sincronía por índice debe mantenerse en todo momento: existencias[i] pertenece a herramientas[i]
#Prohibiciones: No se permite el uso de funciones (def), clases, diccionarios, excepciones (try/except) ni estructuras de datos avanzadas
##################################################################################################################################################################

#Funcionalidades del Menú
#El programa debe presentar un menú interactivo persistente con las siguientes opciones:

    #1. Carga Inicial de Herramientas: Registrar los nombres de las herramientas que se pondrán a la venta. Se debe preguntar al usuario la cantidad de herramientas a cargar
    #y se debe usar una estructura pertinente. En caso de nombre vacío o duplicado se debe seguir pidiendo hasta que sea correcto respetando la cantidad de herramientas
    #que el usuario indicó antes de la carga.

    #2. Carga de Existencias: Ingresar la cantidad de unidades para cada herramienta registrada previamente, respetando el orden de ingreso. Cuando el usuario ingresa
    #existencias, el sistema debe mostrar por pantalla el nombre de la herramienta.

    #3. Visualización de Inventario: Mostrar el listado completo de herramientas junto a su stock actual.

    #4. Consulta de Stock (existencias): Buscar una herramienta por su nombre y mostrar cuántas unidades hay disponibles.

    #5. Reporte de Agotados: Listar únicamente aquellos productos cuyo stock sea igual a cero.

    #6. Alta de Nuevo Producto: Permitir agregar solo una nueva herramienta al final de las listas con su stock inicial. En caso de nombre vacío, nombre duplicado o valor de
    #existencia negativo se debe volver al menú principal mostrando por pantalla el motivo

    #7. Actualización de Stock (Venta/Ingreso):
        #Venta: Disminuir el stock tras validar que hay unidades suficientes.
        #Ingreso: Aumentar el stock por reposición de mercadería.

    #8. Salir: Finalizar la ejecución del sistema.

#####################################################################################################################################################################################
#Criterios de Validación (Robustez)
#El sistema debe ser "a prueba de errores" comunes:
    #● No permitir nombres de herramientas vacíos ni duplicados.
    #● No permitir ingresar existencias (opción 2 del menú) sin tener nombres de herramientas cargadas (opción 1)
    #● Validar que las existencias ingresadas sean números enteros positivos o cero.
    #● Impedir ventas que superen el stock disponible (no se permiten saldos negativos).
    #● Informar mediante un mensaje claro si se intenta operar sobre una herramienta que no existe en el catálogo.
#####################################################################################################################################################################################

Herremientas = []
Existencias = []

#Menu principal.  Me gustaria saber si existe una manera de que esto no se printee en todas las pantallas. Que tuviera que elegir una opcion para volver a el. 
while True:
    print()
    print("============================================================ \n")
    print("Menú:")
    print()
    print("  1. Carga Inicial de Herramientas")
    print("  2. Carga de Existencias")
    print("  3. Visualización de Inventario")
    print("  4. Consulta de Stock")
    print("  5. Reporte de Agotados")
    print("  6. Alta de Nuevo Producto")
    print("  7. Actualización de Stock (Venta/Ingreso)")
    print("  8. Salir")
    print()
    print("============================================================ \n")

    Opcion = input("Seleccione una opción (1-8): ")
    print()

#La carga de herramientas (Solo su nombre).
    if Opcion == "1":
        Cantidad_herramientas = input("Ingrese la cantidad de herramientas a cargar: ")
        print()
        if Cantidad_herramientas.isdigit() and int(Cantidad_herramientas) > 0:  #En esta linea me aseguro de que el usuario ingrese un numero y de que este sea entero positivo.
            Cantidad_herramientas = int(Cantidad_herramientas)
            for i in range(Cantidad_herramientas):
                while True:
                    Nombre_herramienta = input(f"Ingrese el nombre de la herramienta {i+1}: ").capitalize()
                    if Nombre_herramienta and Nombre_herramienta not in Herremientas:
                        Herremientas.append(Nombre_herramienta)
                        Existencias.append(0)  
                        break
                    else:
                        print("Nombre inválido o duplicado. Intente nuevamente.")
        else:
            print("Cantidad inválida. Debe ser un número entero positivo.")

#En un primer momento lo hice "mal", interprete el enunciado de otra manera e hice el punto 1 y 2 juntos, porque pedia el nombre del objeto 
#y luego la cantidad del mismo, pero lo cambie al releer el enunciado.

#Carga de existencias.
    elif Opcion == "2":
        if not Herremientas:
            print("No hay herramientas cargadas. Por favor, cargue herramientas primero (opción 1).")
        else:
            for i in range(len(Herremientas)):
                while True:
                    Cantidad = input(f"Ingrese la cantidad para {Herremientas[i]}: ")
                    if Cantidad.isdigit() and int(Cantidad) >= 0:   #Nuevamente uso el mismo metodo, para ver que se haya ingresado un numero entero positivo. 
                        Existencias[i] = int(Cantidad)  #Actualizo la cantidad, por si ya habia. ¿Se sumara? Tengo que ver
                        break
                    print("Cantidad inválida. Debe ser un número entero positivo o cero.")

#Visualización de inventario.
    elif Opcion == "3":
        if not Herremientas:
            print("No hay herramientas cargadas. Por favor, cargue herramientas primero (opción 1).")
        else:
            print("Inventario:\n")
            for i in range(len(Herremientas)):
                print(f"  {Herremientas[i]}: {Existencias[i]} unidades")

#Consulta de stock.
    elif Opcion == "4":
        if not Herremientas:
            print("No hay herramientas cargadas. Por favor, cargue herramientas primero (opción 1).")
        else:
            Nombre_consulta = input("Ingrese el nombre de la herramienta a consultar: ")
            Nombre_consulta = Nombre_consulta.capitalize()
            if Nombre_consulta in Herremientas:
                index = Herremientas.index(Nombre_consulta)  #Con index, me da el indice de la herramienta y con eso, despues puedo mostrar la cantidad de unidades de esa misma.
                print(f"Stock disponible de {Nombre_consulta}: {Existencias[index]} unidades")
            else:
                print("La herramienta no existe en el catálogo.")

#Reporte de agotados.
    elif Opcion == "5":
        if not Herremientas:
            print("No hay herramientas cargadas. Por favor, cargue herramientas primero (opción 1).")
        else:
            print("Herramientas agotadas:\n")
            Agotados = False
            for i in range(len(Herremientas)):
                if Existencias[i] == 0:
                    print(f"  {Herremientas[i]}")
                    Agotados = True
            if not Agotados:
                print("No hay herramientas agotadas.")

#Alta de nuevo producto.
    elif Opcion == "6":
        while True:
            Nuevo_producto = input("Ingrese el nombre del nuevo producto: ").capitalize()
            if not Nuevo_producto:
                print("Nombre vacío. Volviendo al menú principal.")
                break
            elif Nuevo_producto in Herremientas:
                print("Nombre duplicado. Volviendo al menú principal.")
                break
            else:
                while True:
                    Stock_inicial = input("Ingrese las unidades disponibles del nuevo producto: ")
                    if Stock_inicial.isdigit() and int(Stock_inicial) >= 0:
                        Herremientas.append(Nuevo_producto)
                        Existencias.append(int(Stock_inicial))
                        print(f"Producto '{Nuevo_producto}' agregado, {Stock_inicial} unidades disponibles.")
                        break
                    else:
                        print("Valor de existencia inválido. Debe ser un número entero positivo o cero. Volviendo al menú principal.")
                        break
                break

#Actualización de stock (Venta/Ingreso).
    elif Opcion == "7":
        if not Herremientas:
            print("No hay herramientas cargadas. Por favor, cargue herramientas primero (opción 1).")
        else:
            Nombre_producto = input("Ingrese el nombre del producto a actualizar: ").capitalize()
            if Nombre_producto in Herremientas:
                index = Herremientas.index(Nombre_producto)
                while True:
                    Tipo_actualizacion = input("¿Desea realizar una venta (V) o un ingreso (I)? ").upper()
                    if Tipo_actualizacion == "V":
                        Cantidad_venta = input("Ingrese la cantidad a vender: ")
                        if Cantidad_venta.isdigit() and int(Cantidad_venta) > 0:
                            Cantidad_venta = int(Cantidad_venta)
                            if Cantidad_venta <= Existencias[index]:
                                Existencias[index] -= Cantidad_venta
                                print(f"Venta realizada. Stock actualizado de {Nombre_producto}: {Existencias[index]} unidades.")
                                break
                            else:
                                print("No hay suficientes unidades para realizar la venta.")
                        else:
                            print("Cantidad inválida. Debe ser un número entero positivo.")
                    elif Tipo_actualizacion == "I":
                        Cantidad_ingreso = input("Ingrese la cantidad de unidades a ingresar: ")
                        if Cantidad_ingreso.isdigit() and int(Cantidad_ingreso) > 0:
                            Existencias[index] += int(Cantidad_ingreso)
                            print(f"Ingreso realizado. Stock actualizado de {Nombre_producto}: {Existencias[index]} unidades.")
                            break
                        else:
                            print("Cantidad inválida. Debe ser un número entero positivo.")
                    else:
                        print("Opción inválida. Por favor, ingrese 'V' para VENTA o 'I' para INGRESO.")
            else:
                print("La herramienta no existe en el catálogo.")

    elif Opcion == "8":
        print("Saliendo del sistema. ¡Hasta la próxima!")
        print()
        break
