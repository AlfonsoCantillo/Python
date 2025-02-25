import os

class Coche:
  def __init__(self,marca,modelo,anio):
    self.marca= marca
    self.modelo= modelo
    self.anioFabricacion= anio
  
  def informacion(self):
    os.system("cls")
    print("Descripción del coche:\n Marca: ",self.marca,"\n Modelo: ",self.modelo,"\n Año de Fabricación:", self.anioFabricacion)

coche = Coche("Toyota","Corolla","2020")

coche.informacion()
