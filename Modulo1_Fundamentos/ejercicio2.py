'''
Primera infancia entre 0 y 5 años
Infancia entre 6 y 13 años
Adolecencia entre 14 y 17
18+ Adultos
'''

edad = int(input("Ingrese su edad:"))
if edad < 0:
  print("La edad digitada no es valida")
  print("Digite una edad valida")
else:
  if edad < 6:
    print("Primera infancia")
  elif edad >=6 and edad<=13:
    print("Infancia")
  elif edad >= 14 and edad <= 17:
    print ("Adolecencia")
  else:
    print("Adulto")