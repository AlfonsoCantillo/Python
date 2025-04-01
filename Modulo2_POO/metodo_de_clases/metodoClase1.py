"""
Un método de clase: Es un tipo especial de método que se define dentro de una clase y 
tiene acceso a la propia clase, pero no a una instancia específica de esa clase. 
Esto significa que un método de clase puede modificar el estado de la clase, no de una instancia 
concreta.

Para definir un método de clase, se usa el decorador @classmethod

La principal diferencia entre un método de instancia y un método de clase es el primer parámetro, 
que en un método de clase es cls, en lugar de self. 
cls hace referencia a la clase en sí, mientras que self hace referencia a la instancia de la clase.
"""
#Ejemplo donde se usa un método de clase para crear una instancia de la clase de manera alternativa:
class Persona:
  #atributo de clase
  cantidad_personas = 0

  def __init__(self,nombre):
    self.nombre= nombre
    Persona.cantidad_personas += 1
  
  @classmethod
  def desde_nombre(cls,nombre):
    # Método de clase que crea una nueva instancia usando solo un nombre
    return cls(nombre)
  
  @classmethod
  def obtener_cantidad_personas(cls):
    # Método de clase para acceder a un atributo de clase
    return cls.cantidad_personas

# Crear una persona usando el método de clase
persona_1= Persona.desde_nombre("Juan")
persona_2= Persona.desde_nombre("Ana")
# Acceder a la cantidad de personas creadas
print(Persona.obtener_cantidad_personas())

"""
- desde_nombre: es un método de clase que crea una nueva instancia de la clase Persona
usando solo el nombre.

- obtener_cantidad_personas: es otro método de clase que devuelve la cantidad de instancias de
Persona creadas, accediendo al atributo de clase cantidad_personas.
"""