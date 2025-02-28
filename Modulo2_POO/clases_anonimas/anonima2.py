"""
Tienes la tarea de crear un formulario de usuario utilizando campos dinámicos. Cada formulario tendrá distintos campos que pueden ser especificados como una lista de nombres de campos (como nombre, edad, email, etc.). Tu objetivo es generar una clase anónima con los campos proporcionados y asignar valores a esos campos.
Instrucciones:
1.	Crea una función crear_formulario(campos) que reciba una lista de campos (como ['nombre', 'edad', 'email']) y cree una clase anónima Formulario con esos campos.
2.	Dentro de la clase generada, cada campo debe ser un atributo con un valor inicial de cadena vacía ("").
3.	Luego, crea un formulario utilizando la clase generada con la lista de campos proporcionada.
4.	Asigna valores a los campos del formulario (por ejemplo, formulario_obj.nombre = "Carlos" y muestra cada uno de los valores de los campos.

"""

def crear_formulario(campos):
  atributos= {campo: "" for campo in campos}  
  Formulario= type('Formulario', (object,), atributos)
  return Formulario

campos=["nombre","edad","email","Móvil"]

Formulario = crear_formulario(campos)

formulario_obj = Formulario()
formulario_obj.nombre = "Alfonso"
formulario_obj.edad = "40"
formulario_obj.email = "alfonso@gmail.com"
formulario_obj.movil = "3002563214"

print(f"Nombre: {formulario_obj.nombre}")
print(f"Edad: {formulario_obj.edad}")
print(f"Email: {formulario_obj.email}")
print(f"Móvil: {formulario_obj.movil}")