import pandas as pd

print(f"Pandas versión: {pd.__version__}")

# Crear un DataFrame simple
data = {
    'nombre': ['Juan', 'Maria', 'Pedro', 'Ana'],
    'edad': [20, 21, 22, 23]
}

df = pd.DataFrame(data)
print(df) 