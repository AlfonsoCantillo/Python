class Animal:
  def __init__(self, nombre:str, edad:int):
    self.nombre= nombre
    self.edad= edad
  
  def hablar(self):
    print("El animal hace un sonido")

class Perro(Animal):
  def __init__(self, nombre, edad, raza):
    super().__init__(nombre,edad)
    self.raza= raza
  
  def hablar(self):
    print(f"{self.nombre} dice ¡Guaau!")

perro= Perro("Rex",2,"Labrador")

print(perro.nombre)
print(perro.edad)
print(perro.raza)

perro.hablar()
