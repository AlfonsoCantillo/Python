try:
  numero = int(input("Ingrese un número: "))
  resultado = 10 / numero
  print(f"Resultado de la división es: {resultado}")
except ValueError:
  print("Ingrese un número valido.")
except ZeroDivisionError:
  print("No se puede dividir por cero.")
except Exception as e:
  print(f"Error no identificado: {e}") 
finally:
  print("Fin del programa")   