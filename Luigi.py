from personaje import personaje

class luigi:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida
        self._tieneFlor = False

    def comerHonguito(self):
        self.vida += 1
        return f"{self.nombre} comió un honguito y ahora tiene {self.vida} de vida."

    def comerFlor(self):
        self._tieneFlor = True
        return f"{self.nombre} comió una flor y ahora puede lanzar fuego."

    def tieneFlor(self):
        return self._tieneFlor

    def saltarSobre(self):
        return f"{self.nombre} salta con estilo sobre el enemigo."

    def lanzarFuego(self):
        if self._tieneFlor:
            return f"{self.nombre} lanza fuego verde!"
        return f"{self.nombre} no tiene el poder de fuego."
