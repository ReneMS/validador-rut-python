from logic import validar_rut, generar_rut_valido

def menu():
    print("\n--- HERRAMIENTAS DE RUT CHILE ---")
    print("1. Validar un RUT")
    print("2. Generar un RUT aleatorio válido")
    print("3. Salir")
    
    opcion = input("\nSelecciona una opción: ")
    
    if opcion == "1":
        rut = input("Ingresa el RUT (ej: 12.345.678-9): ")
        if validar_rut(rut):
            print(f"✅ El RUT {rut} es VÁLIDO.")
        else:
            print(f"❌ El RUT {rut} es INVÁLIDO.")
            
    elif opcion == "2":
        nuevo_rut = generar_rut_valido()
        print(f"✨ RUT Generado: {nuevo_rut}")
        
    elif opcion == "3":
        print("¡Adiós!")
        return False
    else:
        print("⚠️ Opción no válida.")
    
    return True

if __name__ == "__main__":
    corriendo = True
    while corriendo:
        corriendo = menu()