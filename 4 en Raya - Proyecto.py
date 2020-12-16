#Inicio variables generales.
import os
os.system ('cls')
fichas_puestas = 0
posicionj1 = 0
posicionj2 = 0
partida = True
tabla = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

#Función Tablero(tabla) para mostrar el tablero, en la que cada item de la lista, es un número donde igualaremos ese numero con la posición de la ficha del jugador.
def Tablero(tabla):
    print(tabla[13], ' | ', tabla[14], ' | ', tabla[15], ' | ', tabla[16])

    print('---------------------')

    print(tabla[9], ' | ', tabla[10], ' | ', tabla[11], ' | ', tabla[12])

    print('---------------------')

    print(tabla[5], ' | ', tabla[6], ' | ', tabla[7], ' | ', tabla[8])

    print('---------------------')

    print(tabla[1], ' | ', tabla[2], ' | ', tabla[3], ' | ', tabla[4])

#Función Menu() que muestra el menú incorporando la función de OpcionesMenu(), para elegir que opción escoge el jugador.
def Menu():
        print(" ========================================== ")
        print("== Bienvenido al juego del Cuatro en Raya ==")
        print(" ========================================== ")
        print("=============== IMPORTANTE =================")
        print(" ========================================== ")
        print("==== LEER instrucciones antes de jugar =====")
        print(" ========================================== ")
        print("== 1. Instrucciones ==")
        print("== 2. Jugar ==")
        print("== 3. Apagar el juego ==")
        OpcionesMenu()

#Función OpcionesMenu escogemos que evento sucederá dependiendo la elección del jugador.       
def OpcionesMenu():
    opcion = int(input("¿Qué opción deseas? "))
    if opcion == 1:
        Instrucciones()
    elif opcion == 2:
        Jugadas()
    elif opcion == 3:
        os.system ('cls')
        print ("HASTA LUEGO, ¡VUELVE PRONTO!")
    else:
        print("La opción es incorrecta, elija una opción correcta.")


def Instrucciones():
    os.system('cls')
    print("")
    print(" ========================================================================== ")
    print(" =========================== INSTRUCCIONES ================================ ")
    print("Las casillas van de izquierda a derecha empezando por abajo hacia arriba.")
    print("")
    print("Cada jugador tendrá un movimiento por turno, en el cual tendrá que elegir")
    print("que ficha poner en cada casilla, siempre y cuando no repita una posición")
    print("ya utilizada por el otro jugador. En caso de que fuese así, saltará un")
    print("mensaje indicando dicho error y a continuación, solicitará una nueva posición")
    print("")
    print("Para ganar, simplemente hay que conseguir posicionar 4 fichas en horizontal,")
    print("diagonal o vertical seguidas y proclamarte GANADOR de la partida! Si llegado")
    print("el momentoel tablero se queda sin posiciones disponibles y no hay ganador, se")
    print("quedará la partidda como empate, por lo que no habrá ganadores ni perdedores.")
    print(" =========================== IMPORTANTE =================================== ")
    print(" ===== LO PRINCIPAL DE ESTE JUEGO, ES DIVERTIRSE Y PASAR UN BUEN RATO ===== ")
    print("")
    input("Pulse cualquier tecla para volver al menú principal: ")
    print("")
    if input:
        os.system ('cls')
        Menu()

def Jugadas():
    jugar = True
    while jugar:
        tupla=(InicioJugadores())
        partida=True
        turno = 0
        while partida:
            if partida and turno == 0:
                partida=JugadaJugador1(posicionj1, tupla)
                turno += 1
            else:
                partida= JugadaJugador2(posicionj2, tupla)
                turno = 0
        jugar = SeguirJugando()

def InicioJugadores():
    jugador1 = input("¿Nombre del primer jugador? ")
    jugador2 = input("¿Nombre del segundo jugador? ")
    while jugador1 == jugador2:
        print("Los jugadores no pueden tener el mismo nombre.")
        jugador1 = input("¿Nombre del primer jugador? ")
        jugador2 = input("¿Nombre del segundo jugador? ")
    return(jugador1, jugador2)

def JugadaJugador1(posicionj1, tupla):
    global fichas_puestas
    partida = True
    Tablero(tabla)
    while partida:
        print("Dame la posición de la ficha", tupla[0])
        posicionj1 = int(input("Posición: "))
        if 1 <= posicionj1 <= 16:
            while tabla[posicionj1] == "O" or tabla[posicionj1] == "X":
                print("Esta posición es erronea o ya está cogida, dime otra.")
                posicionj1 = int(input("Posición: "))
            tabla[posicionj1] = "X"
            fichas_puestas += 1
            if PartidaGanada(tabla) == True:
                os.system ('cls')
                Tablero(tabla)
                print (" ")
                print ("¡ENHORABUENA ", str.upper(tupla[0]), " HAS GANADO!" )
                JuegoFinalizado()
                return False
            elif fichas_puestas == 16:
                os.system ('cls')
                Tablero(tabla)
                print ("=================")
                print ("== E M P A T E ==")
                print ("=================")
                return False
        os.system ('cls')
        return True
    

def JugadaJugador2(posicionj2, tupla):
    global fichas_puestas
    partida = True
    Tablero(tabla)
    while partida:
        print("Dame la posición de la ficha", tupla[1])
        posicionj2 = int(input("Posición: "))
        if 1 <= posicionj2 <= 16:
            while tabla[posicionj2] == "X" or tabla[posicionj2] ==  "O":
                print("Esta posición es erronea o ya está cogida, dime otra.")
                posicionj2 = int(input("Posición: "))
            tabla[posicionj2] = "O"
            fichas_puestas += 1
            
            if PartidaGanada(tabla)==True:
                os.system ('cls')
                Tablero(tabla)
                print (" ")
                print ("¡ENHORABUENA ", str.upper(tupla[1]), " HAS GANADO!" )
                JuegoFinalizado()
                return False
            elif fichas_puestas == 16:
                os.system ('cls')
                Tablero(tabla)
                print ("=================")
                print ("== E M P A T E ==")
                print ("=================")
                return False
        os.system ('cls')
        return True

def PartidaGanada(tabla):
    if tabla[13] == tabla[14] == tabla[15] == tabla[16] or\
        tabla[9] == tabla[10] == tabla[11] == tabla[12] or\
        tabla[5] == tabla[6] == tabla[7] == tabla[8] or\
        tabla[1] == tabla[2] == tabla[3] == tabla[4] or\
        tabla[13] == tabla[9] == tabla[5] == tabla[1] or\
        tabla[14] == tabla[10] == tabla[6] == tabla[2] or\
        tabla[15] == tabla[11] == tabla[7] == tabla[3] or\
        tabla[16] == tabla[12] == tabla[8] == tabla[4] or\
        tabla[13] == tabla[10] == tabla[7] == tabla[4] or\
        tabla[1] == tabla[6] == tabla[11] == tabla[16]:
        print ("===============")
        print (" ¡VICTORIA!")
        return True
    else:
        return False

def JuegoFinalizado():
    print("=================")
    print("==FIN DEL JUEGO==")
    print("=================")
    

def SeguirJugando(): #Devolverá TRUE si el jugador quiere seguir jugando.
    global fichas_puestas
    global tabla
    print(" ")
    respuesta= input("Quieres jugar otra partida? S/N: ").lower()
    if respuesta == "s" or respuesta == "si":
        os.system ('cls')
        fichas_puestas = 0
        tabla = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        return True
    else:
        print(" ")
        print ("GRACIAS POR HABER JUGADO AL 4 EN RAYA.")
        return False
        
# Programa principal
Menu()
