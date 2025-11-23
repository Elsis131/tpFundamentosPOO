from mario import mario
from luigi import luigi
from enemigos import bowser

def mostrarMenu():

        print("\n MENÚ DE OPCIONES")
        print("1. Mario come un honguito")
        print("2. Mario come una flor")
        print("3. Luigi come un honguito")
        print("4. Luigi come una flor")
        print("5. Bowser lanza fuego")
        print("6. Bowser realiza ataque con salto")
        print("7. Bowser realiza un combo de ataque")
        print("8. Bowser recibe daño")
        print("0. Salir")

def main():

    while True:
        mostrarMenu()
        opcion = input("selecciona una opción: ")
        if opcion == "1":
            mario.comerHonguito()