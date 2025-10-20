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
    """Ordena y muestra los productos por precio (menor a mayor) usando burbuja"""
    print("\nORDENANDO POR PRECIO (MENOR A MAYOR)")
    print("-" * 60)

    lista = productos.copy()
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]['precio'] > lista[j + 1]['precio']:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    for p in lista:
        print(f"Bs{p['precio']:<6} | {p['nombre']}")


def ordenar_por_nombre(productos):
    """Ordena y muestra los productos por nombre (A-Z) usando selección"""
    print("\nORDENANDO POR NOMBRE (A-Z)")
    print("-" * 60)

    lista = productos.copy()
    n = len(lista)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j]['nombre'] < lista[min_idx]['nombre']:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

    for p in lista:
        print(f"{p['nombre']}")


def ordenar_por_stock(productos):
    """Ordena y muestra los productos por stock (menor a mayor) usando burbuja"""
    print("\nORDENANDO POR STOCK (MENOR A MAYOR)")
    print("-" * 60)

    lista = productos.copy()
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]['stock'] > lista[j + 1]['stock']:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    for p in lista:
        print(f"Stock: {p['stock']:<3} | {p['nombre']}")
