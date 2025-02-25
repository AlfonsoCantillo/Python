"""
Patrón Factory
El patrón Factory es utilizado para crear objetos sin exponer la lógica de creación al cliente
y permite crear instancias de diferentes clases mediante un método común.
"""
class Animal:
  def hablar(self):
    pass

class Perro(Animal):
  def hablar(self):
    return "Guau!"

class Gato(Animal):
  def hablar(self):
    return "Miauuu!"

class AnimalFactory:
  def crear_animal(self, tipoAnimal):
    if tipoAnimal == "perro":
        return Perro()
    elif tipoAnimal == "gato":
        return Gato()
    else:
        return None

# Uso
factory = AnimalFactory()
animal = factory.crear_animal("perro")

if animal is None:
  print("Animal no identificado")
else:
  print(animal.hablar())  # Salida: Guau!