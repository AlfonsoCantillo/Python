def sumar(num1,num2):
  resultado = num1 + num2
  return resultado

def restar(num1,num2):
  resultado = num1 - num2  
  return resultado

def multiplicar(num1,num2):
  resultado = num1 * num2  
  return resultado

def dividir(num1,num2):
  if(num2 != 0):
    resultado = num1 / num2  
  else:
    resultado = "Error"
  return resultado

sw = 0
while sw == 0:
  print("Operaciones Matemáticas")
  print("[1] Sumar")
  print("[2] Restar")
  print("[3] Multiplicar")
  print("[4] Dividir")
  print("[0] Salir")
  op = int(input("Digite la operación que quiere realizar: "))
  if (op == 0):
    sw = 1
  elif (op in(1,2,3,4,0)):
    n1 = float(input("Digite el numero 1: "))
    n2 = float(input("Digite el numero 2: "))
    if (op == 1):
      operacion= "Suma"
      resultado= sumar(n1,n2)
    elif (op == 2):
      operacion= "Resta"
      resultado= restar(n1,n2)
    elif (op == 3):
      operacion= "Multiplicación"
      resultado= multiplicar(n1,n2)
    elif (op == 4):
      operacion= "División"
      resultado= dividir(n1,n2)

    print("El resultado de la ",operacion,"es: ",resultado)
  else:
    print("Opción incorrecta")