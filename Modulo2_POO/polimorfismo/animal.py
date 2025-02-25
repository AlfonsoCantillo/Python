class Animal:
  def hacerSonido(self):
    """
    Cuando se realiza un metodo que no tiene implementyación utilizo la palabra pass, 
    para que el compilador no me muestre error
    """
    pass   

class Perro(Animal):
  def hacerSonido(self):
    print("Guaau")

class Gato(Animal):
  def hacerSonido(self):
    print("Miauu")

class Gallina(Animal):
  def hacerSonido(self):
    print("Clo clo")


print("---------------------\n")

animales= [Perro(),Gato(),Gallina()]

for animal in animales:
  animal.hacerSonido()