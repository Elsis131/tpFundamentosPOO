class bowser:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def lanzarFuego(self):
        return f"{self.nombre} lanza fuego!"

    def recibirDanio(self, danio):
        self.vida -= danio
        if self.vida < 0:
            self.vida = 0
        return f"{self.nombre} recibió {danio} de daño y le quedan {self.vida} de vida."

    def ataqueConSalto(self):
        return f"{self.nombre} ataca con un salto!"

    def comboAtaque(self):
        return f"{self.nombre} realiza un combo de ataques!"
