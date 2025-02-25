#Definir la clase persona
class Persona:
  #Método constructor
  def __init__(self,nombre,edad):
    self.nombre= nombre
    self.edad= edad
    
  #Método saludar
  def saludar(self):
    print("Hola!, mi nombre es, ",self.nombre,", tengo ",self.edad," años.")

#Crear un objeto de la clase
persona = Persona("Alfonso Cantillo",40)

#Usar el método saludar de la clase persona
persona.saludar()