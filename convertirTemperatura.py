"""
Crea un programa que convierta una temperatura de grados Celsius a grados Fahrenheit y viceversa.
Instrucciones:
1.	Pide al usuario que ingrese una temperatura y la unidad (Celsius o Fahrenheit).
2.	Realiza la conversión.
3.	Muestra el resultado.
"""
#Funcion para convertir grados celsius a fahrenheit
def celsiusAFahrenheit(temperatura):
  fahrenheit = (temperatura * 9/5) + 32
  return round(fahrenheit,2)

#Funcion para convertir grados fahrenheit a celsuis
def fahrenheitACelsius(temperatura):
  celsius = (temperatura - 32)* 5/9
  return round(celsius,2)

opcion = 0
while opcion != 3:  
  print("-----------------------------------------------")
  print("                  MENU DE OPCIONES")
  print("-----------------------------------------------")
  print("[1] Convertir grados Celcius a Fahrenheit.")
  print("[2] Convertir grados Fahrenheit a Celcius.")
  print("[3] Salir")
  try:
    opcion = int(input("Digite opción: "))
    if (opcion in(1,2)):    
      temperatura= float(input("Digite la temperatura: "))
      if (opcion == 1):
        resultado = celsiusAFahrenheit(temperatura)
        print (temperatura,"°C es igual a ",resultado,"°F")
      elif (opcion == 2):
        resultado = fahrenheitACelsius(temperatura)
        print (temperatura,"°F es igual a ",resultado,"°C")
    elif (opcion == 3):
      print("Gracias por utilizar nuestros servicios.")  
    else:
      print("La opción digitada es invalida")  
  except:
    print("La opción/temperatura digitada es invalida")

