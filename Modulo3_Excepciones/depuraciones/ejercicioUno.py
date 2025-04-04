import pdb
from abc import ABC, abstractmethod
from dataclasses import dataclass

#Clase abstracta empleado
@dataclass
class Empleado(ABC):
  nombre: str
  salario_base: float

  @abstractmethod
  def calcular_salario(self):
    pass

@dataclass
class Manager(Empleado):

  def calcular_salario(self):
    return self.salario_base + 5000
  

@dataclass
class Developer(Empleado):

  def calcular_salario(self):
    return self.salario_base + 2000
  
def calcular_salario(empleado: Empleado) -> float:
  pdb.set_trace()
  return empleado.calcular_salario()

if __name__ == "__main__":
  manager = Manager("Luis", 5000)
  developer = Developer("Alfonso", 2000)

  print(f"Salario Total Manager: {manager.calcular_salario()}")
  print(f"Salario Total Developer: {developer.calcular_salario()}")

  #n = next =>avanzar siguiente linea
  #s = step =>brinca a la siguiente funcion
  #c = continue =>se detiene hasta la siguiente pausa o finaliza
  #p = variable =>Imprime el valor de una variable