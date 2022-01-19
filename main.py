from Mascota import Mascota
from Ninja import Ninja

nombre=input("tu nombre ninja: ")
apellido = input("tu apellido ninja: ")
nombre_mascota= input("el nombre de su mascota: ")
premio=input("dale de comer a tu mascota: ")
comida_mascota=input("comida frecuente de tu mascota: ")
Jonathan=Ninja(nombre, apellido, nombre_mascota, premio, comida_mascota)


Jonathan.alimentar()
Jonathan.bañar()

