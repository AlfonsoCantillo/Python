"""
Patron de Diseño Singleton: 
Su propósito es garantizar que una clase tenga una única instancia y proporcionar un 
punto de acceso global a esa instancia. Es especialmente útil cuando se necesita controlar 
el acceso a algún recurso compartido, como una conexión a una base de datos, un registro de
configuración global, entre otros.
"""
class Singleton:
  _instancia = None

  @staticmethod
  def obtener_instancia():
    if Singleton.instancia is None:
      Singleton._instancia= Singleton()
    
    return Singleton._instancia

obj1= Singleton._instancia()
obj2= Singleton._instancia()

print (obj1 is obj2)