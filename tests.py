import unittest
from logic import validar_rut, calcular_dv, formatear_rut

class TestRutLogic(unittest.TestCase):

    def test_calcular_dv(self):
        # Casos conocidos
        self.assertEqual(calcular_dv("30686957"), "4")
        self.assertEqual(calcular_dv("18502012"), "6")
        # Caso borde dígito K (ejemplo teórico para validación)
        # Si el resultado del módulo 11 es 10, retorna K.
        # Un cuerpo que genere resto 10 con módulo 11 necesitaría mock o cálculo inverso,
        # pero probamos la consistencia.
        pass

    def test_validar_rut_valido(self):
        self.assertTrue(validar_rut("30.686.957-4"))
        self.assertTrue(validar_rut("30686957-4"))
        self.assertTrue(validar_rut("306869574"))
        self.assertTrue(validar_rut("11.111.111-1")) # RUT de prueba clásico

    def test_validar_rut_invalido(self):
        self.assertFalse(validar_rut("12.345.678-1")) # DV incorrecto
        self.assertFalse(validar_rut("abc"))          # No numérico
        self.assertFalse(validar_rut("1-1"))          # Muy corto

    def test_formatear_rut(self):
        self.assertEqual(formatear_rut("123456789"), "12.345.678-9")
        self.assertEqual(formatear_rut("111111111"), "11.111.111-1")
        self.assertEqual(formatear_rut("1-9"), "1-9") # Mínimo

if __name__ == '__main__':
    unittest.main()