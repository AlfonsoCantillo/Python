class ErrorPago(Exception):
  pass

class PasarelaPago:
  @staticmethod
  def procesar_pago(numero_tarjeta, monto):
    if not numero_tarjeta.startswith("4"):
      raise ErrorPago("El número de la tarjeta no es valido. Debe iniciar con el número 4.")
    if monto <= 0:
      raise ErrorPago("El monto de la compra debe ser mayor a cero.")
    if len(numero_tarjeta) != 16:
      raise ErrorPago("El número de la tarjeta no es valido. Debe tener 16 digitos.")
    
    return f"El pago de ${monto} fur procesado con éxito."
  
def proceso_pago_cliente(nombre_cliente,numero_tarjeta,monto):
  try:
    print(f"Iniciando el proceso de pago de {nombre_cliente}")
    resultado = PasarelaPago.procesar_pago(numero_tarjeta,monto)
  except ErrorPago as e:
    print(f"Error al procesar el pago: {e}")
  except Exception as e:
    print(f"Error inesperado: {e}")
  else:
    print(resultado)
  finally:
    print("El registro de la transacción finalizo.")

if __name__ == "__main__":
  proceso_pago_cliente("Alfonso Cantillo","0563258974122589",-150000)
