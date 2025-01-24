#Filtre la matriz y devuelva una nueva matriz con solo los valores iguales o Mayores de 18 años:

edades = [5, 12, 17, 18, 24, 32]

def mayorEdad(x):
  if x < 18:
    return False
  else:
    return True

adultos = filter(mayorEdad, edades)

for x in adultos:
  print(x)