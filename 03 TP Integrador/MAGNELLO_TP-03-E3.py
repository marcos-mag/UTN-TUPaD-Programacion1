#E3-Agenda-de-turnos-con-nombres
#Hay 2 días de atención: Lunes y Martes. 
#Cada día tiene cupos fijos: -
    #• Lunes: 4 turnos 
    #• Martes: 3 turnos 
#Reglas 
#1. Pedir nombre del operador (solo letras). - 
#2. Menú repetitivo hasta salir: 
    #1. Reservar turno 
    #2. Cancelar turno (por nombre) 
    #3. Ver agenda del día 
    #4. Ver resumen general 
    #5. Cerrar sistema 
#3. Reservar: -
    #o Elegir día (1=Lunes, 2=Martes). 
    #o Pedir nombre del paciente (solo letras). 
    #o Verificar que no esté repetido en ese día (comparando con las variables ya cargadas). 
    #o Guardar en el primer espacio libre (ej. lunes1, lunes2...). 
#4. Cancelar: -
    #o Elegir día. 
    #o Pedir nombre del paciente (solo letras). 
    #o Si existe, cancelar y dejar el espacio vacío (""). 
#5. Ver agenda del día: - 
    #Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si está vacío.
#6. Resumen general: -
    #o Turnos ocupados y disponibles por día. 
    #o Día con más turnos (o empate). 

#Cupos fijos: (SI FUERAN LISTAS, SERIA MÁS FACIL)
#Lunes
Lunes1 = ""
Lunes2 = "" 
Lunes3 = ""
Lunes4 = ""
#Martes
Martes1 = ""; Martes2 = ""; Martes3 = ""  #Me enseñaron esto, para ahorrar lineas. Dejo los lunes asi para ver la diferencia.

#Pedimos nombre. Ando probando el while not. 
N_operador = input("Buenos Dias, ingrese nombre del operador/a:")
while not N_operador.isalpha():
    N_operador = input("Error, el nombre ingresado solo debe tener letras:")

#Menu repetitivo.
#1-Reserva de turnos.
while True:
    print("Menú: \n 1. Reservar turno \n 2. Cancelar turno \n 3. Ver agenda del día \n 4. Ver resumen general \n 5. Cerrar sistema", end="\n\n")  #Que descubrimiento fue el \n, dios santo.
    Opcion = input("Seleccione una opción (1-5): ")
    if Opcion.isdigit() and 1 <= int(Opcion) <= 5:
        Opcion = int(Opcion)
        if Opcion == 1:
            Dia = input("Seleccione el día para reservar (1=Lunes, 2=Martes): ")
            if Dia.isdigit() and 1 <= int(Dia) <= 2:
                Dia = int(Dia)
                Nombre_paciente = input("Ingrese el nombre del paciente: ")
                while not Nombre_paciente.isalpha():
                    Nombre_paciente = input("Error, el nombre ingresado solo debe tener letras: ")
                if Dia == 1:
                    if Lunes1 == "" and Nombre_paciente not in [Lunes2, Lunes3, Lunes4]:
                        Lunes1 = Nombre_paciente
                        print(f"Turno reservado para {Nombre_paciente} el lunes.")
                    elif Lunes2 == "" and Nombre_paciente not in [Lunes1, Lunes3, Lunes4]:
                        Lunes2 = Nombre_paciente
                        print(f"Turno reservado para {Nombre_paciente} el lunes.")
                    elif Lunes3 == "" and Nombre_paciente not in [Lunes1, Lunes2, Lunes4]:
                        Lunes3 = Nombre_paciente
                        print(f"Turno reservado para {Nombre_paciente} el lunes.")
                    elif Lunes4 == "" and Nombre_paciente not in [Lunes1, Lunes2, Lunes3]:
                        Lunes4 = Nombre_paciente
                        print(f"Turno reservado para {Nombre_paciente} el lunes.")
                    else:
                        print("No hay turnos disponibles o el paciente ya tiene un turno ese día.")
                elif Dia == 2:
                    if Martes1 == "" and Nombre_paciente not in [Martes2, Martes3]:
                        Martes1 = Nombre_paciente
                        print(f"Turno reservado para {Nombre_paciente} el martes.")
                    elif Martes2 == "" and Nombre_paciente not in [Martes1, Martes3]:
                        Martes2 = Nombre_paciente
                        print(f"Turno reservado para {Nombre_paciente} el martes.")
                    elif Martes3 == "" and Nombre_paciente not in [Martes1, Martes2]:
                        Martes3 = Nombre_paciente
                        print(f"Turno reservado para {Nombre_paciente} el martes.")
                    else:
                        print("No hay turnos disponibles o el paciente) ya tiene un turno ese día.")

#2-Cancelar un turno:
        elif Opcion == 2:
            Dia = input("Seleccione el día correspondiente al turno a cancelar (1=Lunes, 2=Martes): ")
            if Dia.isdigit() and 1 <= int(Dia) <= 2: #Soy medio nabo, osea si y no, porque evito el posible error de que me ingresen un numero entre el 1 y el 2 con el int, pero podria poner solo para que sea o 1 o 2. Algo asi: while dia not in ["1", "2"]
                Dia = int(Dia)
                Nombre_paciente = input("Ingrese el nombre del paciente a cancelar: ")
                while not Nombre_paciente.isalpha():
                    Nombre_paciente = input("Error, el nombre ingresado solo debe tener letras: ")
                if Dia == 1:
                    if Nombre_paciente == Lunes1:
                        Lunes1 = ""
                        print(f"Turno cancelado para {Nombre_paciente} el lunes.") #Capaz estoy ocupando muchas lineas de codigo, pero creo que debolverles una respuesta despues de solicitar cancelar el turno, le sacaria un poco de incertidummbre al usuario de si lo hizo bien o no.
                    elif Nombre_paciente == Lunes2:
                        Lunes2 = ""
                        print(f"Turno cancelado para {Nombre_paciente} el lunes.")
                    elif Nombre_paciente == Lunes3:
                        Lunes3 = ""
                        print(f"Turno cancelado para {Nombre_paciente} el lunes.")
                    elif Nombre_paciente == Lunes4:
                        Lunes4 = ""
                        print(f"Turno cancelado para {Nombre_paciente} el lunes.")
                    else:
                        print("No se encontró un turno para ese paciente ese día.")
                elif Dia == 2:
                    if Nombre_paciente == Martes1:
                        Martes1 = ""
                        print(f"Turno cancelado para {Nombre_paciente} el martes.")
                    elif Nombre_paciente == Martes2:
                        Martes2 = ""
                        print(f"Turno cancelado para {Nombre_paciente} el martes.")
                    elif Nombre_paciente == Martes3:
                        Martes3 = ""
                        print(f"Turno cancelado para {Nombre_paciente} el martes.")
                    else:
                        print("No se encontró un turno para ese paciente ese día.")

#3-Ver agenda del día:
        elif Opcion == 3:
            Dia = input("Seleccione el día para ver la agenda (1=Lunes, 2=Martes): ")
            if Dia.isdigit() and 1 <= int(Dia) <= 2:
                Dia = int(Dia)
                if Dia == 1:
                    print("Agenda del Lunes:\n" #Me gusta como queda, anteriormente hubiera puesto un print por cada turno...
                        f"  Turno 1: {Lunes1 or 'Libre'}\n" #2 espacios generan sangria :O. Estoy descubriendo la polvora. 
                        f"  Turno 2: {Lunes2 or 'Libre'}\n"
                        f"  Turno 3: {Lunes3 or 'Libre'}\n"
                        f"  Turno 4: {Lunes4 or 'Libre'}\n")
                elif Dia == 2:
                    print("Agenda del Martes:\n"
                        f"  Turno 1: {Martes1 or 'Libre'}\n"
                        f"  Turno 2: {Martes2 or 'Libre'}\n"
                        f"  Turno 3: {Martes3 or 'Libre'}\n")
            else:
                print("Opción de día no válida. Por favor, seleccione 1 o 2.")

#4-Resumen general:
        elif Opcion == 4:
            Turnos_ocupados_Lunes = sum(1 for turno in [Lunes1, Lunes2, Lunes3, Lunes4] if turno)
            Turnos_disponibles_Lunes = 4 - Turnos_ocupados_Lunes
            Turnos_ocupados_Martes = sum(1 for turno in [Martes1, Martes2, Martes3] if turno)
            Turnos_disponibles_Martes = 3 - Turnos_ocupados_Martes
            print(f"Resumen General:\n"
                f"  Lunes: {Turnos_ocupados_Lunes} turnos ocupados, {Turnos_disponibles_Lunes} turnos disponibles.\n"
                f"  Martes: {Turnos_ocupados_Martes} turnos ocupados, {Turnos_disponibles_Martes} turnos disponibles.\n")
            if Turnos_ocupados_Lunes > Turnos_ocupados_Martes:
                print("El día con más turnos ocupados es el Lunes.")
            elif Turnos_ocupados_Martes > Turnos_ocupados_Lunes:
                print("El día con más turnos ocupados es el Martes.")
            else:
                print("Ambos días tienen la misma cantidad de turnos ocupados.")

#5-Cerrar sistema:
        elif Opcion == 5:
            print("Cerrando sistema. ¡Nos vemos!")
            break
    else:   
        print("Opción no válida. Por favor, seleccione un número entre 1 y 5.")


#Creo que ya noto los pequeños cambios que vengo ahciendo en comparacion a los anteriores trabajos. (No los hago el mismo dia, capaz uno por dia)
#El uso de \n y no abusar tanto de los print(), creo que le da un toque.
#Estoy feliz. 
#Pd: Entiendo que no hay problema si comento tanto pot todo el codigo, no? ajajaj
