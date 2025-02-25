class Vehiculo:
  def __init__(self,marca):
    self.marca= marca
  
  def mostrar_info(self):
    print(f"Vehículo de la marca: {self.marca}")

class Coche(Vehiculo):
  #def __init__(self, marca):
    #super().__init__(marca)

  def mostrar_info(self):
    print(f"Coche de la marca: {self.marca}")

class Moto(Vehiculo):
  #def __init__(self, marca):
    #super().__init__(marca)

  def mostrar_info(self):
    print(f"Moto de la marca: {self.marca}")

vehiculos= [Coche("Chevrolet"),Moto("AKT")]

for vehiculo in vehiculos:
  vehiculo.mostrar_info()