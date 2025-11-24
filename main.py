from mario import mario
from luigi import luigi
from enemigos import bowser

# ---------------------------------------------------------
# MENÚS
# ---------------------------------------------------------

def menuSeleccionPersonaje():
    print("\n SELECCIONÁ TU PERSONAJE")
    print("1. Mario")
    print("2. Luigi")
    print("0. Salir")

def menuExploracion():
    print("\n ACCIONES DISPONIBLES")
    print("1. Correr hacia adelante")
    print("2. Mirar alrededor")
    print("3. Comer honguito")
    print("4. Comer flor")
    print("5. Ir hacia el castillo de Bowser")
    print("0. Salir")

def menuCombate(jugador):
    print(f"\n ACCIONES DE COMBATE ({jugador.nombre})")
    print("1. Saltar sobre Bowser")
    print("2. Esquivar ataque")
    if hasattr(jugador, "tieneFlor") and jugador.tieneFlor():
        print("3. Lanzar fuego")      # solo aparece si tiene el poder
    print("0. Salir del combate")

# ---------------------------------------------------------
# FLUJO PRINCIPAL
# ---------------------------------------------------------

def main():
    # SELECCIÓN DE PERSONAJE ---------------------------------------
    while True:
        menuSeleccionPersonaje()
        op = input("Elegí una opción: ")
        if op == "1":
            jugador = mario("Mario", 3)
            break
        elif op == "2":
            jugador = luigi("Luigi", 3)
            break
        elif op == "0":
            print("Saliendo del juego...")
            return
        else:
            print("Opción inválida.")

    enemigo = bowser("Bowser", 5)

    # EXPLORACIÓN DEL MAPA -----------------------------------------
    while True:
        menuExploracion()
        op = input("Elegí una acción: ")

        if op == "1":
            print(f"{jugador.nombre} corre por el sendero; cada vez se ve más cerca el castillo.")

        elif op == "2":
            print("El ambiente está silencioso; algunos bloques y árboles secos decoran el camino.")

        elif op == "3":
            if hasattr(jugador, "comerHonguito"):
                print(jugador.comerHonguito())
            else:
                print("Esta acción no está disponible para este personaje.")

        elif op == "4":
            if hasattr(jugador, "comerFlor"):
                print(jugador.comerFlor())
            else:
                print("Esta acción no está disponible para este personaje.")

        elif op == "5":
            print("Te acercás al castillo; la puerta se abre con un ruido fuerte.")
            print("Entrás con cautela, avanzás por un pasillo oscuro y… Bowser aparece frente a vos.")
            break

        elif op == "0":
            print("Saliendo del juego…")
            return

        else:
            print("Esa opción no existe.")

    # COMBATE CON BOWSER -------------------------------------------
    print("\n BOWSER RUGE Y SE PREPARA PARA ATACARTE")

    while enemigo.vida > 0:
        menuCombate(jugador)
        op = input("¿Qué hacés?: ")

        if op == "1":
            if hasattr(jugador, "saltarSobre"):
                print(jugador.saltarSobre())
            enemigo.recibirDanio(1)
            print(f"Bowser ahora tiene {enemigo.vida} de vida.")

        elif op == "2":
            print("Esquivás el ataque; Bowser se frustra y prepara otro movimiento.")

        elif op == "3" and hasattr(jugador, "tieneFlor") and jugador.tieneFlor():
            if hasattr(jugador, "lanzarFuego"):
                print(jugador.lanzarFuego())
            enemigo.recibirDanio(2)
            print(f"Bowser ahora tiene {enemigo.vida} de vida.")

        elif op == "0":
            print("Te retirás del combate...")
            return

        else:
            print("Esa acción no existe o no podés usarla.")

        # Turno de Bowser si sigue vivo
        if enemigo.vida > 0:
            print("\nBowser te ataca violentamente.")
            respuesta = input("¿Querés intentar esquivar? (s/n): ")
            if respuesta.lower() == "s":
                print("Lográs esquivar de milagro; seguís en pie.")
            else:
                if hasattr(jugador, "vida"):
                    jugador.vida -= 1
                    print(f"Bowser te golpea; ahora tenés {jugador.vida} de vida.")
                    if jugador.vida <= 0:
                        print("Bowser te derrotó.")
                        return
                else:
                    print("Bowser te golpea.")

    print("\nBowser cae al suelo derrotado; el castillo queda en silencio.")
    print("Ganaste la pelea.")

# ---------------------------------------------------------
# EJECUCIÓN
# ---------------------------------------------------------

if __name__ == "__main__":
    main()
