"""
Los métodos estáticos: Son aquellos que pertenecen a la clase y no a una instancia específica
de esa clase. Esto significa que un método estático no tiene acceso directo a la instancia de la 
clase (es decir, no recibe el parámetro self que se usa en los métodos normales de instancia). 
Tampoco tiene acceso directo a las variables de instancia de la clase, pero puede acceder a las
variables de clase (si son accesibles).

Los métodos estáticos son útiles cuando necesitas una función que realice una tarea que está 
relacionada con la clase pero no depende de la instancia específica de esa clase.

Para definir un método estático en Python, se utiliza el decorador @staticmethod
"""
class Calculadora:
  @staticmethod
  def suma(a, b):
      return a + b

  @staticmethod
  def resta(a, b):
      return a - b

#Llamado desde la clase:
resultado_suma = Calculadora.suma(5, 3)
print(resultado_suma)  # Imprime: 8    

print("-----------------------------------")    

#Llamado desde una instancia:
calc = Calculadora()
resultado_resta = calc.resta(10, 4)
print(resultado_resta)  # Imprime: 6