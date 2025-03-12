try:
  numero = int(input("Ingreso numero: "))
  resultado = 10 / numero
except ValueError as e:
  print(f"Error: entrada invalida. {e}")
except ZeroDivisionError:
  print(f"Error: No se puede desarrollar una division entre cero")
else:
  print(f"El resultado es {resultado}")
finally: #Siempre se ejecuta
  print(f"Ejercicio finalizado")

