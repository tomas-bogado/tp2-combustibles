import os
from fuentes import cargar_csv, cargar_json
from pipeline import normalizar_precios
from analisis import ConsultaPrecio, seleccionar_vigentes, buscar_estaciones, exportar_consulta

def ejecutar_aplicacion():
    print("=== EJECUTANDO BUSCADOR DE PRECIOS DE COMBUSTIBLES ===")
    
    # Obtener la ruta absoluta del directorio actual (src/) y la raíz del proyecto
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))      # carpeta src/
    ROOT_DIR = os.path.dirname(BASE_DIR)                       # carpeta raíz (tp2-combustibles)
    
    ruta_csv = os.path.join(ROOT_DIR, "data", "combustibles.csv")
    ruta_json = os.path.join(ROOT_DIR, "data", "combustibles.json")
    
    localidad_consulta = "Rosario"
    combustible_consulta = "nafta super"
    fecha_referencia = "23-10-2026"
    
    # Probamos ambos formatos de forma secuencial para cumplir con la consigna
    formatos = ["csv", "json"]

    try:
        consulta = ConsultaPrecio(localidad_consulta, combustible_consulta, fecha_referencia)
        print(f"[OK] Parámetros validados: {consulta.localidad} | {consulta.combustible} | Ref: {consulta.fecha_referencia}")

        for formato in formatos:
            print(f"\n----------------------------------------")
            if formato == "csv":
                print("[INFO] Leyendo desde fuente CSV...")
                if os.path.exists(ruta_csv):
                    datos_crudos = cargar_csv(ruta_csv)
                else:
                    print(f"[AVISO] No se encontró {ruta_csv}")
                    continue
            else:
                print("[INFO] Leyendo desde fuente JSON...")
                if os.path.exists(ruta_json):
                    datos_crudos = cargar_json(ruta_json)
                else:
                    print(f"[AVISO] No se encontró {ruta_json}")
                    continue
                
            print(f"[OK] Lectura exitosa: {len(datos_crudos)} registros cargados.")

            datos_limpios, rechazos = normalizar_precios(datos_crudos)
            print(f"[OK] Pipeline aplicado: {len(datos_limpios)} válidos, {len(rechazos)} rechazados.")

            datos_vigentes = seleccionar_vigentes(datos_limpios, consulta.fecha_referencia)
            print(f"[OK] Registros vigentes filtrados: {len(datos_vigentes)}")

            resultados = buscar_estaciones(datos_vigentes, consulta.localidad, consulta.combustible)

            print(f"\n--- RESULTADOS ORDENADOS PARA {consulta.localidad} ({formato.upper()}) ---")
            if not resultados:
                print("No se encontraron estaciones para los criterios indicados.")
            else:
                for idx, r in enumerate(resultados, start=1):
                    print(f"{idx}. Estación: {r.get('estacion')} | Precio: ${r.get('precio')} | Vigencia: {r.get('fecha')}")
                
                # Asegurar que outputs exista y exportar
                output_dir = os.path.join(ROOT_DIR, "outputs")
                os.makedirs(output_dir, exist_ok=True)
                exportar_consulta(resultados, os.path.join(output_dir, f"resultado_consulta_{formato}.csv"))
                print(f"[OK] Reporte exportado: resultado_consulta_{formato}.csv")

    except Exception as e:
        print(f"[ERROR EN LA APLICACIÓN]: {e}")

if __name__ == "__main__":
    ejecutar_aplicacion()