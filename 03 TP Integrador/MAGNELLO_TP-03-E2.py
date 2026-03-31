#Objetivo: Login con intentos + menú de acciones con validación estricta. 
#Requisitos 
#1. Definir credenciales fijas en el código: 
    #o usuario correcto: "alumno" 
    #o clave correcta: "python123" 
#2. Permitir máximo 3 intentos para ingresar usuario y clave. 
#3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar. 
#4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir: 
    #1. Ver estado de inscripción (mostrar “Inscripto”) 
    #2. Cambiar clave (pedir nueva clave y confirmación; deben coincidir) 
    #3. Mostrar mensaje motivacional (1 frase) 
    #4. Salir 
    #5. Validación del menú: 
        #o Debe ser número (.isdigit()) 
        #o Debe estar entre 1 y 4

Usuario_correcto = "alumno"
Clave_correcta = "python123"    
Intentos = 0

while Intentos < 3:
    Usuario_ingresado = input("Ingrese su usuario: ")
    print()
    Clave_ingresada = input("Ingrese su clave: ")
    
    if Usuario_ingresado == Usuario_correcto and Clave_ingresada == Clave_correcta:
        print("¡Bienvenido!")
        print() 
        while True:
            print("Menú:")   
            print()         
            print("1. Ver estado de inscripción")
            print("2. Cambiar clave")
            print("3. Mostrar mensaje motivacional")
            print("4. Salir")
            print()
            Opcion = input("Seleccione una opción (1-4): ")
            
            if Opcion.isdigit() and 1 <= int(Opcion) <= 4:
                Opcion = int(Opcion)
                if Opcion == 1:
                    print("Estado de inscripción: Inscripto")
                elif Opcion == 2:
                    Nueva_clave = input("Ingrese la nueva clave: ")
                    if len(Nueva_clave) < 6:
                        print("La clave debe tener al menos 6 caracteres. Intente nuevamente.")
                    Confirmacion_clave = input("Confirme la nueva clave: ")
                    if Nueva_clave == Confirmacion_clave:
                        Clave_correcta = Nueva_clave
                        print("Clave cambiada exitosamente.")
                    else:
                        print("Las claves no coinciden. Intente nuevamente.")
                elif Opcion == 3:
                    print("Viaje antes que destino, disfruta el proceso.")
                elif Opcion == 4:
                    print("¡Nos vemos!")
                    break
            else:
                print("Opción inválida. Por favor, seleccione un número entre 1 y 4.")
        break
    else:
        Intentos += 1
        print(f"Credenciales incorrectas. Intento {Intentos} de 3.")


#Creo que acabo de usar la peor opcion para aumentar la separacion de lineas entre cada printeo, use print() pero no se si es correcto.
#Seguro que existe otra forma, pero no se me ocurre ahora mismo.  