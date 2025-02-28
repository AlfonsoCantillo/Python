class Logger:
    _instancia = None
    _logs = []

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            # Si la instancia no existe, la creamos
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def agregar_log(self, mensaje):
        """Agrega un mensaje al registro de logs."""
        self._logs.append(mensaje)

    def mostrar_logs(self):
        """Muestra todos los logs registrados."""
        for log in self._logs:
            print(log)


# Uso del Singleton Logger
logger1 = Logger()
logger2 = Logger()

logger1.agregar_log("Iniciando aplicación")
logger1.agregar_log("Conexión exitosa a la base de datos")
logger2.agregar_log("Operación completada")

# Verificación de que logger1 y logger2 son la misma instancia
print(logger1 is logger2)  # Esto debería imprimir True

# Mostrar todos los logs
logger2.mostrar_logs()