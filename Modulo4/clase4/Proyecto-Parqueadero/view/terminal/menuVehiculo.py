
from controller.vehiculosController import vehiculosController
import datetime 

class MenuVehiculo:
  def __init__(self):
    self.controller_vehiculos = vehiculosController()
  
  def mostrar_menu(self):
    while True:
      print("1. Ingresar vehículo")
      print("2. Actualizar vehículos")
      print("3. Eliminar vehículos")
      print("4. Ver vehículos")
      print("0. Salir")
      opcion = input("Ingrese una opción: ")  
      if opcion == "1":
        self.ingresar_vehiculo()
      elif opcion == "2":
        self.actualizar_vehiculo()        
      elif opcion == "3":
        self.eliminar_vehiculo()        
      elif opcion == "4":
        self.ver_vehiculos()        
      elif opcion == "0":
        print("Saliendo")
        break
      else:
        print("Opción invalida")
      
  def ingresar_vehiculo(self):
    placa = input("Ingrese la placa: ")  
    tipoVehiculo = input("Ingrese el tipo de vehículo: ")
    fechaIngreso = datetime.datetime.now()
    resultado= self.controller_vehiculos.grabar_vehiculo(placa,tipoVehiculo,fechaIngreso)
    print(resultado['mensaje'])

  def ver_vehiculos(self):
    vehiculos = self.controller_vehiculos.obtener_vehiculos_todos()
    print(vehiculos)
  
  def actualizar_vehiculo(self):
    placa = input("Ingrese la placa del vehiculo que desea actualizar: ")  
    if self.controller_vehiculos.obtener_vehiculos_uno(placa):
      tipoVehiculo = input("Ingrese el tipo de vehículo: ")
      fechaIngreso = datetime.datetime.now()
      resultado = self.controller_vehiculos.modificar_vehiculo(placa,tipoVehiculo,fechaIngreso)
      print(resultado['mensaje'])
    else:
      print(f"El vehículo con placas {placa}, no se encuentra al interior del parqueadero.")

  def eliminar_vehiculo(self):
    placa = input("Ingrese la placa del vehiculo que desea eliminar: ")  
    if self.controller_vehiculos.obtener_vehiculos_uno(placa):      
      resultado = self.controller_vehiculos.eliminar_vehiculo(placa)
      print(resultado['mensaje'])
    else:
      print(f"El vehículo con placas {placa}, no se encuentra al interior del parqueadero.")
    