from Mascota import Mascota

class Ninja(Mascota):
    def __init__ (self,nombre,apellido,nombre_mascota,premio,comida_mascota):
        super().__init__(nombre_mascota,premio)
        self.nombre = nombre
        self.apellido = apellido
        self.comida_mascota=comida_mascota
    
    def caminar(self):
        super().jugar()
    
    def alimentar(self):
        super().comer()
        print("me diste de comer:",self.comida_mascota)
    
    def bañar(self):
        super().ruido()
    
    

    
            
    
        
        
    