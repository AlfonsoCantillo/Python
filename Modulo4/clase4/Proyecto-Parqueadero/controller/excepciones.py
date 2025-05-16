# excepciones.py

class VehiculoYaExisteException(Exception):
    """Se lanza cuando un vehículo ya está registrado en el sistema."""
    def __init__(self, placa):
        mensaje = f"El vehículo con placa {placa} ya se encuentra en el parqueadero."
        super().__init__(mensaje)


class VehiculoNoEncontradoException(Exception):
    """Se lanza cuando no se encuentra un vehículo por placa."""
    def __init__(self, placa):
        mensaje = f"El vehículo con placa {placa} no está registrado en el sistema."
        super().__init__(mensaje)


class TipoVehiculoInvalidoException(Exception):
    """Se lanza cuando el tipo de vehículo no es válido o no tiene tarifa asignada."""
    def __init__(self, tipo):
        mensaje = f"Tipo de vehículo '{tipo}' no válido o sin tarifa configurada."
        super().__init__(mensaje)


class ErrorTarifaException(Exception):
    """Se lanza cuando no se puede obtener la tarifa para un vehículo."""
    def __init__(self, mensaje="Error al obtener la tarifa del vehículo."):
        super().__init__(mensaje)


class ParametroNoEncontradoException(Exception):
    """Se lanza cuando no se encuentra un parámetro general por su llave."""
    def __init__(self, llave):
        mensaje = f"No se encontró el parámetro con llave '{llave}'."
        super().__init__(mensaje)
