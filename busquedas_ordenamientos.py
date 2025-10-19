def buscar_por_nombre(productos, nombre_buscar):
    """
    Búsqueda lineal por nombre (parcial o completo, insensible a mayúsculas).

    Parámetros:
        productos (list[dict]): Lista de productos.
        nombre_buscar (str): Nombre o parte del nombre a buscar.
    """
    if not nombre_buscar.strip():
        print("Debe ingresar un nombre válido")
        return

    print(f"\nBUSCANDO PRODUCTOS CON NOMBRE: '{nombre_buscar}'")
    print("-" * 60)
    
    resultados = [p for p in productos if nombre_buscar.lower() in p['nombre'].lower()]
    
    if not resultados:
        print("No se encontraron productos con ese nombre")
        return

    print(f"Se encontraron {len(resultados)} producto(s):")
    for p in resultados:
        print(f"{p['nombre']:<20} | Código: {p['codigo']} | Precio: Bs{p['precio']:<6} | Stock: {p['stock']}")


def obtener_codigo(producto):
    """Función auxiliar para obtener el código del producto"""
    return producto['codigo']


def buscar_por_codigo(productos, codigo_buscar):
    """
    Búsqueda binaria por código. Ordena internamente por código.

    Parámetros:
        productos (list[dict]): Lista de productos.
        codigo_buscar (str): Código exacto del producto.
    """
    if not codigo_buscar.strip():
        print("Debe ingresar un código válido")
        return

    print(f"\nBUSCANDO PRODUCTO CON CÓDIGO: '{codigo_buscar}'")
    print("-" * 60)

    productos_ordenados = sorted(productos, key=obtener_codigo)
    izquierda, derecha = 0, len(productos_ordenados) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        p = productos_ordenados[medio]
        
        if p['codigo'] == codigo_buscar:
            print("PRODUCTO ENCONTRADO:")
            print(f"{p['nombre']:<20} | Código: {p['codigo']} | Precio: Bs{p['precio']:<6} | Stock: {p['stock']}")
            return
        elif p['codigo'] < codigo_buscar:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    print("No se encontró un producto con ese código")


def ordenar_por_precio(productos):
    """Muestra los productos ordenados por precio ascendente (menor a mayor)"""
    print("\nORDENANDO POR PRECIO (MENOR A MAYOR)")
    print("-" * 60)

    for p in sorted(productos, key=lambda x: x['precio']):
        print(f"Bs{p['precio']:<6} | {p['nombre']}")


def ordenar_por_nombre(productos):
    """Muestra los productos ordenados por nombre (A-Z)"""
    print("\nORDENANDO POR NOMBRE (A-Z)")
    print("-" * 60)

    for p in sorted(productos, key=lambda x: x['nombre']):
        print(f"{p['nombre']}")


def ordenar_por_stock(productos):
    """Muestra los productos ordenados por stock descendente (mayor a menor)"""
    print("\nORDENANDO POR STOCK (MAYOR A MENOR)")
    print("-" * 60)

    for p in sorted(productos, key=lambda x: x['stock'], reverse=True):
        print(f"Stock: {p['stock']:<3} | {p['nombre']}")
