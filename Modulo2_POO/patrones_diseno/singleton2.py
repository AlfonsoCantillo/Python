class Singleton:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            # Si la instancia no existe, la creamos
            cls._instancia = super().__new__(cls)
        return cls._instancia

# Uso del Singleton
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # Esto imprimirá True, ya que s1 y s2 son la misma instancia.