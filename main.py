# TODO: Importar módulos cuando estén listos
from inventario import agregar_producto, eliminar_producto, modificar_producto, reabastecer_stock, mostrar_productos
from reportes import top_3_vendidos, productos_stock_bajo, ventas_por_franja_horaria, resumen_semanal, ticket_promedio
# from busquedas_ordenamientos import *
from io_archivos import cargar_desde_csv, guardar_en_csv, exportar_alertas

def mostrar_menu_principal():
    print("\n" + "="*50)
    print("              KIOSKO UNIVERSITARIO UCB")
    print("="*50)
    print("1. Gestión de Inventario")
    print("2. Registrar Venta")
    print("3. Reportes y Estadísticas")
    print("4. Búsquedas y Ordenamientos") 
    print("5. Guardar y Salir")

def gestion_inventario(productos):
    print("\n GESTIÓN DE INVENTARIO")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Modificar producto")
    print("4. Reabastecer stock")
    print("5. Mostrar todos los productos")
    print("6. Volver al menú principal")
    opcion = input("\nSeleccione una opción(1-6): ")
    
    if opcion == "1":
        productos = agregar_producto(productos)
    elif opcion == "2":
        productos = eliminar_producto(productos)
    elif opcion == "3":
        productos = modificar_producto(productos)
    elif opcion == "4":
        productos = reabastecer_stock(productos)
    elif opcion == "5":
        mostrar_productos(productos)
    elif opcion == "6":
        return productos
    else:
        print("Opción inválida")
    
    return productos  # para devolver los productos actualizados

def registrar_venta(productos):
    print("\nREGISTRAR VENTA")
    # Mostrar productos disponibles
    print("\nPRODUCTOS DISPONIBLES:")
    print("-" * 60)
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto['nombre']} - Bs{producto['precio']} - Stock: {producto['stock']}")
    print("-" * 60)
    
    try:
        # Seleccionar producto
        opcion = int(input("\nSeleccione el número del producto: ")) - 1
        
        if opcion < 0 or opcion >= len(productos):
            print("Opción inválida")
            return productos
        
        producto = productos[opcion]
        
        # Pedir cantidad
        cantidad = int(input(f"Cantidad de '{producto['nombre']}' a vender: "))
        
        # Validar stock
        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0")
            return productos
        
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
        
    except ValueError:
        print("Error: Debe ingresar números válidos")
    
    return productos
def mostrar_reportes(productos):
    print("\n REPORTES Y ESTADÍSTICAS")
    print("1. Top 3 productos más vendidos del día")
    print("2. Productos con stock bajo")
    print("3. Ventas por franja horaria")
    print("4. Resumen semanal")
    print("5. Ticket promedio del día")  # ← NUEVA OPCIÓN
    print("6. Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        top_3_vendidos(productos)
    elif opcion == "2":
        productos_stock_bajo(productos)
    elif opcion == "3":
        ventas_por_franja_horaria()
    elif opcion == "4":
        resumen_semanal()
    elif opcion == "5":  # ← NUEVA OPCIÓN
        ticket_promedio(productos)
    elif opcion == "6":
        return
    else:
        print("Opción inválida")

def busquedas_ordenamientos(productos):
    print("\nBÚSQUEDAS Y ORDENAMIENTOS")
    print("1. Buscar producto por nombre")
    print("2. Buscar producto por código")
    print("3. Ordenar productos por precio")
    print("4. Ordenar productos por nombre")
    print("5. Ordenar productos por stock")
    print("6. Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        # TODO: Llamar a función buscar_por_nombre()
        print("Búsqueda por nombre...")
    elif opcion == "2":
        # TODO: Llamar a función buscar_por_codigo()
        print("Búsqueda por código...")
    elif opcion == "3":
        # TODO: Llamar a función ordenar_por_precio()
        print("Ordenar por precio...")
    elif opcion == "4":
        # TODO: Llamar a función ordenar_por_nombre()
        print("Ordenar por nombre...")
    elif opcion == "5":
        # TODO: Llamar a función ordenar_por_stock()
        print("Ordenar por stock...")
    elif opcion == "6":
        return
    else:
        print("Opción inválida")

def main():
    productos = cargar_desde_csv()
    
    while True:
        mostrar_menu_principal()
        opcion = input("\nSeleccione una opción (1-5): ")
        
        if opcion == "1":
            gestion_inventario(productos)
        elif opcion == "2":
            registrar_venta(productos)
        elif opcion == "3":
            mostrar_reportes(productos)
        elif opcion == "4":
            busquedas_ordenamientos(productos)
        elif opcion == "5":
            guardar_en_csv(productos)
            exportar_alertas(productos)
            print("\n Guardando datos... SALIDA EXITOSA")
            break
        else:
            print("\nOpción inválida.")
        
        input("\nPresione Enter para continuar")

if __name__ == "__main__":
    main()