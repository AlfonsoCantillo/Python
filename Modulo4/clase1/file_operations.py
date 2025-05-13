def leer_archivo(nombre_archivo):
    """Leer e imprimir el contenido de un archivo usando el modo 'r' (solo lectura)."""
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(f"Contenido de {nombre_archivo}:")
            print(contenido)
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no fue encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

def escribir_archivo(nombre_archivo, contenido):
    """Escribir contenido en un archivo usando el modo 'w' (modo escritura, crea nuevo archivo o sobreescribe existente)."""
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(contenido)
        print(f"Se escribió exitosamente en {nombre_archivo}")
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")

def anexar_archivo(nombre_archivo, contenido):
    """Añadir contenido a un archivo usando el modo 'a' (modo anexar, crea el archivo si no existe)."""
    try:
        with open(nombre_archivo, 'a') as archivo:
            archivo.write(contenido)
        print(f"Se anexó exitosamente a {nombre_archivo}")
    except Exception as e:
        print(f"Error al anexar al archivo: {e}")

def leer_escribir_archivo(nombre_archivo, nuevo_contenido):
    """Abrir un archivo en modo 'r+' (modo lectura y escritura, el archivo debe existir)."""
    try:
        with open(nombre_archivo, 'r+') as archivo:
            # Leer contenido actual
            contenido_actual = archivo.read()
            print(f"Contenido actual de {nombre_archivo}:")
            print(contenido_actual)
            
            # Mover al inicio del archivo y escribir nuevo contenido
            archivo.seek(0)
            archivo.write(nuevo_contenido)
            print(f"Se actualizó exitosamente {nombre_archivo}")
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no fue encontrado. El modo 'r+' requiere que el archivo exista.")
    except Exception as e:
        print(f"Error en la operación de lectura/escritura: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python file_operations.py <operacion>")
        print("Operaciones disponibles: leer, escribir, anexar, leer_escribir")
        sys.exit(1)
    
    operacion = sys.argv[1]
    archivo_prueba = "alfonso.txt"
    
    if operacion == "leer":
        # Leer el archivo
        leer_archivo(archivo_prueba)
        
    elif operacion == "escribir":
        # Escribir en un archivo
        escribir_archivo(archivo_prueba, "Hola, este es un archivo de prueba.\nLínea 2 del archivo de prueba.\n")
        
    elif operacion == "anexar":
        # Anexar al archivo
        anexar_archivo(archivo_prueba, "Esta línea fue anexada.\n")
        
    elif operacion == "leer_escribir":
        # Usar modo lectura y escritura
        leer_escribir_archivo(archivo_prueba, "Este contenido reemplaza todo en el archivo.\n")
        
    else:
        print(f"Error: Operación '{operacion}' no reconocida")
        print("Operaciones disponibles: leer, escribir, anexar, leer_escribir") 