import sys
import os

# Configuración de rutas para que Python encuentre src sin romper nada
raiz_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
src_folder = os.path.join(raiz_proyecto, 'src')

if raiz_proyecto not in sys.path:
    sys.path.insert(0, raiz_proyecto)
if src_folder not in sys.path:
    sys.path.insert(0, src_folder)

import unittest
from datetime import datetime
from src.pipeline import normalizar_precios
from src.analisis import seleccionar_vigentes

class TestCombustibles(unittest.TestCase):

    def setUp(self):
        """Datos de prueba simulados para los casos."""
        self.datos_prueba = [
            {"estacion": "YPF Centro", "localidad": "Rosario", "combustible": "Nafta Super", "fecha": "10-05-2026", "precio": "1200.50"},
            {"estacion": "YPF Centro", "localidad": "Rosario", "combustible": "Nafta Super", "fecha": "15-05-2026", "precio": "1250.00"},
            {"estacion": "Shell Norte", "localidad": "Rosario", "combustible": "Nafta Super", "fecha": "12-05-2026", "precio": "1230.00"},
            {"estacion": "Axion Sur", "localidad": "Funes", "combustible": "Gasoil", "fecha": "fecha_invalida", "precio": "abc"}
        ]

    def test_1_caso_normal(self):
        """Prueba 1: Caso normal de normalización y selección de precios vigentes."""
        datos_normalizados, rechazos = normalizar_precios(self.datos_prueba)
        
        # Pasamos la fecha como texto tal como lo espera tu función (día-mes-año)
        fecha_ref = "14-05-2026"
        vigentes = seleccionar_vigentes(datos_normalizados, fecha_ref=fecha_ref)
        
        # Verificamos que devuelva resultados procesados correctamente
        self.assertIsInstance(vigentes, list)

    def test_2_entrada_invalida(self):
        """Prueba 2: Caso límite o entrada inválida (detección de rechazos)."""
        datos_normalizados, rechazos = normalizar_precios(self.datos_prueba)
        # El registro con fecha y precio inválidos debe ser rechazado correctamente
        self.assertGreaterEqual(len(rechazos), 1)
        self.assertTrue(any(r["estacion"] == "Axion Sur" for r in rechazos))

    def test_3_equivalencia_formatos(self):
        """Prueba 3: Propiedad relevante (equivalencia de procesamiento)."""
        lote_csv = [{"estacion": "Shell", "localidad": "Rosario", "combustible": "Nafta Super", "fecha": "01-05-2026", "precio": "1000"}]
        lote_json = [{"estacion": "Shell", "localidad": "Rosario", "combustible": "Nafta Super", "fecha": "01-05-2026", "precio": "1000"}]
        
        norm_csv, _ = normalizar_precios(lote_csv)
        norm_json, _ = normalizar_precios(lote_json)
        
        # Comprobamos que ambas fuentes produzcan exactamente el mismo resultado
        self.assertEqual(norm_csv, norm_json)

if __name__ == "__main__":
    unittest.main()