"""
Patron de Diseño Singleton: 
Su propósito es garantizar que una clase tenga una única instancia y proporcionar un 
punto de acceso global a esa instancia. Es especialmente útil cuando se necesita controlar 
el acceso a algún recurso compartido, como una conexión a una base de datos, un registro de
configuración global, entre otros.
"""

class Logger:
  _instance = None

  # Método __new__ para garantizar que solo se cree una instancia
  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      print("Creando la instancia de Logger")
      cls._instance = super(Logger, cls).__new__(cls)
    return cls._instance

  def __init__(self):
    # Si la instancia ya está creada, evitamos la re-inicialización
    if not hasattr(self, 'initialized'):
      self.initialized = True
      self.logs = []

  def log(self, message):
    self.logs.append(message)

  def show_logs(self):
    return "\n".join(self.logs)


# Uso del Singleton:
logger1 = Logger()
logger1.log("Iniciando el sistema.")
logger1.log("Error en el sistema.")

logger2 = Logger()  # Esta instancia es la misma que logger1
logger2.log("Error al conectar a la base de datos.")

print(f"¿Ambas instancias son iguales? {logger1 is logger2}")  # Esto será True
print("Logs del sistema:")
print(logger2.show_logs())  # Muestra todos los logs que se registraron