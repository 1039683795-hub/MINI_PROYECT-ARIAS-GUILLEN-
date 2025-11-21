"""
Demo interactivo del Cajero Electrónico
"""
from mini_proyecto.operaciones import Cajero
from mini_proyecto.estrategias import validar_opcion

def demo_cajero():
    print("\n" + "="*50)
    print("     DEMO: CAJERO ELECTRÓNICO FUNCIONAL")
    print("="*50)
    
    cajero = Cajero(100000)
    
    # 1. Consultar saldo inicial
    print("\n✓ Operación 1: Consultar saldo inicial")
    saldo = cajero.consultar_saldo()
    print(f"   Saldo actual: ${saldo:,}")
    
    # 2. Depositar dinero
    print("\n✓ Operación 2: Depositar $50,000")
    cantidad = 50000
    nuevo_saldo = cajero.depositar(cantidad)
    print(f"   Depósito exitoso. Nuevo saldo: ${nuevo_saldo:,}")
    
    # 3. Retirar dinero
    print("\n✓ Operación 3: Retirar $30,000")
    cantidad = 30000
    nuevo_saldo = cajero.retirar(cantidad)
    print(f"   Retiro exitoso. Nuevo saldo: ${nuevo_saldo:,}")
    
    # 4. Consultar saldo final
    print("\n✓ Operación 4: Consultar saldo final")
    saldo = cajero.consultar_saldo()
    print(f"   Saldo actual: ${saldo:,}")
    
    # 5. Intentar retirar más de lo disponible (error)
    print("\n✓ Operación 5: Intentar retirar $200,000 (sin fondos)")
    try:
        cajero.retirar(200000)
    except ValueError as e:
        print(f"   ❌ Error: {e}")
    
    # 6. Intentar depositar cantidad negativa (error)
    print("\n✓ Operación 6: Intentar depositar cantidad negativa")
    try:
        cajero.depositar(-500)
    except ValueError as e:
        print(f"   ❌ Error: {e}")
    
    print("\n" + "="*50)
    print("     DEMO COMPLETADA EXITOSAMENTE")
    print("="*50 + "\n")

if __name__ == "__main__":
    demo_cajero()
