dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

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


def resumen_semanal(ventas_semana):
    """
    Imprime un resumen de ventas de la semana usando la matriz ventas_semana.
    """
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    print("\nRESUMEN SEMANAL")
    print("-" * 60)
    print(f"{'Día':<12} {'Mañana':<10} {'Tarde':<10} {'Noche':<10} {'Total':<10}")
    print("-" * 60)

    totales_mañana = totales_tarde = totales_noche = 0

    for i, dia in enumerate(ventas_semana):
        total_dia = sum(dia)
        print(f"{dias_semana[i]:<12} Bs{dia[0]:<8} Bs{dia[1]:<8} Bs{dia[2]:<8} Bs{total_dia:<8}")
        totales_mañana += dia[0]
        totales_tarde += dia[1]
        totales_noche += dia[2]

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
