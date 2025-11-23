from personaje import personaje

class mario(personaje):
    def __init__(self, nombre, vida):
        super().__init__(nombre, vida)
        self.__tieneHonguito = False
        self.__poderesFuego = False

    def comerHonguito(self):
        if self.__tieneHonguito:
            return f"{self.nombre} ya comió un honguito, no puede usar otro."
        
        self.__tieneHonguito = True
        self.vida += 1
        return f"{self.nombre} comió un honguito, ahora tiene {self.vida} de vida."
    
    def comerFlor(self):
        if self.__poderesFuego:
            return f"{self.nombre} ya tiene el poder de fuego, no puede agarrar otra flor."
        
        self.__poderesFuego = True
        return f"{self.nombre} comió una flor, ahora tiene poderes de fuego. :D"
    