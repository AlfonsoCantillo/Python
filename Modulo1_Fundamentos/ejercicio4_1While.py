tabla = int(input("Digite la tabla a imprimir en pantalla:"))
if tabla >= 0 and tabla <= 10:
  i=1
  print("Tabla de Multiplicar del " + str(tabla))
  while i<11:
    if i==6:
      break
    resultado = i * tabla
    print(i,"x",tabla,"=",resultado)
    i+=1
else:
  print("Número incorrecto")

'''
Tabla de Multiplicar del 7
1 x 7 = 7
2 x 7 = 14
3 x 7 = 21
4 x 7 = 28
5 x 7 = 35
'''