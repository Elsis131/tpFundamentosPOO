from personaje import personaje

class luigi(personaje):
    def __init__(self, nombre, vida):
        super().__init__(nombre, vida)
        self.__tieneHonguito = False
        self.__poderesHielo = False

    def comerHonguito(self):
        if self.__tieneHonguito:
            return f"{self.nombre} ya comió un honguito; no puede usar otro."
        
        self.__tieneHonguito = True
        self.vida += 1
        return f"{self.nombre} comió un honguito; ahora tiene {self.vida} de vida."
    
    def comerFlor(self):
        if self.__poderesHielo:
            return f"{self.nombre} ya tiene el poder de hielo; no puede agarrar otra flor."
        
        self.__poderesHielo = True
        return f"{self.nombre} comió una flor, ahora tiene poderes de hielo. :D"
