class bowser:
    def __init__(self, nombre, vida):
        self.__nombre = nombre
        self.__vida = []

    def lanzar_fuego(self):
        return f"{self.nombre} lanza  fuego!"

    def recibir_daño(self, daño):
        self.vida -= daño
        return f"{self.nombre} recibió {daño} de daño y le quedan {self.vida} de vida."
    
    def ataque_con_salto (self):
        return f"{self.__nombre} ataca con un salto!"
    
    def combo_ataque (self):
        return f"{self.__nombre} realiza un combo de ataques!"
