'''
Un ta-te-ti con ciertas cosas de Gardel.
'''

JUGADOR_1 = {"Número": 1, "Letra": " "}
JUGADOR_2 = {"Número": 2, "Letra": " "}
JUGADOR_ACTIVO = {}
JUGADORES_DEFINIDOS = False
JUGANDO = True
PRIMERA_PARTIDA = True
CASILLEROS = {"1": " ", "2": " ", "3": " ", "4": " ",
              "5": " ", "6": " ", "7": " ", "8": " ", "9": " ", }
GARDEL = """
  @@@@@@@@@@@@@@@@@@@@@@@@wN@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@Q;Q@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@QM@@@@@@@@@QiQ@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@WI@&gQ@@@@@8QdQ@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@Qh@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@^@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@&Q@@@8AFm&Q@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@,-?O@@@A?(;--,;*(fhWQ@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@/ -@@Q,i@QYhD3|:-    ,;(XQ@@@@@@@@@@@@@@@@
  @@@@@@@@QF^IavQj  >@@@@@@Q9ji;,- -^IR@@@@@@@@@@@@
  @@@@@@@@@@@hc.I-  >@@yq@@DG@@@Q@QNh1?|&@@@@@@@@@@
  @@@@@@@@@@@KSj     .,  -M, ~ic+yKg@@@@@@@@@@@@@@@
  @@@@@@@@@@@Q:*                    Q@@@@@@@@@@@@@@
  @@@@@@@@@@@@f         -r,        ,@@@@@@@@@@@@@@@
  @@@@@@@@@@@@8       .  -=?       f@@@@@@@@@@@@@@@
  @@@@@@@@@@@@D       ~yr,    ;   ~@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@Q; ,-         -.   +@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@M;:|.          ,A@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@N9@@G^.    .3@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@KKQ@OxhA@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@l  .:7.r@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@D.  +Nq@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@| &@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@q~@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@@Q@@@@@@@@@@@@@@@@@@@@@@
"""


def dar_la_bienvenida():
    '''
    Da la bienvenida a los jugadores y muestra a Carlos Gardel.
    '''
    limpiar_pantalla()
    print(GARDEL)
    print(
        "\n  > Bienvenidos al Ta-Te-Ti, un juego tan argentino como "
        "Carlos GARDEL —de quien se afirma que en realidad era uruguayo o francés—.\n")
    if input("  > Presioná Enter para continuar."):
        return


def definir_jugadores():
    '''
    Pide a Jugador 1 que ingrese "X" o "O".
    Devuelve tuple de dos elementos.
    El elemento [0] es la letra del Jugador 1; el [1], la del Jugador 2.
    '''
    while True:
        input_j_1 = input('\n  > Jugador 1, ¿querés ser "X" o "O"?: ').lower()
        if input_j_1 == "x":
            return ("X", "O")
        if input_j_1 == "o":
            return ("O", "X")
        print('\n  > No entendí. Por favor, ingresá "X" o "O".')


def cambiar_jugador_activo():
    '''
    Se fija cuál es el jugador activo y devuelve la variable asociada al otro jugador.
    '''
    if JUGADOR_ACTIVO["Número"] == 1:
        return JUGADOR_2
    return JUGADOR_1


def elegir_casillero(jugador):
    '''
    Asigna al casillero elegido la letra del jugador.
    Se asegura de que el input del usuario se pueda convertir a integer.
    Chequea si el casillero ya está ocupado y, si está ocupado, pide al usuario que elija otro.
    '''
    eleccion = ""
    while not eleccion.isdigit():
        eleccion = input(
            f'\n  > Jugador {jugador["Número"]}, elegí un casillero del 1 al 9, for favor: ')
        if eleccion.isdigit():
            if int(eleccion) in range(1, 10):
                if CASILLEROS[eleccion] != " ":
                    print(
                        "\n  > Ese casillero ya está ocupado, es mejor para todos si elegís otro.")
                    eleccion = ""
                    continue
                CASILLEROS[eleccion] = jugador["Letra"]
                return
        print('\n  > Lo lamento muchísimo, pero sólo admito números del 1 al 9.')
        eleccion = ""


def mostrar_tablero(casilleros):
    '''
    Limpia la pantalla.
    Muestra el tablero con las posiciones actuales.
    '''
    limpiar_pantalla()
    print(f"""
   ___________ ___________ ___________ 
  |1          |2          |3          |
  |           |           |           |
  |     {casilleros['1']}     |     {casilleros['2']}     |     {casilleros['3']}     |
  |           |           |           |
  |___________|___________|___________|
  |4          |5          |6          |
  |           |           |           |
  |     {casilleros['4']}     |     {casilleros['5']}     |     {casilleros['6']}     |
  |           |           |           |
  |___________|___________|___________|
  |7          |8          |9          |
  |           |           |           |
  |     {casilleros['7']}     |     {casilleros['8']}     |     {casilleros['9']}     |
  |           |           |           |
  |___________|___________|___________|
    """)


def vaciar_casilleros():
    '''
    Devuelve un dictionary de casilleros vacíos.
    '''
    return {"1": " ", "2": " ", "3": " ", "4": " ",
            "5": " ", "6": " ", "7": " ", "8": " ", "9": " ", }


def chequear_ganador_o_empate(jugador):
    '''
    Chequea si la jugada es una jugada ganadora.
    Chequea si hay un empate.
    '''
    jugadas_ganadoras = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], [
        "1", "4", "7"], ["2", "5", "8"], ["3", "6", "9"], ["1", "5", "9"], ["3", "5", "7"]]
    for jugada in jugadas_ganadoras:
        ganador = True
        for casillero in jugada:
            if CASILLEROS[casillero] != jugador["Letra"]:
                ganador = False
                break
        if ganador:
            print(
                f'\n  > No me queda más que felicitar al jugador {jugador["Número"]}'
                ' por haber conseguido la victoria.')
            return True
    if chequear_empate():
        print("\n  > Tenemos un desabrido empate.")
        return True
    return False


def chequear_empate():
    '''
    Chequea si el tablero tiene todas las posiciones ocupadas.
    '''
    for casillero in CASILLEROS:
        if CASILLEROS[casillero] == " ":
            return False
    return True


def jugar_de_nuevo():
    '''
    Pregunta a los jugadores si quieren jugar de nuevo.
    Si no quieren, se despide.
    '''
    respuestas_admitidas = ["s", "n"]
    respuesta = input("\n  > ¿Quieren jugar de nuevo? S/N: ").lower()

    while respuesta not in respuestas_admitidas:
        respuesta = input(
            '\n  > No entendí. Por favor, ingresen "S" si quieren jugar de nuevo'
            ' o "N" si no quieren: ').lower()

    if respuesta == "s":
        return True

    if respuesta == "n":
        limpiar_pantalla()
        print(GARDEL)
        print("\n  > Ha sido un honor tenerlos como jugadores, lo digo con honestidad.\n")
        return False


def limpiar_pantalla():
    '''
    Imprime nuevas líneas para limpiar la pantalla.
    '''
    print("\n")
    print("""
  #############################################################
  #############################################################
  ###                                                       ###
  ###   NO DEBISTE SCROLLEAR HASTA ACÁ ARRIBA.              ###
  ###   DESCUBRISTE UN SECRETO DE LA PROGRAMACIÓN           ###
  ###   Y AHORA VAS A TENER QUE PAGAR CARA TU CURIOSIDAD.   ###
  ###                                                       ###
  #############################################################
  #############################################################
  """)
    print("\n"*500)


while JUGANDO:
    if PRIMERA_PARTIDA:
        dar_la_bienvenida()
        PRIMERA_PARTIDA = False
    if not JUGADORES_DEFINIDOS:
        mostrar_tablero(CASILLEROS)
        JUGADOR_1["Letra"], JUGADOR_2["Letra"] = definir_jugadores()
        JUGADORES_DEFINIDOS = True
        JUGADOR_ACTIVO = JUGADOR_1
        print(
            f'\n  > El jugador 1 juega con "{JUGADOR_1["Letra"]}"'
            f' y el jugador 2 con "{JUGADOR_2["Letra"]}"')
    elegir_casillero(JUGADOR_ACTIVO)
    mostrar_tablero(CASILLEROS)
    if chequear_ganador_o_empate(JUGADOR_ACTIVO):
        if not jugar_de_nuevo():
            JUGANDO = False
            break
        JUGADORES_DEFINIDOS = False
        CASILLEROS = vaciar_casilleros()
        continue
    JUGADOR_ACTIVO = cambiar_jugador_activo()
