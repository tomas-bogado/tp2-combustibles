import os
from datetime import datetime
from fuentes import cargar_csv, cargar_json
from datetime import datetime

def normalizar_precios(registros):
    """
    Convierte las fechas a objetos datetime reales y los precios a números decimales (float),
    registrando tanto los datos limpios como las filas rechazadas por errores de formato.
    """
    registros_normalizados = []
    rechazados = []
   
    for fila in registros:
        fila_limpia = fila.copy()
        
        try:
            # 1. Convertir precio a float
            precio_str = str(fila_limpia.get("precio", 0)).replace(",", ".")
            fila_limpia["precio"] = float(precio_str)
            
            # 2. Convertir fecha a datetime
            fecha_str = fila_limpia.get("fecha")
            if fecha_str:
                fila_limpia["fecha"] = datetime.strptime(fecha_str.strip(), "%d-%m-%Y")
            
            registros_normalizados.append(fila_limpia)
            
        except (ValueError, TypeError) as e:
            # Registramos la fila rechazada junto al motivo del error
            fila_con_error = fila.copy()
            fila_con_error["motivo_rechazo"] = str(e)
            rechazados.append(fila_con_error)
            
    return registros_normalizados, rechazados

if __name__ == "__main__":
    # Prueba rápida del pipeline de normalización
    datos_crudos = cargar_csv()
    print(f"Registros crudos leídos: {len(datos_crudos)}")
    
    datos_limpios, rechazos = normalizar_precios(datos_crudos)
    print(f"Registros normalizados con éxito: {len(datos_limpios)}")
    if datos_limpios:
        print("Ejemplo de registro normalizado:", datos_limpios[0])

    datos_json_crudos = cargar_json()
    datos_json_limpios, rechazos_json = normalizar_precios(datos_json_crudos)
    print(f"JSON normalizados con éxito: {len(datos_json_limpios)}")