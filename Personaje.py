class personaje:
    def __init__(self, nombre, vida):
        self._nombre = nombre
        self._vida = vida

    def saltar (self):
        return f"{self.nombre} saltó."
    
    def avanzar (self):
        return f"{self.nombre} avanzó."
    