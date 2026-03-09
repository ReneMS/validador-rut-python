import random

def validar_rut(rut_completo):
    # Limpiar el RUT
    rut_limpio = rut_completo.replace(".", "").replace("-", "").upper()
    
    # Validación básica
    if len(rut_limpio) < 8:
        return False
        
    cuerpo = rut_limpio[:-1]
    dv_ingresado = rut_limpio[-1]
    
    if not cuerpo.isdigit():
        return False

    # Calcular DV (Módulo 11)
    reverso = map(int, reversed(cuerpo))
    factores = [2, 3, 4, 5, 6, 7]
    suma = 0
    
    for i, d in enumerate(reverso):
        suma += d * factores[i % 6]
        
    dv_esperado = 11 - (suma % 11)
    
    if dv_esperado == 11:
        dv_real = "0"
    elif dv_esperado == 10:
        dv_real = "K"
    else:
        dv_real = str(dv_esperado)

    return dv_real == dv_ingresado

def generar_rut_valido():
    # Generar un cuerpo aleatorio
    cuerpo = str(random.randint(5000000, 25000000))
    
    # Calcular su DV
    reverso = map(int, reversed(cuerpo))
    factores = [2, 3, 4, 5, 6, 7]
    suma = 0
    for i, d in enumerate(reverso):
        suma += d * factores[i % 6]
    
    res = 11 - (suma % 11)
    
    if res == 11:
        dv = "0"
    elif res == 10:
        dv = "K"
    else:
        dv = str(res)
    
    return f"{cuerpo}-{dv}"