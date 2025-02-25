class Carro:
  def conducir(self):
    print("El carro esta en marcha")

class Bicicleta:
  def conducir(self):
    print("La bicicleta está pedaliando")

class Vehiculofactory:
  @staticmethod
  def crear_vehiculo(tipo):
    if tipo == 'carro':
      return Carro()
    elif tipo == 'bicicleta':
      return Bicicleta()
    else:
      return False

tipoVehiculo= 'BiciCleta'
vehiculo1= Vehiculofactory.crear_vehiculo(tipoVehiculo.lower())
if vehiculo1 == False:
  print("Vehículo no identificado")
else:
  vehiculo1.conducir()