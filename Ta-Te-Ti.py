jugador_1 = {"Número": 1, "Letra": " "}
jugador_2 = {"Número": 2, "Letra": " "}
jugador_activo = {}
jugadores_definidos = False
jugando = True
primera_partida = True
casilleros = {"1": " ", "2": " ", "3": " ", "4": " ",
              "5": " ", "6": " ", "7": " ", "8": " ", "9": " ", }
gardel = """
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
    limpiar_pantalla()
    global primera_partida
    print(gardel)
    print(
        "\n  > Bienvenidos al Ta-Te-Ti, un juego tan argentino como Carlos Gardel —de quien se afirma que en realidad era uruguayo o francés—.\n")
    primera_partida = False
    if input("  > Presioná Enter para continuar."):
        return


def definir_jugadores():
    global jugador_1
    global jugador_2
    global jugadores_definidos
    global jugador_activo
    while not jugadores_definidos:
        input_j_1 = input('\n  > Jugador 1, ¿querés ser "X" o "O"?: ').lower()
        if input_j_1 == "x":
            jugador_1["Letra"] = "X"
            jugador_2["Letra"] = "O"
            jugadores_definidos = True
        elif input_j_1 == "o":
            jugador_1["Letra"] = "O"
            jugador_2["Letra"] = "X"
            jugadores_definidos = True
        else:
            print('\n  > No entendí. Por favor, ingresá "X" o "O".')
    jugador_activo = jugador_1
    return print(f'\n  > El jugador 1 juega con "{jugador_1["Letra"]}" y el 2 con "{jugador_2["Letra"]}".\n\n  > Empieza el jugador 1.')


def definir_jugador_activo():
    global jugador_activo
    if jugador_activo["Número"] == 1:
        jugador_activo = jugador_2
    else:
        jugador_activo = jugador_1


def elegir_casillero(jugador):
    eleccion = ""
    while not eleccion.isdigit():
        eleccion = input(
            f'\n  > Jugador {jugador["Número"]}, elegí un casillero del 1 al 9, for favor: ')
        if eleccion.isdigit():
            if int(eleccion) in range(1, 10):
                if casilleros[eleccion] != " ":
                    print(
                        "\n  > Ese casillero ya está ocupado, es mejor para todos si elegís otro.")
                    eleccion = ""
                    continue
                else:
                    casilleros[eleccion] = jugador["Letra"]
                    return
        print('\n  > Lo lamento muchísimo, pero sólo admito números del 1 al 9.')
        eleccion = ""


def mostrar_tablero(casilleros):
    limpiar_pantalla()
    print("   ___________ ___________ ___________ ")
    print("  |1          |2          |3          |")
    print("  |           |           |           |")
    print(
        f"  |     {casilleros['1']}     |     {casilleros['2']}     |     {casilleros['3']}     |")
    print("  |           |           |           |")
    print("  |___________|___________|___________|")
    print("  |4          |5          |6          |")
    print("  |           |           |           |")
    print(
        f"  |     {casilleros['4']}     |     {casilleros['5']}     |     {casilleros['6']}     |")
    print("  |           |           |           |")
    print("  |___________|___________|___________|")
    print("  |7          |8          |9          |")
    print("  |           |           |           |")
    print(
        f"  |     {casilleros['7']}     |     {casilleros['8']}     |     {casilleros['9']}     |")
    print("  |           |           |           |")
    print("  |___________|___________|___________|")


def limpiar_tablero():
    global casilleros
    casilleros = {"1": " ", "2": " ", "3": " ", "4": " ",
                  "5": " ", "6": " ", "7": " ", "8": " ", "9": " ", }


def chequear_ganador(jugador):
    jugadas_ganadoras = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], [
        "1", "4", "7"], ["2", "5", "8"], ["3", "6", "9"], ["1", "5", "9"], ["3", "5", "7"]]
    for jugada in jugadas_ganadoras:
        ganador = True
        for casillero in jugada:
            if casilleros[casillero] != jugador["Letra"]:
                ganador = False
                break
        if ganador:
            print(
                f'\n  > No me queda más que felicitar al jugador {jugador["Número"]} por haber conseguido la victoria.')
            return True
    if chequear_empate():
        print("\n  > Tenemos un desabrido empate.")
        return True
    return False


def chequear_empate():
    for casillero in casilleros:
        if casilleros[casillero] == " ":
            return False
    return True


def jugar_de_nuevo():
    global jugando
    global jugadores_definidos
    respuestas_admitidas = ["s", "n"]
    respuesta = input("\n  > ¿Quieren jugar de nuevo? S/N: ").lower()

    while respuesta not in respuestas_admitidas:
        respuesta = input(
            '\n  > No entendí. Por favor, ingresen "S" si quieren jugar de nuevo o "N" si no quieren: ').lower()

    if respuesta == "s":
        jugando = True
        jugadores_definidos = False

    if respuesta == "n":
        jugando = False
        print("\n  > Ha sido un honor tenerlos como jugadores, lo digo con honestidad.\n")

    return jugando


def limpiar_pantalla():
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


while jugando:
    if primera_partida:
        dar_la_bienvenida()
    if not jugadores_definidos:
        mostrar_tablero(casilleros)
        definir_jugadores()
    elegir_casillero(jugador_activo)
    mostrar_tablero(casilleros)
    if chequear_ganador(jugador_activo):
        if not jugar_de_nuevo():
            break
        else:
            limpiar_tablero()
            continue
    definir_jugador_activo()
