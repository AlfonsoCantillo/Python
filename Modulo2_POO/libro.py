"""
Ejercicio: Clase Libro
Objetivo:
Crear una clase llamada Libro que represente un libro. 
Cada libro tiene un título, un autor y un número de páginas. 
Luego, crea una instancia de la clase Libro y accede a sus atributos.
Instrucciones:
1.	Crea una clase llamada Libro que tenga un método constructor (__init__) para inicializar los 
atributos titulo, autor y paginas del libro.
2.	Dentro de la clase, crea un método llamado descripcion() que imprima una breve descripción del 
libro, incluyendo el título, el autor y el número de páginas.
3.	Luego, crea una instancia de la clase Libro con datos de ejemplo (por ejemplo, un libro con 
título "Python para Todos", autor "Juan Pérez" y 250 páginas).
Finalmente, accede a los atributos de esa instancia para imprimirlos en la consola y llama al 
método descripcion() para mostrar la descripción del libro.
"""
#Definir la clase Libro
class Libro:
  #Método constructor
  def __init__(self,titulo,autor,numeroPaginas):
    self.titulo = titulo
    self.autor = autor
    self.numeroPaginas = numeroPaginas
  #Método descripción
  def descripcion(self):
    print("Descripción del libro:\n Título: ",self.titulo,"\n Autor: ",self.autor,"\n Número de Páginas :", self.numeroPaginas," páginas")

#Instanciar la clase libro
libro = Libro("Python para Todos","Juan Pérez",250)

#LLamar al método descripción de la clase libro
libro.descripcion()