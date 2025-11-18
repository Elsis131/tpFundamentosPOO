from personaje import personaje

class luigi (personaje):
    def __init__(self, nombre, vida, poderesHielo):
        super().__init__(nombre, vida)
        self.__poderesHielo = False

    def comerHonguito (self):
        self.vida += 1
        return f"{self.nombre} comió un honguito y ahora tiene {self.vida} de vida."
    
    def comerFlor (self):
        self.__poderesHielo = True
        return f"{self.nombre} comió una flor y ahora tiene poderes :D"
    