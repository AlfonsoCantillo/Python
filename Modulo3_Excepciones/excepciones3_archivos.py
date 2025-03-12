try:
  with open("datos.txt","r") as archivo:
    contenido = archivo.read()
    numero = int(contenido.strip())
    resultado = 100 / numero
    print(f"El resultado es {resultado}")
except Exception as e:
  print(f"Error: {e}")