def saludar(self):
  print(f"Hola mi nombre es: {self.nombre}")

Persona= type('Persona', (object,),{
  'nombre': 'Juan', #Atributo
  'saludar': saludar #Funcion de la clase
})

persona_objeto= Persona()
persona_objeto.saludar()
print(persona_objeto.nombre)