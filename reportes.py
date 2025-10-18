ventas_semana = [
    [0, 0, 0],  # Lunes: 
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
    Muestra productos vendidos hoy (los que tienen vendidos_hoy > 0)
    """
    print("\n PRODUCTOS VENDIDOS HOY:")
    print("-" * 50)
    
    productos_vendidos = [p for p in productos if p['vendidos_hoy'] > 0]
    
    if not productos_vendidos:
        print("No hay ventas registradas hoy")
        return
    
    for producto in productos_vendidos:
        print(f"{producto['nombre']} - Vendidos: {producto['vendidos_hoy']} - Total: Bs{producto['vendidos_hoy'] * producto['precio']:.2f}")

def productos_stock_bajo(productos):
    """
    Muestra productos con stock bajo (stock < stock_minimo)
    """
    print("\nPRODUCTOS CON STOCK BAJO:")
    print("-" * 50)
    
    productos_bajos = [p for p in productos if p['stock'] < p['stock_minimo']]
    
    if not productos_bajos:
        print("Todos los productos tienen stock suficiente")
        return
    
    for producto in productos_bajos:
        print(f"{producto['nombre']}")
        print(f"   Stock actual: {producto['stock']} | Mínimo requerido: {producto['stock_minimo']}")
        print(f"   Faltan: {producto['stock_minimo'] - producto['stock']} unidades")
        print()

def ventas_por_franja_horaria():
    """
    Ventas por franja horaria
    """
    print("\nVENTAS POR FRANJA HORARIA:")
    print("-" * 40)
    
    total_mañana = sum(dia[0] for dia in ventas_semana)
    total_tarde = sum(dia[1] for dia in ventas_semana)
    total_noche = sum(dia[2] for dia in ventas_semana)
    total_semana = total_mañana + total_tarde + total_noche
    
    if total_semana == 0:
        print("No hay ventas registradas en la semana")
        return
    
    print(f"Mañana:  Bs{total_mañana} ({(total_mañana/total_semana)*100:.1f}%)")
    print(f"Tarde:   Bs{total_tarde} ({(total_tarde/total_semana)*100:.1f}%)")
    print(f"Noche:   Bs{total_noche} ({(total_noche/total_semana)*100:.1f}%)")
    print(f"Total semanal: Bs{total_semana}")

def resumen_semanal():
    """
    Resumen semanal con matriz 2D
    """
    print("\nRESUMEN SEMANAL:")
    print("-" * 60)
    print(f"{'Día':<12} {'Mañana':<10} {'Tarde':<10} {'Noche':<10} {'Total':<10}")
    print("-" * 60)
    
    for i, dia in enumerate(ventas_semana):
        total_dia = sum(dia)
        print(f"{dias_semana[i]:<12} Bs{dia[0]:<8} Bs{dia[1]:<8} Bs{dia[2]:<8} Bs{total_dia:<8}")
    
    print("-" * 60)
    
    # Totales generales
    total_mañana = sum(dia[0] for dia in ventas_semana)
    total_tarde = sum(dia[1] for dia in ventas_semana)
    total_noche = sum(dia[2] for dia in ventas_semana)
    total_general = total_mañana + total_tarde + total_noche
    
    print(f"{'TOTAL':<12} Bs{total_mañana:<8} Bs{total_tarde:<8} Bs{total_noche:<8} Bs{total_general:<8}")


def obtener_vendidos(producto):
    """Función auxiliar para devolver los vendidos del producto (sin lambda)"""
    return producto.get('vendidos_hoy', 0)


def top_3_vendidos(productos):
    """
    Muestra el TOP 3 de productos más vendidos del día
    """
    print("\nTOP 3 PRODUCTOS MÁS VENDIDOS HOY:")
    print("-" * 50)
    
    productos_con_ventas = [p for p in productos if p.get('vendidos_hoy', 0) > 0]
    top_productos = sorted(productos_con_ventas, key=obtener_vendidos, reverse=True)[:3]
    
    if not top_productos:
        print("No hay ventas registradas hoy.")
        return
    
    for i, producto in enumerate(top_productos, 1):
        total = producto['vendidos_hoy'] * producto['precio']
        print(f"{i}° {producto['nombre']:<15} - {producto['vendidos_hoy']} unidades - Bs{total:.2f}")
        
def ticket_promedio(productos):
    """
    Calcula y muestra el ticket promedio del día
    """
    print("\nTICKET PROMEDIO DEL DÍA:")
    print("-" * 40)
    
    # Calcular ventas totales
    total_ventas = 0
    total_productos_vendidos = 0
    
    for producto in productos:
        ventas_producto = producto.get('vendidos_hoy', 0)
        if ventas_producto > 0:
            total_ventas += ventas_producto * producto['precio']
            total_productos_vendidos += ventas_producto
    
    if total_productos_vendidos == 0:
        print("No hay ventas registradas hoy")
        return
    
    # Calcular ticket promedio
    ticket_promedio = total_ventas / total_productos_vendidos
    
    print(f"Total ventas hoy: Bs{total_ventas:.2f}")
    print(f"Total productos vendidos: {total_productos_vendidos}")
    print(f"Ticket promedio: Bs{ticket_promedio:.2f} por producto")