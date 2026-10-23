import csv
import json
import os

# Os.path verifica si el archivo físico realmente existe en la ruta para evitar que el programa se rompa por error
# csv.DictReader recorre el archivo CSV línea por línea y convierte cada fila en un diccionario usando los encabezados como claves
def cargar_csv(ruta_archivo="data/combustibles.csv"):
    """
    Lee el archivo CSV de combustibles y devuelve una lista de diccionarios.
    """
    registros = []
    if not os.path.exists(ruta_archivo):
        print(f"Error: No se encontró el archivo en {ruta_archivo}")
        return registros

    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            registros.append(fila)
            
    return registros

# Lee todo el archivo JSON y lo traduce automáticamente a una lista de diccionarios de Python
def cargar_json(ruta_archivo="data/combustibles.json"):
    """
    Lee el archivo JSON de combustibles y devuelve una lista de diccionarios.
    """
    if not os.path.exists(ruta_archivo):
        print(f"Error: No se encontró el archivo en {ruta_archivo}")
        return []

    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        registros = json.load(archivo)
            
    return registros

if __name__ == "__main__":
    # Prueba rápida para verificar la lectura
    datos_csv = cargar_csv()
    print(f"CSV cargado con éxito: {len(datos_csv)} registros leídos.")
    
    datos_json = cargar_json()
    print(f"JSON cargado con éxito: {len(datos_json)} registros leídos.")