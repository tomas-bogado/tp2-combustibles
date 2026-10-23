# tp2-combustibles
Trabajo práctico 2 — Consulta de precios de combustibles en Python

# Buscador de Precios Vigentes de Combustibles

## 1. Definición del Problema y Alcance

### Problema y necesidad que se aborda
En Argentina, los precios de los combustibles varían constantemente entre distintas estaciones de servicio y localidades. Cuando un usuario o empresa consulta registros de precios, suele encontrarse con archivos históricos que contienen múltiples actualizaciones de fechas pasadas. Comparar estos registros sin filtrar de forma explícita la fecha de vigencia provoca que se tomen decisiones con precios desactualizados o información inconsistente.

### Usuario objetivo y uso
El programa está pensado para:
* Conductores particulares y administradores de flotas: Para buscar y comparar opciones con el fin de optimizar sus costos de carga de combustible.
* Dueños de estaciones de servicio o analistas del sector: Para consultar la competencia local, verificar qué precios se encuentran vigentes en una fecha dada y estudiar el posicionamiento del mercado en su localidad.

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



## 2. Documentación de los Datos y Procedencia

### Fuente y obtención
* **Procedencia:** Datos generados mediante simulación controlada y estructurada para fines académicos del trabajo práctico, representando registros de precios de estaciones de servicio en distintas localidades.
* **Responsable:** Tomas Bogado Viscarra.
* **Licencia / Condiciones de uso:** Uso libre y abierto para fines educativos en la cátedra de Programación Orientada a Datos (UCA, 2026).
* **Fecha de consulta / generación:** Octubre de 2026.

### Unidad de análisis y variables utilizadas
* **Unidad de análisis:** Cada fila representa una **actualización de precio de un tipo de combustible específico en una estación de servicio determinada** en una fecha dada.
* **Variables utilizadas (5 variables, superando el mínimo de 3 exigido):**
  1. `estacion` (texto): Nombre o identificador comercial de la estación de servicio.
  2. `localidad` (texto): Ciudad o zona geográfica donde se ubica la estación.
  3. `combustible` (texto): Tipo de producto (Nafta Super, Nafta Premium, Gasoil).
  4. `fecha` (texto AAAA-MM-DD): Fecha en la que entró en vigencia el precio registrado.
  5. `precio` (numérico decimal): Precio por unidad en pesos.

### Muestra y alcance del conjunto de datos
El conjunto cuenta con **50 observaciones** exactas distribuidas en formatos equivalentes `CSV` y `JSON` (`data/combustibles.csv` y `data/combustibles.json`), permitiendo probar lecturas múltiples, fechas desactualizadas y registros históricos por estación.

### Limitaciones, sesgos y restricciones
* Los datos son sintéticos y acotados a un conjunto reducido de localidades de prueba, por lo que no reflejan la totalidad del mercado nacional.
* No incluye datos personales sensibles, credenciales ni claves privadas[cite: 2].