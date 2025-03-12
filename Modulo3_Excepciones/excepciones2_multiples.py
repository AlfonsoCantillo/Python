def division_segura():
  try:
    numerador = int(input("Ingrese el numerador:"))
    denominador= int(input("Ingrese el denominador:"))
    resultado = numerador/denominador
    print(f"El resultado de la división es {resultado}")
  except(ZeroDivisionError,ValueError) as e: #Manejo multiple de excepciones ValueError = excepcion general
    print(f"Error: {e}")

division_segura()