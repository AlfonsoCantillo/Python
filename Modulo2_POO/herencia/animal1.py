class Animal:
  def __init__(self,nombre,edad):
    self.nombre= nombre
    self.edad= edad

  def hablar(self):
    print("El animal hace un sonido")
  
  def informacion(self):
    print(f"Esta es la información del Animal: \nNombre: {self.nombre},\nEdad: {self.edad} años")

class Gato(Animal):
  def __init__(self, nombre, edad, raza):
    super().__init__(nombre, edad)
    self.raza= raza

  def hablar(self):
    print(f"{self.nombre} ¡Maulla!")
  
  def ronronear(self):
    print(f"{self.nombre} esta ronroneando.")
  
  def informacion(self):
    super().informacion() #LLamar el metodo informacion de la super clase
    print(f"Raza: {self.raza}")    
  
gato= Gato("Tom",2,"Americano")

gato.informacion()

gato.hablar()

gato.ronronear()

super(Gato,gato).hablar() #Esto ejecuta el metodo hablar de la superclase