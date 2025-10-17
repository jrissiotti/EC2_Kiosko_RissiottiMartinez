# TODO: Importar módulos cuando estén listos
# from inventario import *
# from reportes import *
# from busquedas_ordenamientos import *
# from io_archivos import *

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
    print("5. Volver al menú principal")
    opcion = input("\nSeleccione una opción(1-5): ")
    
    if opcion == "1":
        # TODO: Llamar a función agregar_producto()
        print("Agregar producto...")
    elif opcion == "2":
        # TODO: Llamar a función eliminar_producto()
        print("Eliminar producto...")
    elif opcion == "3":
        # TODO: Llamar a función modificar_producto()
        print("Modificar producto...")
    elif opcion == "4":
        # TODO: Llamar a función reabastecer_stock()
        print("Reabastecer stock...")
    elif opcion == "5":
        return
    else:
        print("Opción inválida")

def registrar_venta(productos):
    print("\nREGISTRAR VENTA")
    # TODO: Implementar lógica de venta
    # TODO: Mostrar lista de productos
    # TODO: Seleccionar producto y cantidad
    # TODO: Validar stock disponible
    # TODO: Actualizar stock y vendidos_hoy
    # TODO: Calcular total y mostrar ticket

def mostrar_reportes(productos):
    print("\n REPORTES Y ESTADÍSTICAS")
    print("1. Productos vendidos el día de hoy")
    print("2. Productos con stock bajo")
    print("3. Ventas por franja horaria") # Reporte de matriz 2D: ventas por franjas (mañana/tarde/noche)
    print("4. Resumen semanal")
    print("5. Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        # TODO: Llamar a función vendidos_hoy()
        print("Productos vendidos hoy...")
    elif opcion == "2":
        # TODO: Llamar a función productos_stock_bajo()
        print("Productos stock bajo...")
    elif opcion == "3":
        # TODO: Llamar a función ventas_por_franja_horaria()
        print("Ventas por franja horaria...")
    elif opcion == "4":
        # TODO: Llamar a función resumen_semanal()
        print("Resumen semanal...")
    elif opcion == "5":
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
    productos = []  # TODO: Cargar productos desde CSV
    
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
            # TODO: Guardar productos en CSV y binario
            print("\n Guardando datos... SALIDA EXITOSA")
            break
        else:
            print("\nOpción inválida.")
        
        input("\nPresione Enter para continuar")

if __name__ == "__main__":
    main()