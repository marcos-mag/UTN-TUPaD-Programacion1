#1. Descripción del Escenario  Vas a desarrollar un simulador de batalla por turnos en Python. El programa enfrentará a un usuario (Gladiador) contra un oponente controlado por la computadora (Enemigo). 
# El objetivo es reducir los puntos de vida del oponente a cero antes de que él lo haga contigo. Este ejercicio evalúa el uso de variables (int, float, string, boolean), estructuras de control (if/elif/else), ciclos (while y for) y validación de datos estricta. 

#2. Requerimientos Técnicos  
# A. Tipos de Datos  
#Debes utilizar obligatoriamente los siguientes tipos de datos para las variables del juego:  
    # • String: Para el nombre del jugador.  
    # • Int: Para los Puntos de Vida (HP) y cantidad de pociones.  
    # • Float: Para el cálculo del daño (ej: un golpe crítico multiplica el ataque por 1.5). 
    # • Boolean: Para controlar si el juego sigue activo o quién tiene el turno.  
#B. Reglas de Validación (¡Importante!)  
    #• No está permitido usar bloques try / except.  
    #• Para validar texto, debes usar el método .isalpha() dentro de un ciclo while.  
    #• Para validar números, debes usar el método .isdigit() dentro de un ciclo while.}

#3. Flujo del Programa  
    # Paso 1: Configuración del Personaje   --
        #El programa inicia pidiendo el nombre del Gladiador.  --  
        #Validación: El nombre solo puede contener letras. Si el usuario ingresa números, símbolos o lo deja vacío, el programa debe decir "Error: Solo se permiten letras" y volver a preguntar hasta que sea válido.  
    #Paso 2: Inicialización de Estadísticas --
    #El programa debe definir las variables iniciales (sin preguntar al usuario):  
        #• Vida del Gladiador: 100 (int)  
        #• Vida del Enemigo: 100 (int)  
        #• Pociones de Vida: 3 (int)  
        #• Daño base "Ataque Pesado": 15 (int)  
        #• Daño base del enemigo: 12 (int)  
        #• Turno Gladiador : True (booleano)
    #Paso 3: El Ciclo de Combate  
    #El juego entra en un ciclo que se repite mientras ambos combatientes tengan más de 0 puntos de vida. --
    #Turno del Jugador:  
        #Muestra la vida actual de ambos y las pociones restantes. Luego, ofrece un menú con 3 opciones:  --
            #1. Ataque Pesado  
            #2. Ráfaga Veloz (Requiere uso de for)  
            #3. Curar  
        #Validación del Menú: El programa debe pedir la opción al usuario. --
            #1. Verificar que lo ingresado sea un número (.isdigit()).  
            #2. Verificar que el número sea 1, 2 o 3.  
            #Si falla alguna validación, mostrar mensaje de error y volver a pedir.

#Lógica de las Acciones:  
    #Acción A: Ataque Pesado (Opción 1)  --
        #Calcula el daño final. Si la vida del enemigo es menor a 20 puntos, el jugador realiza un "Golpe Crítico" multiplicando su daño base por 1.5 (resultado float).  
        #Resta el daño a la vida del enemigo.  
        #Muestra un mensaje: "¡Atacaste al enemigo por X puntos de daño!"  

    #Acción B: Ráfaga Veloz (Opción 2)  --
        #Esta acción realiza una serie de golpes rápidos. Debes implementar un bucle for.  
        #El bucle debe repetirse 3 veces (usando range).  
        #Dentro del bucle, en cada repetición: 
            #1. Resta 5 puntos de daño a la vida del enemigo.  
            #2. Muestra el mensaje: " > Golpe conectado por 5 de daño".  

    #Acción C: Curar (Opción 3)  --
        #Si tienes pociones (> 0): Suma 30 puntos a tu vida y resta 1 poción.  
        #Si NO tienes pociones: Muestra "¡No quedan pociones!" y pierdes el turno (el enemigo ataca igual).  

    #Turno del Enemigo:  --
    #Justo después de tu acción, el enemigo ataca automáticamente.  
        #Resta el daño base del enemigo (12) a tu vida.  
        #Muestra un mensaje: "¡El enemigo te atacó por 12 puntos de daño!"  
    #Paso 4: Fin del Juego  
    #Cuando el ciclo termine (porque la vida de alguno llegó a 0 o menos), debes evaluar:  
        #Si vida_jugador > 0: Mostrar "¡VICTORIA! [Nombre] ha ganado la batalla."  
        #Si vida_jugador <= 0: Mostrar "DERROTA. Has caído en combate."

Hp_Gladiador = 100
Hp_Enemigo = 100
Pociones_de_Vida = 3
Daño_base_Ataque_Pesado = 15
Daño_base_Enemigo = 12
Turno_Gladiador = True 

print("======= BIENVENIDO AL ELISEO =======")
Nombre_Gladiador = input("Ingresa el nombre de tu Gladiador: ")
while not Nombre_Gladiador.isalpha():
    Nombre_Gladiador = input("Error: Solo se permiten letras. Por favor ingresa un nombre válido: ")
print("======= INICIO DEL COMBATE =======\n")
while Hp_Gladiador > 0 and Hp_Enemigo > 0:
    if Turno_Gladiador:
        print(f"{Nombre_Gladiador} (HP:{Hp_Gladiador}) VS. Aquiles (HP:{Hp_Enemigo}) | Pociones restantes: {Pociones_de_Vida}\n")
        print("Elige tu acción:\n")
        print("  1. Ataque Pesado")
        print("  2. Ráfaga Veloz")
        print("  3. Curar\n")
        
        Opcion = input("Ingresa el número de tu acción: ")
        
        while not Opcion.isdigit() or int(Opcion) not in [1, 2, 3]: #Me gusta mas esta forma de poner las variantes disponibles, antes venia usando > o <. Consideero que es depende de lo que busco, pero otra cosa mas que descubri.
            print("Error: Opción inválida. Por favor ingresa 1, 2 o 3.")
            Opcion = input("Ingresa el número de tu acción: ")
        
        Opcion = int(Opcion)

#Golpe Pesado.        
        if Opcion == 1:
            Daño_final = Daño_base_Ataque_Pesado
            if Hp_Enemigo < 20:
                Daño_golpe_critico = float(Daño_base_Ataque_Pesado * 1.5)
                Hp_Enemigo -= Daño_golpe_critico
                print(f"¡JACKPOT! ¡Golpe critico! Le inflinjiste al enemigo {Daño_golpe_critico:.2f} puntos de daño\n")
            else:  #Aca tenia puesto un continue, no se cuanto tarde en darme cuenta que me estaba haciendo macana esa primera elleccion jhajajajaja
                Hp_Enemigo -= Daño_final
                print(f"¡Atacaste al enemigo por {Daño_final} puntos de daño!\n")

#Rafaga Veloz.        
        elif Opcion == 2:
            for i in range(3):
                Hp_Enemigo -= 5
                print(" > Golpe conectado por 5 de daño")

#Poti de vida
        elif Opcion == 3:
            if Pociones_de_Vida > 0:
                Hp_Gladiador += 30
                Pociones_de_Vida -= 1
                print("¡Te has curado por 30 puntos de vida!")
            else:
                print("¡No quedan pociones! Pierdes el turno.")
        
        Turno_Gladiador = False

#Turno de Aquiles. Estaria grasioso sumarle alguna variante para que no solo golpee por 15. 
    else:
        Hp_Gladiador -= Daño_base_Enemigo
        print(f"¡El enemigo te atacó por {Daño_base_Enemigo} puntos de daño!\n")
        Turno_Gladiador = True
        if Hp_Gladiador > 0 and Hp_Enemigo > 0:
            print("======= NUEVO TURNO =======\n")

#Fin del juego. 
if Hp_Gladiador > 0 and Hp_Enemigo <=0:
    print(f"VICTORIA - {Nombre_Gladiador} a ganado el combate")
elif Hp_Gladiador <=0:
    print (f"DERROTA - {Nombre_Gladiador} a caido en batalla")


#Ultima actividad, muy entretenida, me llevo unas 3-4 horas hacerlo y ver que todo este bien (Si es que lo esta)
#Me gusto mucho, me entretuve bastante y creo que el resultado fue bueno.
#Me pongo a la espera de la devolucion 
