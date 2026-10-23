import os
from datetime import datetime
from fuentes import cargar_csv, cargar_json

def normalizar_precios(registros):
    """
    Convierte las fechas a objetos datetime reales y los precios a números decimales (float),
    asegurando que los datos queden listos para ser analizados sin errores de tipo.
    """
    registros_normalizados = []
    
    for fila in registros:
        # Hacemos una copia de la fila para no modificar el diccionario original crudo
        fila_limpia = fila.copy()
        
        try:
            # 1. Convertir el precio de texto a float (número con decimales)
            # Reemplazamos posibles comas por puntos por si viene con formato europeo/latino
            precio_str = str(fila_limpia.get("precio", 0)).replace(",", ".")
            fila_limpia["precio"] = float(precio_str)
            
            # 2. Convertir la fecha de texto (ej: "10-05-2026") a un objeto fecha real de Python
            fecha_str = fila_limpia.get("fecha")
            if fecha_str:
                # Intentamos parsear la fecha en formato DD-MM-YYYY
                fila_limpia["fecha"] = datetime.strptime(fecha_str.strip(), "%d-%m-%Y")
                
            registros_normalizados.append(fila_limpia)
            
        except (ValueError, TypeError) as e:
            # Si hay un error de formato en el precio o la fecha, registramos o filtramos la fila
            print(f"Advertencia: Se descartó un registro por formato inválido. Detalle: {e}")
            
    return registros_normalizados

if __name__ == "__main__":
    # Prueba rápida del pipeline de normalización
    datos_crudos = cargar_csv()
    print(f"Registros crudos leídos: {len(datos_crudos)}")
    
    datos_limpios = normalizar_precios(datos_crudos)
    print(f"Registros normalizados con éxito: {len(datos_limpios)}")
    if datos_limpios:
        print("Ejemplo de registro normalizado:", datos_limpios[0])

    datos_json_crudos = cargar_json()
    datos_json_limpios = normalizar_precios(datos_json_crudos)
    print(f"JSON normalizados con éxito: {len(datos_json_limpios)}")