"""
Interface: Es un contrato o un conjunto de métodos que una clase debe implementar. 
Define un conjunto de métodos abstractos, es decir, métodos que no tienen una implementación en
la interfaz misma, pero que las clases que implementan la interfaz deben definir.
"""
from abc import ABC, abstractmethod #Importacion para crear un metodo abstracto

class Vehiculo_interface(ABC): #Definición de la Interfaz
  @abstractmethod
  def mover(self): #Definición de un método abstracto, sin implementación
    pass

class Carro(Vehiculo_interface): #Crear clase hija Carro()
  def mover(self):
    print("El carro se está conduciendo por carretera")
  
class Bicicleta(Vehiculo_interface): #Crear clase hija Bicicleta
  def mover(self):
    print("La bicicleta tiene dos llantas")

vehiculos=[Carro(),Bicicleta()] #Crear una lista, para instanciar las clases hijas

for vehiculo in vehiculos: #Recorrer la lista
  vehiculo.mover() #Llamar el método mover() de cada clase hija instanciada

