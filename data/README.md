# Carpeta de Datos (data/)

Este directorio contiene los conjuntos de datos utilizados para la ejecución y pruebas de la aplicación, provistos en formatos equivalentes para comprobar la lectura dual (Paso 3 y Paso 4 de la consigna).

## Archivos disponibles
- `combustibles.csv`: Registros de precios en formato tabular CSV.
- `combustibles.json`: Registros equivalentes estructurados en formato JSON.

## Esquema y Variables
Cada archivo contiene 50 observaciones con las siguientes variables:
- `estacion`: Nombre o identificador comercial de la estación de servicio.
- `localidad`: Localidad o zona geográfica.
- `combustible`: Tipo de producto (ej. nafta super).
- `fecha`: Fecha de vigencia del precio (formato DD-MM-AAA).
- `precio`: Precio por unidad en formato numérico decimal.

Para más detalles sobre la procedencia, licencia y alcance de los datos, consulte el README principal en la raíz del repositorio.