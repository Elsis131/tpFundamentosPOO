from personaje import personaje

class mario (personaje):
    def __init__(self, nombre, vida, poderesFuego):
        super().__init__(nombre, vida)
        self.__poderesFuego = False

    def comerHonguito (self):
        self.vida += 1
        return f"{self.nombre} comió un honguito y ahora tiene {self.vida} de vida."
    
    def comerFlor (self):
        self.__poderesFuego = True
        return f"{self.nombre} comió una flor y ahora tiene poderes :D"
    