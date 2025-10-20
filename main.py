from inventario import agregar_producto, eliminar_producto, modificar_producto, reabastecer_stock, mostrar_productos, pedir_entero
from reportes import top_3_vendidos, productos_stock_bajo, resumen_semanal, ticket_promedio
from busquedas_ordenamientos import buscar_por_nombre, buscar_por_codigo, ordenar_por_precio, ordenar_por_nombre, ordenar_por_stock
from io_archivos import cargar_desde_binario_o_csv, guardar_en_csv, exportar_alertas, guardar_backup_binario
import datetime

# Matriz global de ventas por semana, que se usara mas adelante
ventas_semana = [
    [0, 0, 0],  # Lunes
    [0, 0, 0],  # Martes
    [0, 0, 0],  # Miércoles
    [0, 0, 0],  # Jueves
    [0, 0, 0],  # Viernes
    [0, 0, 0],  # Sábado
    [0, 0, 0]   # Domingo
]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

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
    
    return productos 

def registrar_venta(productos):
    """
    Registra una venta que puede incluir varios productos.
    Cada venta se asigna al día y franja horaria actual.
    """
    total_compra = 0
    venta = []

    hoy = datetime.datetime.today().weekday()
    
    while True:
        codigo = input("\nIngrese el código del producto: ").strip()
        producto = None
        for p in productos:
            if p['codigo'] == codigo:
                producto = p
                break

        if not producto:
            print("Código no encontrado.")
            opcion = input("¿Desea intentar con otro código? si = presione 's', no = presione otra tecla: ").lower()
            if opcion != 's':
                break
            else:
                continue

        print(f"Producto: {producto['nombre']} - Precio: Bs{producto['precio']} - Stock: {producto['stock']}")

        while True:
            try:
                cantidad = int(input("Cantidad a vender: "))
                if cantidad <= 0:
                    print("Debe ser mayor a 0.")
                elif cantidad > producto['stock']:
                    print(f"No hay suficiente stock disponible (Stock: {producto['stock']})")
                else:
                    break
            except ValueError:
                print("Debe ingresar un número válido.")

        producto['stock'] -= cantidad
        producto['vendidos_hoy'] += cantidad
        subtotal = cantidad * producto['precio']
        total_compra += subtotal
        venta.append({'nombre': producto['nombre'], 'cantidad': cantidad, 'subtotal': subtotal})

        hora_actual = datetime.datetime.now().hour
        if 6 <= hora_actual < 12:
            franja = 0  # Mañana
        elif 12 <= hora_actual < 18:
            franja = 1  # Tarde
        else:
            franja = 2  # Noche

        ventas_semana[hoy][franja] += subtotal


        continuar = input("¿Desea agregar otro producto a la venta? si = presione 's', no = presione otra tecla: ").lower()
        if continuar != 's':
            break

    if not venta:
        print("\nNo se registró ninguna venta.")
        return productos

    print("\nTICKET DE COMPRA")
    print("-" * 40)
    for item in venta:
        print(f"{item['nombre']} x{item['cantidad']}  Bs{item['subtotal']:.2f}")
    print("-" * 40)
    print(f"TOTAL A PAGAR: Bs{total_compra:.2f}")
    print("Venta registrada correctamente.")
    return productos

def mostrar_reportes(productos):
    """Submenú para mostrar diferentes reportes y estadísticas del kiosko."""
    print("\n REPORTES Y ESTADÍSTICAS")
    print("1. Top 3 productos más vendidos del día")
    print("2. Productos con stock bajo")
    print("3. Resumen semanal")
    print("4. Ticket promedio del día")
    print("5. Volver al menú principal")
    
    opcion = pedir_opcion("Seleccione una opción: ", 1, 6)
    
    if opcion == 1:
        top_3_vendidos(productos)
    elif opcion == 2:
        productos_stock_bajo(productos)
    elif opcion == 3:
        resumen_semanal(ventas_semana)
    elif opcion == 4:
        ticket_promedio(productos)
    elif opcion == 5:
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
