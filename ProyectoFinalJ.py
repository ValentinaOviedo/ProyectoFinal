import random
#Proyecto Final Batalla Naval 
#Integrantes (Alejandro Mendoza, Valentina Ceron, Saray Rincon, Juan Felipe Castro)
# Generación de tableros
def crearTablero(tamano):
    return [["~" for _ in range(tamano)] for _ in range(tamano)]

def mostrarTableros(tableroDisparosJugador, tableroDisparosOponente):
    print("Tu tablero de disparos:")
    for fila in tableroDisparosJugador:
        print(" ".join(fila))
    
    print("Tablero de disparos del oponente:")
    for fila in tableroDisparosOponente:
        print(" ".join(fila))

# Generación de barcos
def colocarBarcos(tablero, barcos, jugador):
    for barco in barcos:
        colocado = False
        while not colocado:
            if jugador == "jugador":
                print(f"Colocando {barco['nombre']} de tamaño {barco['tamaño']}")
                fila = int(input("Ingresa la fila (0-4): "))
                columna = int(input("Ingresa la columna (0-4): "))
                orientacion = input("Ingresa la orientación (h para horizontal, v para vertical): ").lower()
            else:
                fila = random.randint(0, len(tablero) - 1)
                columna = random.randint(0, len(tablero) - 1)
                orientacion = random.choice(['h', 'v'])
            
            if validarColocacion(tablero, fila, columna, barco['tamaño'], orientacion):
                colocarBarco(tablero, fila, columna, barco['tamaño'], orientacion)
                colocado = True
            elif jugador == "jugador":
                print("Colocación inválida. Inténtelo de nuevo.")

def validarColocacion(tablero, fila, columna, tamano, orientacion):
    if orientacion == 'h':
        if columna + tamano > len(tablero):
            return False
        for i in range(tamano):
            if tablero[fila][columna + i] != "~":
                return False
    else:
        if fila + tamano > len(tablero):
            return False
        for i in range(tamano):
            if tablero[fila + i][columna] != "~":
                return False
    return True

def colocarBarco(tablero, fila, columna, tamano, orientacion):
    if orientacion == 'h':
        for i in range(tamano):
            tablero[fila][columna + i] = "B"
    else:
        for i in range(tamano):
            tablero[fila + i][columna] = "B"

# Sistema de combate
def realizarDisparo(tableroOculto, tableroDisparos, fila, columna):
    if tableroOculto[fila][columna] == "B":
        tableroDisparos[fila][columna] = "X"
        tableroOculto[fila][columna] = "H"  # Marcar como hundido
        return "Impacto"
    elif tableroDisparos[fila][columna] == "~":
        tableroDisparos[fila][columna] = "O"
        return "Agua"
    return "Ya disparaste aquí"

def verificarVictoria(tableroOculto):
    for fila in tableroOculto:
        if "B" in fila:  # Si hay algún barco no hundido
            return False
    return True

# Automatización de la CPU
def jugarContraComputadora():
    tamano = 5
    tableroJugador = crearTablero(tamano)
    tableroComputadora = crearTablero(tamano)
    tableroDisparosJugador = crearTablero(tamano)
    tableroDisparosComputadora = crearTablero(tamano)

    barcos = [
        {"nombre": "portaaviones", "tamaño": 3},
        {"nombre": "submarino", "tamaño": 2}
    ]

    print("Coloca tus barcos")
    colocarBarcos(tableroJugador, barcos, "jugador")
    colocarBarcos(tableroComputadora, barcos, "computadora")

    # Turnos de juego
    turnoJugador = True

    # Condiciones de victoria
    while True:
        if turnoJugador:
            print("Tu turno")
            mostrarTableros(tableroDisparosJugador, tableroDisparosComputadora)
            fila = int(input("Ingresa fila de disparo (0-4): "))
            columna = int(input("Ingresa columna de disparo (0-4): "))
            resultado = realizarDisparo(tableroComputadora, tableroDisparosJugador, fila, columna)
            print(resultado)
            if verificarVictoria(tableroComputadora):
                print("¡Ganaste!")
                return "jugador"
        else:
            print("Turno de la computadora")
            fila = random.randint(0, tamano - 1)
            columna = random.randint(0, tamano - 1)
            resultado = realizarDisparo(tableroJugador, tableroDisparosComputadora, fila, columna)
            print(f"La computadora disparó en ({fila}, {columna}): {resultado}")
            if verificarVictoria(tableroJugador):
                print("La computadora ganó.")
                return "computadora"
        turnoJugador = not turnoJugador

# Método multiplayer
def jugarDosJugadores():
    tamano = 5
    tableroJugador1 = crearTablero(tamano)
    tableroJugador2 = crearTablero(tamano)
    tableroDisparosJugador1 = crearTablero(tamano)
    tableroDisparosJugador2 = crearTablero(tamano)

    barcos = [
        {"nombre": "portaaviones", "tamaño": 3},
        {"nombre": "submarino", "tamaño": 2}
    ]

    # Colocación de barcos de ambos jugadores
    print("Jugador 1 coloca sus barcos")
    colocarBarcos(tableroJugador1, barcos, "jugador")
    print("Jugador 2 coloca sus barcos")
    colocarBarcos(tableroJugador2, barcos, "jugador")

    # Turnos de juego
    turnoJugador1 = True

    # Condiciones de victoria
    while True:
        if turnoJugador1:
            print("Turno del Jugador 1")
            mostrarTableros(tableroDisparosJugador1, tableroDisparosJugador2)
            fila = int(input("Ingresa la fila del disparo (0-4): "))
            columna = int(input("Ingresa la columna del disparo (0-4): "))
            resultado = realizarDisparo(tableroJugador2, tableroDisparosJugador1, fila, columna)
            print(resultado)
            if verificarVictoria(tableroJugador2):
                print("¡Jugador 1 ganó!")
                return "jugador1"
        else:
            print("Turno del Jugador 2")
            mostrarTableros(tableroDisparosJugador2, tableroDisparosJugador1)
            fila = int(input("Ingresa la fila del disparo (0-4): "))
            columna = int(input("Ingresa la columna del disparo (0-4): "))
            resultado = realizarDisparo(tableroJugador1, tableroDisparosJugador2, fila, columna)
            print(resultado)
            if verificarVictoria(tableroJugador1):
                print("¡Jugador 2 ganó!")
                return "jugador2"
        turnoJugador1 = not turnoJugador1

# Reinicio de menú
def mostrarMenu():
    print("Bienvenido al juego Batalla Naval")
    print("1. Juega contra la computadora")
    print("2. Dos Jugadores")
    print("3. Salir") 

def iniciarJuego():
    while True:
        mostrarMenu()
        modo = input("Elige una opción (1-3): ")

        if modo == "1":
            ganador = jugarContraComputadora()
        elif modo == "2":
            ganador = jugarDosJugadores()
        elif modo == "3":
            print("Gracias por jugar. ¡Hasta pronto!")
            break
        else:
            print("La opción seleccionada no es válida, elige una opción entre 1 y 3.")
            continue
        print(f"El ganador es {ganador}.")

        jugarDeNuevo = input("¿Quiere jugar de nuevo? (s/n): ").lower()
        if jugarDeNuevo != "s":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

iniciarJuego()
