class Carro:
  def obtener_tipo(self):
    return "carro"
  
class FabricaCarro:  
  def crear_vehiculo(self):
    return Carro()
  
def Cliente():
  fabrica= FabricaCarro()
  vehiculo= fabrica.crear_vehiculo()
  print(f"Se ha creado un vehículo de tipo: {vehiculo.obtener_tipo()}")

#Ejecutar cliente
Cliente()
