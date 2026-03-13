# Validador y Generador de RUT Chileno 🇨🇱

Este es un proyecto en Python diseñado para manejar la lógica del Rol Único Tributario (RUT) en Chile. Incluye funciones para validar, formatear y generar RUTs, implementando correctamente el algoritmo de Módulo 11.

Es ideal para ser utilizado como base en sistemas que requieran validación de usuarios, limpieza de datos o generación de datos de prueba para desarrollo.

## ✨ Características

- **Validación Robusta:** Comprueba si un RUT es válido verificando el dígito verificador. Soporta formatos con puntos, guiones o solo números.
- **Formateo:** Convierte RUTs "crudos" (ej: `123456789`) al formato estándar visual (ej: `12.345.678-9`).
- **Generación:** Crea RUTs aleatorios matemáticamente válidos para propósitos de prueba.
- **Tests Unitarios:** Incluye una suite de pruebas para garantizar la fiabilidad del código.
- **Sin Dependencias:** Funciona con la librería estándar de Python.

## 📂 Estructura del Proyecto

- `main.py`: Interfaz de línea de comandos (CLI) interactiva para probar las funciones.
- `logic.py`: Núcleo del proyecto. Contiene las funciones puras (`validar_rut`, `calcular_dv`, etc.).
- `tests.py`: Pruebas unitarias para asegurar la calidad del código.

## 🚀 Cómo ejecutar

### Interfaz Interactiva

Para usar el menú interactivo:

1. Clona este repositorio.
2. Ejecuta el archivo principal:
   ```bash
   python main.py
   ```

### Ejecutar Pruebas

Para verificar que todo funciona correctamente en tu entorno:

```bash
python tests.py
```

## 💻 Uso como Librería

Puedes importar `logic.py` en tus propios scripts:

```python
from logic import validar_rut, formatear_rut

rut = "12.345.678-9"

if validar_rut(rut):
    print(f"El RUT {formatear_rut(rut)} es correcto")
```

---

Hecho con 🐍 Python.
