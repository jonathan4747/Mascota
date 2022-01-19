class Mascota:
    def __init__(self, nombre_mascota="N/A",premio="N/A",tipo="N/A",salud=0,energia=0):
        self.nombre_mascota = nombre_mascota
        self.premio=premio
        self.tipo = tipo
        self.salud= salud
        self.energia=energia
    def domir(self):
        self.energia += 25
    def comer(self):
        self.energia +=5
        self.salud +=10
        print("estoy comiendo:",self.premio)
    def jugar(self):
        self.salud +=5
    def ruido (self):
        print("ronquido")
    