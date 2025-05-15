edad = int(input("Ingrese su edad: "))

if edad.isdigit() and edad > 0:
  print(f"Usted tiene {edad} años")
else:
  print("Ingrese una edad valida")