from abc import ABC, abstractmethod

# Interfaz común para los vehículos
class Vehiculo(ABC):
    @abstractmethod
    def crear(self):
        pass

# Clases concretas de vehículos
class Coche(Vehiculo):
    def crear(self):
        return "Coche creado."

class Bicicleta(Vehiculo):
    def crear(self):
        return "Bicicleta creada."

# Fábrica para crear vehículos
class FabricaVehiculos:
    @staticmethod
    def crear_vehiculo(tipo: str) -> Vehiculo:
        """Método de fábrica que retorna una instancia de la clase adecuada"""
        if tipo == "coche":
            return Coche()
        elif tipo == "bicicleta":
            return Bicicleta()
        else:
            raise ValueError("Tipo de vehículo no soportado.")

# Uso del patrón Factory
if __name__ == "__main__":
    tipo_vehiculo = input("Ingrese el tipo de vehículo (coche/bicicleta): ").lower()

    vehiculo = FabricaVehiculos.crear_vehiculo(tipo_vehiculo)
    print(vehiculo.crear())
