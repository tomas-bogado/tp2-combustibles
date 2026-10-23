import re
from datetime import datetime
import csv

class ConsultaPrecio:
    """Clase que modela, valida y encapsula los parámetros de la consulta de precios (Formato AR: DD-MM-YYYY)."""
    
    def __init__(self, localidad: str, combustible: str, fecha_referencia: str):
        # [Tarea: Normalización de localidad] Limpia espacios y capitaliza el texto
        self.localidad = localidad.strip().title()
        
        # [Tarea: Normalización de combustible] Limpia espacios y pasa a minúsculas
        self.combustible = combustible.strip().lower()
        
        # [Tarea: Validación de fecha] Ejecuta la validación estricta y guarda la fecha limpia
        self.fecha_referencia = self._validar_fecha(fecha_referencia)

    def _validar_fecha(self, fecha_str: str) -> str:
        """Valida formato estricto con Expresión Regular (DD-MM-YYYY) y existencia en el calendario."""
        
        # [Tarea: Control de patrón visual] Define la Regex estricta para formato argentino DD-MM-YYYY
        patron = r"^\d{2}-\d{2}-\d{4}$"
        if not re.match(patron, fecha_str):
            raise ValueError(f"Formato de fecha inválido '{fecha_str}'. Debe respetar el patrón DD-MM-YYYY (ej. 23-10-2026).")
        
        # [Tarea: Control de calendario real] Comprueba que la fecha exista físicamente en el calendario
        try:
            datetime.strptime(fecha_str, "%d-%m-%Y")
        except ValueError:
            raise ValueError(f"La fecha '{fecha_str}' no es válida en el calendario real.")
        
        return fecha_str


def seleccionar_vigentes(datos: list[dict], fecha_ref: str) -> list[dict]:
    """Elige el registro más reciente de cada estación y combustible que no supere la fecha de referencia (DD-MM-YYYY)."""
    
    # [Tarea: Conversión de referencia] Transforma la fecha límite de texto a objeto fecha real
    fecha_tope = datetime.strptime(fecha_ref, "%d-%m-%Y")
    recientes = {}

    for row in datos:
        # [Tarea: Conversión segura de registro] Pasa la fecha del registro a objeto fecha real
        f_reg = row.get("fecha")
        f_dt = datetime.strptime(f_reg, "%d-%m-%Y") if isinstance(f_reg, str) else f_reg
        
        # [Tarea: Filtro de fecha futura] Ignora registros posteriores a la fecha de consulta
        if f_dt > fecha_tope:
            continue

        # [Tarea: Identificación única] Crea una clave combinada por estación y combustible
        clave = (row.get("estacion"), row.get("combustible"))

        # [Tarea: Selección del más reciente] Guarda el registro o actualiza si encuentra uno más nuevo
        if clave not in recientes:
            recientes[clave] = row
        else:
            f_actual = datetime.strptime(recientes[clave]["fecha"], "%d-%m-%Y") if isinstance(recientes[clave]["fecha"], str) else recientes[clave]["fecha"]
            if f_dt > f_actual:
                recientes[clave] = row

    # [Tarea: Retorno de lista] Devuelve los valores finales limpios como una lista de diccionarios
    return list(recientes.values())


def buscar_estaciones(datos_vigentes: list[dict], localidad: str, combustible: str) -> list[dict]:
    """Filtra por localidad y combustible, y ordena los resultados de menor a mayor precio."""
    
    # [Caja de resultados] Prepara una lista vacía para guardar únicamente las estaciones que coincidan con la búsqueda
    resultados = []
    
    # [Recorrido de seguridad] Revisa uno por uno todos los registros vigentes que nos pasaron
    for row in datos_vigentes:
        # [Filtro de localidad flexible] Limpia espacios y unifica mayúsculas para comparar la localidad sin importar cómo se escribió
        loc_match = row.get("localidad", "").strip().title() == localidad.strip().title()
        
        # [Filtro de combustible flexible] Limpia espacios y pasa a minúsculas para comparar el tipo de nafta sin errores
        comb_match = row.get("combustible", "").strip().lower() == combustible.strip().lower()
        
        # [Coincidencia exacta] Si la localidad Y el combustible coinciden con lo que buscamos...
        if loc_match and comb_match:
            # ...agrega esta estación a nuestra lista de resultados válidos
            resultados.append(row)

    # [Ordenamiento inteligente] Ordena las estaciones encontradas de menor a mayor precio. 
    # Usa 'key' para enfocar el escáner solo en el precio, lo pasa a número con 'float' para que ordene bien matemáticamente, 
    # y si no tiene precio le pone un 0 por seguridad.
    resultados.sort(key=lambda x: float(x.get("precio", 0)))
    
    # [Entrega final] Devuelve la lista limpia y ordenada para mostrarla o exportarla
    return resultados


 # [Tarea: Escritura de archivo] Abre el archivo y exporta los datos usando las cabeceras originales
    # keys = resultados[0].keys() toma las cabeceras en la primera fila
    # newline="" evita que en Windows se generen líneas en blanco extra entre renglón y renglón al escribir el CSV.
    #writeheader() escribe la primera línea del archivo con los títulos de las columnas (ej: estacion, combustible, precio, fecha).
    #writerwriterows(resultados) agarra toda la lista de diccionarios y los pega uno por uno abajo de los títulos de forma automática.
def exportar_consulta(resultados: list[dict], ruta_salida: str):
    """Guarda los resultados filtrados en un archivo de salida CSV."""
    if not resultados:
        print("No hay datos para exportar en esta consulta.")
        return
    keys = resultados[0].keys()
    with open(ruta_salida, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(resultados)
    print(f"Reporte exportado con éxito en: {ruta_salida}")