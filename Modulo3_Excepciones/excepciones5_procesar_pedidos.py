def procesar_pedido(codigo, cantidad):
  try:
    #Simular una validacion de datos
    if not codigo.isalnum():
      #raise ERROR: Gestiona de forma manual y en tiempo de ejecución un error
      raise ValueError("El código del producto debe ser Alfanúmerico")
    if cantidad <= 0:
      raise ValueError("La cantidad debe ser mayor a cero")

    #Simular el calculo total
    precio_unitario = 100
    total = precio_unitario * cantidad
  except ValueError as e:
    print(f"Error al procesar el pedido: {e}")
  else:
    print(f"El precio total del pedido es: {total:.2f}") #{total:.2f} = Parte entera y 2 decimales
  finally:
    print("Operación finalizada. registro actualizado")

# método principal

if __name__ == "__main__":
  procesar_pedido("01",5)
  procesar_pedido("02",1.36)