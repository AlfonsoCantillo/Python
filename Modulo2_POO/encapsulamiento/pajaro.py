class Pajaro:
  #Atributos de la clase. Globales
  alas = True

  #Atributos de la instancia
  def __init__(self,color,especie,pico):
    self.color= color
    self.especie= especie
    self.pico= pico
  
  def sonido(self):
    print("Pajaro realizando un sonido")

  
class Pollo(Pajaro):  
  def sonido(self):
    print(f"El pollo esta piando")

#Crear el objeto Pajaro
piolin= Pajaro('Amarillo','Canario','Largo')

print(f"Color: {piolin.color}, Especie: {piolin.especie}, Tipo pico: {piolin.pico}")

print("------------------------------")

pollo = Pollo('Amarillo','Gallináceas','corto')

print(f"Color: {pollo.color}, Especie: {pollo.especie}, Tipo pico: {pollo.pico}")

pollo.sonido()

print("------------------------------")
super(Pollo,pollo).sonido()