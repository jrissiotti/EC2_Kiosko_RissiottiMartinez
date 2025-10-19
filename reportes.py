ventas_semana = [
    [0, 0, 0],  # Lunes: mañana, tarde, noche
    [0, 0, 0],  # Martes
    [0, 0, 0],  # Miércoles
    [0, 0, 0],  # Jueves
    [0, 0, 0],  # Viernes
    [0, 0, 0],  # Sábado
    [0, 0, 0]   # Domingo
]

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

def productos_vendidos_hoy(productos):
    """
    Muestra los productos vendidos hoy.

    Parámetros:
        productos (list[dict]): Lista de productos con clave 'vendidos_hoy'.
    """
    print("\nPRODUCTOS VENDIDOS HOY")
    print("-" * 50)

    vendidos = [p for p in productos if p.get('vendidos_hoy', 0) > 0]
    
    if not vendidos:
        print("No se registraron ventas hoy")
        return
    
    for p in vendidos:
        total = p['vendidos_hoy'] * p['precio']
        print(f"{p['nombre']} - Vendidos: {p['vendidos_hoy']} - Total: Bs{total:.2f}")


def productos_stock_bajo(productos):
    """
    Muestra los productos cuyo stock es menor al mínimo requerido.

    Parámetros:
        productos (list[dict]): Lista de productos con 'stock' y 'stock_minimo'.
    """
    print("\nPRODUCTOS CON STOCK BAJO")
    print("-" * 50)

    bajos = [p for p in productos if p['stock'] < p['stock_minimo']]

    if not bajos:
        print("Todos los productos tienen stock suficiente")
        return

    for p in bajos:
        print(f"Producto '{p['nombre']}' - Stock actual: {p['stock']} | Mínimo requerido: {p['stock_minimo']} | Faltan: {p['stock_minimo'] - p['stock']} unidades")


def ventas_por_franja_horaria():
    """
    Muestra las ventas totales por franja horaria de la semana.
    Usa la matriz ventas_semana [7 días x 3 franjas].
    """
    print("\nVENTAS POR FRANJA HORARIA")
    print("-" * 50)

    total_mañana = sum(max(0, dia[0]) for dia in ventas_semana)
    total_tarde = sum(max(0, dia[1]) for dia in ventas_semana)
    total_noche = sum(max(0, dia[2]) for dia in ventas_semana)
    total_semana = total_mañana + total_tarde + total_noche

    if total_semana == 0:
        print("No hay ventas registradas en la semana")
        return

    print(f"Mañana: Bs{total_mañana} ({(total_mañana/total_semana)*100:.1f}%)")
    print(f"Tarde:  Bs{total_tarde} ({(total_tarde/total_semana)*100:.1f}%)")
    print(f"Noche:  Bs{total_noche} ({(total_noche/total_semana)*100:.1f}%)")
    print(f"Total semanal: Bs{total_semana}")


def resumen_semanal():
    """
    Imprime un resumen de ventas de la semana usando la matriz ventas_semana.
    """
    print("\nRESUMEN SEMANAL")
    print("-" * 60)
    print(f"{'Día':<12} {'Mañana':<10} {'Tarde':<10} {'Noche':<10} {'Total':<10}")
    print("-" * 60)

    totales_mañana = totales_tarde = totales_noche = 0

    for i, dia in enumerate(ventas_semana):
        dia_totales = [max(0, v) for v in dia]
        total_dia = sum(dia_totales)
        print(f"{dias_semana[i]:<12} Bs{dia_totales[0]:<8} Bs{dia_totales[1]:<8} Bs{dia_totales[2]:<8} Bs{total_dia:<8}")
        totales_mañana += dia_totales[0]
        totales_tarde += dia_totales[1]
        totales_noche += dia_totales[2]

    total_general = totales_mañana + totales_tarde + totales_noche
    print("-" * 60)
    print(f"{'TOTAL':<12} Bs{totales_mañana:<8} Bs{totales_tarde:<8} Bs{totales_noche:<8} Bs{total_general:<8}")


def top_3_vendidos(productos):
    """
    Muestra los 3 productos más vendidos hoy.
    """
    print("\nTOP 3 PRODUCTOS MÁS VENDIDOS HOY")
    print("-" * 50)

    vendidos = [p for p in productos if p.get('vendidos_hoy', 0) > 0]
    top = sorted(vendidos, key=lambda p: p['vendidos_hoy'], reverse=True)[:3]

    if not top:
        print("No hay ventas registradas hoy")
        return

    for i, p in enumerate(top, 1):
        total = p['vendidos_hoy'] * p['precio']
        print(f"{i}° {p['nombre']:<15} - {p['vendidos_hoy']} unidades - Bs{total:.2f}")


def ticket_promedio(productos):
    """
    Calcula y muestra el ticket promedio por producto vendido hoy.
    """
    print("\nTICKET PROMEDIO DEL DÍA")
    print("-" * 40)

    total_ventas = sum(p['vendidos_hoy'] * p['precio'] for p in productos if p['vendidos_hoy'] > 0)
    total_productos = sum(p['vendidos_hoy'] for p in productos if p['vendidos_hoy'] > 0)

    if total_productos == 0:
        print("No hay ventas registradas hoy")
        return

    ticket = total_ventas / total_productos
    print(f"Total ventas hoy: Bs{total_ventas:.2f}")
    print(f"Total productos vendidos: {total_productos}")
    print(f"Ticket promedio: Bs{ticket:.2f} por producto")
