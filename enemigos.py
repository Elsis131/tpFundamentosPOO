from personaje import personaje

class bowser:
    def __init__(self, nombre, vida, poderes):
        super().__init__(nombre, vida)
        self.__nombre = nombre
        self.__vida = []
        self.__poderes = poderes

    def lanzar_fuego(self):
        return f"{self.nombre} lanzó  fuego!"

    def recibir_daño(self, daño):
        self.vida -= daño
        return f"{self.nombre} recibió {daño} de daño y le quedan {self.vida} de vida."
    
    def ataque_con_salto (self):
        return f"{self.__nombre} atacó con un salto!"
    
    def combo_ataque (self):
        return f"{self.__nombre} realizó un combo de ataques!"
