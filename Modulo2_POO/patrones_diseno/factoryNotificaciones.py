"""
Ejemplo: Sistema de Notificaciones con Factory
Imaginemos que tenemos un sistema que necesita enviar notificaciones de diferentes tipos 
(por ejemplo, Email, SMS, Notificación Push), y queremos crear un Factory que se encargue de 
instanciar la clase adecuada según el tipo de notificación.
"""

from abc import ABC, abstractmethod

# Interfaz común para las notificaciones
class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje: str):
        pass

# Clase concreta para Notificación por Email
class NotificacionEmail(Notificacion):
    def enviar(self, mensaje: str):
        print(f"Enviando correo electrónico: {mensaje}")

# Clase concreta para Notificación por SMS
class NotificacionSMS(Notificacion):
    def enviar(self, mensaje: str):
        print(f"Enviando SMS: {mensaje}")

# Clase concreta para Notificación Push
class NotificacionPush(Notificacion):
    def enviar(self, mensaje: str):
        print(f"Enviando notificación push: {mensaje}")

#Crear la Fabrica
class FabricaNotificaciones:
  @staticmethod
  def crear_notificacion(tipo: str) -> Notificacion:
      """Método de fábrica que retorna una instancia de la clase adecuada"""
      if tipo == "email":
          return NotificacionEmail()
      elif tipo == "sms":
          return NotificacionSMS()
      elif tipo == "push":
          return NotificacionPush()
      else:
          raise ValueError("Tipo de notificación no soportado.")

#Uso del patron factory
def enviar_mensaje(tipo: str, mensaje: str):
    # Usamos la fábrica para obtener la notificación adecuada
    notificacion = FabricaNotificaciones.crear_notificacion(tipo)
    notificacion.enviar(mensaje)

# Ejemplo de uso
if __name__ == "__main__":
    enviar_mensaje("email", "Este es un correo electrónico de prueba.")
    enviar_mensaje("sms", "Este es un mensaje de texto de prueba.")
    enviar_mensaje("push", "Este es una notificación push de prueba.")      
