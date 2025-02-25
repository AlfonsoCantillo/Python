#Ejemplo Encapsulamiento
class Perro:
  def __init__(self,nombre):
    self.__nombre= nombre
  
  def obtenerNombre(self):
    return self.__nombre
  
  def cambiarNombre(self,nuevoNombre):
    self.__nombre= nuevoNombre

perro1= Perro("Rex")
print("Perro 1:",perro1.obtenerNombre())

perro1.cambiarNombre("Max")
print("Perro 2:",perro1.obtenerNombre())