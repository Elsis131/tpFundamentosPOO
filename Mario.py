from personaje import personaje

class mario:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida
        self._tieneFlor = False
        self._comioHonguito = False
        self._comioFlor = False

    def comerHonguito(self):
        if self._comioHonguito:
            return f"{self.nombre} ya comió un honguito antes."
        self._comioHonguito = True
        self.vida += 1
        return f"{self.nombre} comió un honguito y ahora tiene {self.vida} de vida."

    def comerFlor(self):
        if self._comioFlor:
            return f"{self.nombre} ya comió una flor antes."
        self._comioFlor = True
        self._tieneFlor = True
        return f"{self.nombre} comió una flor y ahora puede lanzar fuego."

    def tieneFlor(self):
        return self._tieneFlor

    def saltarSobre(self):
        return f"{self.nombre} salta sobre el enemigo."

    def lanzarFuego(self):
        if self._tieneFlor:
            return f"{self.nombre} lanza bolas de fuego!"
        return f"{self.nombre} no tiene el poder de fuego."
