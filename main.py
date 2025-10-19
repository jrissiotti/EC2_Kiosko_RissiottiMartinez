from inventario import agregar_producto, eliminar_producto, modificar_producto, reabastecer_stock, mostrar_productos, pedir_entero
from reportes import top_3_vendidos, productos_stock_bajo, ventas_por_franja_horaria, resumen_semanal, ticket_promedio
from busquedas_ordenamientos import buscar_por_nombre, buscar_por_codigo, ordenar_por_precio, ordenar_por_nombre, ordenar_por_stock
from io_archivos import cargar_desde_binario_o_csv, guardar_en_csv, exportar_alertas, guardar_backup_binario

def pedir_opcion(mensaje, min_val, max_val):
    """Pide un número entero dentro de un rango determinado."""
    while True:
        try:
            valor = int(input(mensaje))
            if min_val <= valor <= max_val:
                return valor
            else:
                print(f"Debe ingresar un número entre {min_val} y {max_val}")
        except ValueError:
            print("Debe ingresar un número válido")

def mostrar_menu_principal():
    """Muestra el menú principal del kiosko."""
    print("\n" + "="*50)
    print("              KIOSKO UNIVERSITARIO UCB")
    print("="*50)
    print("1. Gestión de Inventario")
    print("2. Registrar Venta")
    print("3. Reportes y Estadísticas")
    print("4. Búsquedas y Ordenamientos") 
    print("5. Guardar y Salir")

def gestion_inventario(productos):
    """Submenú de gestión de inventario: agregar, eliminar, modificar, reabastecer o mostrar productos."""
    print("\n GESTIÓN DE INVENTARIO")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Modificar producto")
    print("4. Reabastecer stock")
    print("5. Mostrar todos los productos")
    print("6. Volver al menú principal")
    
    opcion = pedir_opcion("\nSeleccione una opción(1-6): ", 1, 6)
    
    if opcion == 1:
        productos = agregar_producto(productos)
    elif opcion == 2:
        productos = eliminar_producto(productos)
    elif opcion == 3:
        productos = modificar_producto(productos)
    elif opcion == 4:
        productos = reabastecer_stock(productos)
    elif opcion == 5:
        mostrar_productos(productos)
    elif opcion == 6:
        return productos
    
    return productos  # devuelve productos actualizados

def registrar_venta(productos):
    """Permite registrar una venta de productos, actualizando stock y vendidos_hoy."""
    print("\nREGISTRAR VENTA")
    
    if not productos:
        print("No hay productos disponibles.")
        return productos
    
    print("\nPRODUCTOS DISPONIBLES:")
    print("-" * 60)
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto['nombre']} - Bs{producto['precio']} - Stock: {producto['stock']}")
    print("-" * 60)
    
    opcion = pedir_opcion("\nSeleccione el número del producto: ", 1, len(productos)) - 1
    producto = productos[opcion]
    
    cantidad = pedir_entero(f"Cantidad de '{producto['nombre']}' a vender: ", min_val=1)
    
    if cantidad > producto['stock']:
        print(f"Stock insuficiente. Solo hay {producto['stock']} unidades")
        return productos
    
    # Procesar venta
    producto['stock'] -= cantidad
    producto['vendidos_hoy'] += cantidad
    total = cantidad * producto['precio']
    
    # Mostrar ticket
    print("\nTICKET DE VENTA:")
    print("=" * 30)
    print(f"Producto: {producto['nombre']}")
    print(f"Cantidad: {cantidad}")
    print(f"Precio unitario: Bs{producto['precio']}")
    print(f"TOTAL: Bs{total:.2f}")
    print("=" * 30)
    print("Venta registrada exitosamente")
    
    return productos

def mostrar_reportes(productos):
    """Submenú para mostrar diferentes reportes y estadísticas del kiosko."""
    print("\n REPORTES Y ESTADÍSTICAS")
    print("1. Top 3 productos más vendidos del día")
    print("2. Productos con stock bajo")
    print("3. Ventas por franja horaria")
    print("4. Resumen semanal")
    print("5. Ticket promedio del día")
    print("6. Volver al menú principal")
    
    opcion = pedir_opcion("Seleccione una opción: ", 1, 6)
    
    if opcion == 1:
        top_3_vendidos(productos)
    elif opcion == 2:
        productos_stock_bajo(productos)
    elif opcion == 3:
        ventas_por_franja_horaria()
    elif opcion == 4:
        resumen_semanal()
    elif opcion == 5:
        ticket_promedio(productos)
    elif opcion == 6:
        return

def busquedas_ordenamientos(productos):
    """Submenú para realizar búsquedas y ordenar productos."""
    print("\nBÚSQUEDAS Y ORDENAMIENTOS")
    print("1. Buscar producto por nombre")
    print("2. Buscar producto por código")
    print("3. Ordenar productos por precio")
    print("4. Ordenar productos por nombre")
    print("5. Ordenar productos por stock")
    print("6. Volver al menú principal")
    
    opcion = pedir_opcion("Seleccione una opción: ", 1, 6)
    
    if opcion == 1:
        nombre = input("Ingrese el nombre a buscar: ")
        buscar_por_nombre(productos, nombre)
    elif opcion == 2:
        codigo = input("Ingrese el código a buscar: ")
        buscar_por_codigo(productos, codigo)
    elif opcion == 3:
        ordenar_por_precio(productos)
    elif opcion == 4:
        ordenar_por_nombre(productos)
    elif opcion == 5:
        ordenar_por_stock(productos)
    elif opcion == 6:
        return

def main():
    """
    Función principal del programa.
    Carga productos desde CSV o backup binario y permite:
    - Gestión de inventario
    - Registro de ventas
    - Reportes y estadísticas
    - Búsquedas y ordenamientos
    Al salir, guarda los datos en CSV y backup binario, y exporta alertas.
    """
    productos = cargar_desde_binario_o_csv()
    
    while True:
        mostrar_menu_principal()
        opcion = pedir_opcion("\nSeleccione una opción (1-5): ", 1, 5)
        
        if opcion == 1:
            productos = gestion_inventario(productos)
        elif opcion == 2:
            productos = registrar_venta(productos)
        elif opcion == 3:
            mostrar_reportes(productos)
        elif opcion == 4:
            busquedas_ordenamientos(productos)
        elif opcion == 5:
            guardar_en_csv(productos)
            guardar_backup_binario(productos)
            exportar_alertas(productos)
            print("\nDatos guardados en CSV, backup binario y alertas exportadas. Saliendo...")
            break
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
