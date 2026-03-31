#E4-Escape-Room. 
#• Pedir nombre del agente y validar con .isalpha() en un while. -
#• Validar opciones del menú y cualquier número pedido con .isdigit() en un while. 
#• El juego debe funcionar con estructuras secuenciales, condicionales y repetitivas (puede usar funciones propias del lenguaje como .lower(), len(), formateo, etc.)

#Regla anti-spam (muy importante) -
#Para evitar que el jugador gane eligiendo “Forzar cerradura” 3 veces seguidas al iniciar: 
    #✅ Si el jugador elige Forzar cerradura (opción 1) 3 veces seguidas, entonces: 
        #• se cobra el costo normal (-20 energía, -2 tiempo), 
        #• NO abre cerradura, y 
        #• se activa la alarma automáticamente (alarma = True) porque “la cerradura se trabó”. 
#Si el jugador elige opción 2 o 3, se corta la racha de “forzar seguidas”. - 

#Menú de acciones (se repite mientras el juego siga) 
#El juego continúa mientras: -
    #• energia > 0, tiempo > 0, cerraduras_abiertas < 3 
    #• y no esté bloqueado por alarma. 
#En cada turno mostrar el estado y el siguiente menú: -
    #1. Forzar cerradura (costo: -20 energía, -2 tiempo) 
        # Si la energía está por debajo de 40, hay “riesgo de alarma”: 
            #▪ pedir un número 1-3 (validado). Si elige 3 → alarma=True. 
        #o Si no hay alarma, abre 1 cerradura. 
        #o Regla anti-spam: si es la 3ra vez seguida forzando, se activa alarma y no abre. 
#2. Hackear panel (costo: -10 energía, -3 tiempo) -
        #o Debe usar un for de 4 pasos mostrando progreso. 
        #o En cada paso sumar una letra al codigo_parcial (por ejemplo “A”). 
        #o Si len(codigo_parcial) >= 8, se abre automáticamente 1 cerradura si todavía faltan. 
#3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)  -
#Regla de bloqueo por alarma 
    #• Si alarma == True y tiempo <= 3 y todavía no se abrió la bóveda, el sistema se bloquea y se pierde.
#Condiciones de fin  -
    #• Si cerraduras_abiertas == 3 → VICTORIA 
    #• Si energia <= 0 o tiempo <= 0 → DERROTA 
    #• Si se bloquea por alarma → DERROTA (bloqueo)

Energia = 100
Tiempo = 12
Cerraduras_Abiertas = 0
Alarma = False
Codigo_Parcial = ""
AntiSpam_Accion1 = 0 

print ("\nSos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados.\nSi abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.\n\nBuenas suerte agente.\n") 
Agente = input("Ingrese el nombre del agente: ")
while not Agente.isalpha():
    Agente = input("Nombre inválido. Por favor, ingrese solo letras.")

while Energia > 0 and Tiempo > 0 and Cerraduras_Abiertas < 3 and not Alarma: #Esto seria el bucle pincipal del juego. 
        print(f"Agente: {Agente} | Energía: {Energia} | Tiempo: {Tiempo} | Cerraduras Abiertas: {Cerraduras_Abiertas} | Alarma: {'ON' if Alarma else 'OFF'}\n")
        print("  1. Forzar cerradura (Costo: -20 Energía, -2 Tiempo)")
        print("  2. Hackear panel (Costo: -10 Energía, -3 Tiempo)")
        print("  3. Descansar (Costo: +15 Energía (máx 100), -1 Tiempo; Si alarma ON: -10 energía extra)\n")   
        Acción = input("Elige una accion (1-3): ")
        while not Acción.isdigit() or int(Acción) < 1 or int(Acción) > 3:
            Acción = input("Opción inválida. Por favor, elige una opción (1; 2; 3): ")
        Acción = int(Acción)

#Forzar cerradura. Me tengo que acordar de hacer el anti spam.
        if Acción == 1: 
            Energia -= 20
            Tiempo -= 2
            AntiSpam_Accion1 += 1
            if Energia < 40:
                Riesgo_Alarma = input("Riesgo de alarma! Elige un número del 1 al 3: ")
                while not Riesgo_Alarma.isdigit() or int(Riesgo_Alarma) < 1 or int(Riesgo_Alarma) > 3:
                    Riesgo_Alarma = input("Número inválido. Por favor, elige un número del 1 al 3: ")
                if int(Riesgo_Alarma) == 3:
                        Alarma = True
                        print("¡Alarma activada!\n")
                if AntiSpam_Accion1 >= 3:
                    Alarma = True
                    print("La cerradura se trabó ¡Alarma activada!\n")
                else:
                    Cerraduras_Abiertas += 1
                    print("Cerradura forzada con éxito.\n")
            elif not Alarma: 
                Cerraduras_Abiertas += 1
                print("Cerradura forzada con éxito.\n")

#Hackear panel. Acá tengo que hacer el for de 4 pasos y el código parcial.
        elif Acción == 2:
            Energia -= 10
            Tiempo -= 3
            AntiSpam_Accion1 = 0 
            for i in range(4):
                Codigo_Parcial += "M"
                print(f"Hackeando... Progreso: {Codigo_Parcial}")
            if len(Codigo_Parcial) >= 8 and Cerraduras_Abiertas < 3:
                Cerraduras_Abiertas += 1
                print("Cerradura hackeada con éxito.\n")

#Descansar. Acá tengo que acordarme de la penalización extra si la alarma está ON.
        elif Acción == 3:
            Energia += 15
            AntiSpam_Accion1 = 0 
            if Energia > 100:
                Energia = 100
            Tiempo -= 1
            if Alarma:
                Energia -= 10
                print("Descansaste, pero la alarma está ON. Energía extra perdida.\n")
            else:
                print("Descansaste y recuperaste energía.\n")


        if Alarma and Tiempo <= 3 and Cerraduras_Abiertas < 3:
            print("\n---DERROTA---")
            print("La alarma a sido activada. ¡Sistema bloqueado!\n")
            break   
        if Cerraduras_Abiertas >= 3:
            print("\n---VICTORIA---")
            print("¡Felicitaciones agente! Lograste abrir la bóveda a tiempo.\n")
        elif Energia <= 0 or Tiempo <= 0:
            print("\n---DERROTA---")
            print("Te quedaste sin energía o sin tiempo. ¡Mejor suerte la próxima vez!\n")


#Creo que quedo. Fue una cosa curiosa el hacer esto, la idea de poder crear rpgs o juegos mas "Rusticos", resulta entretenido.
#Seguramente tenga errores, pero bueno, es una primera vez y la verdad que hasta el ultimo intento buscque la forma de romperlo mientras lo jugaba jhaja. 
