import random

def calcular_dv(cuerpo: str) -> str:
    """Calcula el dígito verificador para un cuerpo de RUT dado."""
    reverso = map(int, reversed(cuerpo))
    factores = [2, 3, 4, 5, 6, 7]
    suma = 0
    
    for i, d in enumerate(reverso):
        suma += d * factores[i % 6]
        
    res = 11 - (suma % 11)
    
    if res == 11:
        return "0"
    elif res == 10:
        return "K"
    return str(res)

def validar_rut(rut_completo: str) -> bool:
    # Limpiar el RUT
    rut_limpio = rut_completo.replace(".", "").replace("-", "").upper()
    
    # Validación básica
    if len(rut_limpio) < 2:
        return False
        
    cuerpo = rut_limpio[:-1]
    dv_ingresado = rut_limpio[-1]
    
    if not cuerpo.isdigit():
        return False

    return calcular_dv(cuerpo) == dv_ingresado

def generar_rut_valido() -> str:
    # Generar un rut aleatorio
    cuerpo = str(random.randint(5000000, 25000000))
    dv = calcular_dv(cuerpo)
    return f"{cuerpo}-{dv}"

def formatear_rut(rut_raw: str) -> str:
    """Formatea un RUT string (ej: 123456789 -> 12.345.678-9)."""
    rut_limpio = rut_raw.replace(".", "").replace("-", "").upper()
    
    if len(rut_limpio) < 2:
        return rut_raw
        
    cuerpo = rut_limpio[:-1]
    dv = rut_limpio[-1]
    
    if not cuerpo.isdigit():
        return rut_raw
        
    # Formatear con puntos de miles
    cuerpo_fmt = "{:,}".format(int(cuerpo)).replace(",", ".")
    return f"{cuerpo_fmt}-{dv}"