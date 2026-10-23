# tp2-combustibles
Trabajo práctico 2 — Consulta de precios de combustibles en Python

# Buscador de Precios Vigentes de Combustibles

## 1. Definición del Problema y Alcance

### Problema y necesidad que se aborda
En Argentina, los precios de los combustibles varían constantemente entre distintas estaciones de servicio y localidades. Cuando un usuario o empresa consulta registros de precios, suele encontrarse con archivos históricos que contienen múltiples actualizaciones de fechas pasadas. Comparar estos registros sin filtrar de forma explícita la fecha de vigencia provoca que se tomen decisiones con precios desactualizados o información inconsistente.

### Usuario objetivo y uso
El programa está pensado para **conductores particulares, administradores de flotas de transporte y analistas de mercado** que necesitan conocer con exactitud el precio vigente más reciente de cada estación de servicio en una localidad determinada para optimizar sus costos de carga de combustible.

### Solución propuesta y operaciones
Se propone una aplicación de consola en Python que permite procesar y consultar registros de precios de estaciones de servicio. El programa permite realizar las siguientes operaciones:
1. Cargar y validar fuentes de datos tabulares en formatos CSV y JSON.
2. Filtrar los registros por **localidad**, **tipo de combustible** y **fecha de referencia**.
3. Seleccionar automáticamente el precio vigente más reciente para cada estación que no supere la fecha de consulta ingresada.
4. Ordenar los precios vigentes de menor a mayor y exportar la consulta.

### Resultado producido e interpretación
El programa genera una tabla ordenada (en pantalla y/o archivo de salida) con las estaciones de servicio de la localidad, la dirección, el tipo de combustible, la fecha de la última actualización aplicada y el precio por litro vigente. Esto permite al usuario identificar rápidamente cuál es la opción más económica y actualizada a la fecha consultada.

### Alcance de la primera versión
* **Incluido:**
  * Lectura de datos en CSV y JSON.
  * Normalización y validación de fechas y precios.
  * Filtro por localidad, tipo de combustible y fecha de referencia.
  * Selección del registro más reciente por estación que no supere la fecha elegida.
  * Ordenamiento de opciones por precio ascendente.
  * Registro y reporte de filas rechazadas o inconsistentes.
* **Fuera del alcance (versiones futuras):**
  * Interfaz gráfica de usuario (GUI) o aplicación web.
  * Conversión automática de monedas o cálculo de inflación.
  * Geolocalización en mapa o cálculo de rutas óptimas hacia la estación.
  * Integración en tiempo real mediante APIs web externas.