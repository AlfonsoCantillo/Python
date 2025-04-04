import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG)

@dataclass
class Vendedor:
  nombre: str
  ventas_totales: float

  def calcular_comision(self) -> float:
    if self.ventas_totales > 10000:
      comision = self.ventas_totales * 0.10
      logging.debug(f"{self.nombre} ha alcanzado el umbral de ventas. Comisión de: {comision}")
    else:
      comision = self.ventas_totales * 0.05
      logging.debug(f"{self.nombre} No ha alcanzado el umbral de ventas. Comisión de: {comision}")
    
    return comision

if __name__ == "__main__":
  vendedor1 = Vendedor("Alfonso",20000)
  vendedor2= Vendedor("Luis",5000)

  print(f"{vendedor1.calcular_comision()}")
  print(f"{vendedor2.calcular_comision()}")