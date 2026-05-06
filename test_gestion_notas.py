"""
Tests unitarios para el Sistema de Gestión de Notas
Ejecutar con: python -m pytest tests/test_gestion_notas.py
"""

import unittest
import json
import os
import tempfile
from pathlib import Path
import sys

# Agregar el directorio padre al path para importar main.py
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import GestorNotas


class TestGestorNotas(unittest.TestCase):
    """Suite de pruebas para la clase GestorNotas"""
    
    def setUp(self):
        """Configuración antes de cada test"""
        # Usar archivo temporal para tests
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        self.gestor = GestorNotas(self.temp_file.name)
    
    def tearDown(self):
        """Limpieza después de cada test"""
        # Eliminar archivo temporal
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_agregar_estudiante(self):
        """Test: Agregar un estudiante"""
        resultado = self.gestor.agregar_estudiante("123", "Juan", "juan@test.com")
        self.assertTrue(resultado)
        self.assertIn("123", self.gestor.estudiantes)
        self.assertEqual(self.gestor.estudiantes["123"]["nombre"], "Juan")
    
    def test_agregar_estudiante_duplicado(self):
        """Test: No permitir agregar estudiante duplicado"""
        self.gestor.agregar_estudiante("123", "Juan", "juan@test.com")
        resultado = self.gestor.agregar_estudiante("123", "Otro", "otro@test.com")
        self.assertFalse(resultado)
    
    def test_eliminar_estudiante(self):
        """Test: Eliminar un estudiante"""
        self.gestor.agregar_estudiante("123", "Juan", "juan@test.com")
        resultado = self.gestor.eliminar_estudiante("123")
        self.assertTrue(resultado)
        self.assertNotIn("123", self.gestor.estudiantes)
    
    def test_eliminar_estudiante_inexistente(self):
        """Test: No permitir eliminar estudiante inexistente"""
        resultado = self.gestor.eliminar_estudiante("999")
        self.assertFalse(resultado)
    
    def test_registrar_calificacion(self):
        """Test: Registrar una calificación"""
        self.gestor.agregar_estudiante("123", "Juan", "juan@test.com")
        resultado = self.gestor.registrar_calificacion("123", "Python", 85)
        self.assertTrue(resultado)
        self.assertIn("Python", self.gestor.estudiantes["123"]["calificaciones"])
    
    def test_registrar_calificacion_invalida(self):
        """Test: Rechazar calificación fuera de rango"""
        self.gestor.agregar_estudiante("123", "Juan", "juan@test.com")
        resultado = self.gestor.registrar_calificacion("123", "Python", 150)
        self.assertFalse(resultado)
    
    def test_registrar_calificacion_negativa(self):
        """Test: Rechazar calificación negativa"""
        self.gestor.agregar_estudiante("123", "Juan", "juan@test.com")
        resultado = self.gestor.registrar_calificacion("123", "Python", -10)
        self.assertFalse(resultado)
    
    def test_obtener_promedio_simple(self):
        """Test: Calcular promedio de una materia"""
        self.gestor.agregar_estudiante("123", "Juan", "juan@test.com")
        self.gestor.registrar_calificacion("123", "Python", 80)
        self.gestor.registrar_calificacion("123", "Python", 90)
        promedio = self.gestor.obtener_promedio("123", "Python")
        self.assertEqual(promedio, 85.0)
    
    def test_obtener_promedio_general(self):
        """Test: Calcular promedio general"""
        self.gestor.agregar_estudiante("123", "Juan", "juan@test.com")
        self.gestor.registrar_calificacion("123", "Python", 80)
        self.gestor.registrar_calificacion("123", "JavaScript", 90)
        promedio = self.gestor.obtener_promedio("123")
        self.assertEqual(promedio, 85.0)
    
    def test_obtener_promedio_inexistente(self):
        """Test: Obtener promedio de estudiante inexistente"""
        promedio = self.gestor.obtener_promedio("999", "Python")
        self.assertIsNone(promedio)
    
    def test_obtener_escala_excelente(self):
        """Test: Escala Excelente (90-100)"""
        escala = self.gestor.obtener_escala(95)
        self.assertEqual(escala, "Excelente")
    
    def test_obtener_escala_bueno(self):
        """Test: Escala Bueno (80-89)"""
        escala = self.gestor.obtener_escala(85)
        self.assertEqual(escala, "Bueno")
    
    def test_obtener_escala_satisfactorio(self):
        """Test: Escala Satisfactorio (70-79)"""
        escala = self.gestor.obtener_escala(75)
        self.assertEqual(escala, "Satisfactorio")
    
    def test_obtener_escala_aceptable(self):
        """Test: Escala Aceptable (60-69)"""
        escala = self.gestor.obtener_escala(65)
        self.assertEqual(escala, "Aceptable")
    
    def test_obtener_escala_deficiente(self):
        """Test: Escala Deficiente (<60)"""
        escala = self.gestor.obtener_escala(55)
        self.assertEqual(escala, "Deficiente")
    
    def test_persistencia_datos(self):
        """Test: Los datos se guardan y cargan correctamente"""
        # Agregar estudiante
        self.gestor.agregar_estudiante("123", "Juan", "juan@test.com")
        self.gestor.registrar_calificacion("123", "Python", 85)
        
        # Crear nuevo gestor con mismo archivo
        gestor2 = GestorNotas(self.temp_file.name)
        
        # Verificar que los datos se cargaron
        self.assertIn("123", gestor2.estudiantes)
        self.assertEqual(gestor2.estudiantes["123"]["nombre"], "Juan")
        promedio = gestor2.obtener_promedio("123", "Python")
        self.assertEqual(promedio, 85.0)


class TestIntegracion(unittest.TestCase):
    """Tests de integración del flujo completo"""
    
    def setUp(self):
        """Configuración antes de cada test"""
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        self.gestor = GestorNotas(self.temp_file.name)
    
    def tearDown(self):
        """Limpieza después de cada test"""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_flujo_completo(self):
        """Test: Flujo completo de registro y reportes"""
        # Agregar 3 estudiantes
        self.gestor.agregar_estudiante("001", "Carlos", "carlos@test.com")
        self.gestor.agregar_estudiante("002", "María", "maria@test.com")
        self.gestor.agregar_estudiante("003", "Pedro", "pedro@test.com")
        
        # Registrar calificaciones para Carlos
        self.gestor.registrar_calificacion("001", "Python", 90)
        self.gestor.registrar_calificacion("001", "Python", 85)
        self.gestor.registrar_calificacion("001", "JavaScript", 88)
        
        # Registrar calificaciones para María
        self.gestor.registrar_calificacion("002", "Python", 95)
        self.gestor.registrar_calificacion("002", "JavaScript", 92)
        
        # Registrar calificaciones para Pedro
        self.gestor.registrar_calificacion("003", "Python", 70)
        
        # Verificar promedios
        self.assertAlmostEqual(self.gestor.obtener_promedio("001"), 87.67, places=1)
        self.assertAlmostEqual(self.gestor.obtener_promedio("002"), 93.5, places=1)
        self.assertEqual(self.gestor.obtener_promedio("003"), 70.0)
        
        # Verificar escalas
        self.assertEqual(self.gestor.obtener_escala(87.67), "Excelente")
        self.assertEqual(self.gestor.obtener_escala(93.5), "Excelente")
        self.assertEqual(self.gestor.obtener_escala(70.0), "Satisfactorio")


if __name__ == '__main__':
    unittest.main()
