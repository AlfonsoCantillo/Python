import os

class Coche:
  def __init__(self,marca,modelo,anio):
    self.__marca= marca
    self.__modelo= modelo
    self.__anio= anio
  
  def getMarca(self):
    return self.__marca
  
  def getModelo(self):
    return self.__modelo
  
  def getAnio(self):
    return self.__anio
  
  def setAnio(self,nuevoAnio):
    if self.__anio < nuevoAnio:
      self.__anio= nuevoAnio
      return self.__anio
    else:
      print ("El año digitado ("+str(nuevoAnio)+"), no puede ser menor al actual ("+str(self.__anio)+")")
  
  def saludar(self):
    print ("Hola, soy un {", self.__marca +"}{" , self.__modelo , "} del año {",str(self.__anio),"}")

os.system("cls")

coche1 = Coche("Toyota","Corolla",2020)

coche1.saludar()

coche1.setAnio(2019)
coche1.saludar()

print(coche1.getAnio())
