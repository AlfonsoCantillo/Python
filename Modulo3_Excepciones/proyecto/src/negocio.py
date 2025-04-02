from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Vendedor(ABC): #Implementación clase abstracta para definir la clase vendedor
  nombre: str
  ventas: float

  @abstractmethod
  def calcular_comision(self) -> float:
    pass

@dataclass
class VendedorBase(Vendedor):
  #Implementación de un vendedor con una comisión del 10%
  def calcular_comision(self) -> float:
    return self.ventas * 0.10

@dataclass
class VendedorPremium(Vendedor):
  #Implementación concreta de un vendedor con una comisión del 15%
  def calcular_comision(self) -> float:
    return self.ventas * 0.15
