def buscar_por_nombre(productos, nombre_buscar):
    """
    Búsqueda lineal por nombre
    """
    print(f"\nBUSCANDO: '{nombre_buscar}'")
    print("-" * 50)
    
    resultados = []
    for producto in productos:
        if nombre_buscar.lower() in producto['nombre'].lower():
            resultados.append(producto)
    
    if not resultados:
        print("No se encontraron productos con ese nombre")
        return
    
    print(f"Se encontraron {len(resultados)} productos:")
    for producto in resultados:
        print(f"   {producto['nombre']} - Código: {producto['codigo']} - Precio: Bs{producto['precio']} - Stock: {producto['stock']}")

def obtener_codigo(producto):
    """Función auxiliar para obtener el código del producto"""
    return producto['codigo']

def buscar_por_codigo(productos, codigo_buscar):
    """
    Búsqueda binaria por código
    """
    print(f"\nBUSCANDO CÓDIGO: '{codigo_buscar}'")
    print("-" * 50)
    
    # Ordenar productos por código para búsqueda binaria
    productos_ordenados = sorted(productos, key=obtener_codigo)
    
    izquierda, derecha = 0, len(productos_ordenados) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        producto_medio = productos_ordenados[medio]
        
        if producto_medio['codigo'] == codigo_buscar:
            print(f"PRODUCTO ENCONTRADO:")
            print(f"   Nombre: {producto_medio['nombre']}")
            print(f"   Código: {producto_medio['codigo']}")
            print(f"   Precio: Bs{producto_medio['precio']}")
            print(f"   Stock: {producto_medio['stock']}")
            return
        
        elif producto_medio['codigo'] < codigo_buscar:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    print("No se encontró un producto con ese código")
def ordenar_por_precio(productos):
    """
    Ordenamiento por precio ascendente - Método burbuja
    """
    print("\n ORDENANDO POR PRECIO MÁS BARATO A MÁS CARO")
    print("-" * 50)
    
    lista_ordenada = productos.copy()
    n = len(lista_ordenada)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_ordenada[j]['precio'] > lista_ordenada[j + 1]['precio']:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
    
    for producto in lista_ordenada:
        print(f"   Bs{producto['precio']:<6} - {producto['nombre']}")

def ordenar_por_nombre(productos):
    """
    Ordenamiento por nombre (A-Z) - Método selección
    """
    print("\n📊 ORDENANDO POR NOMBRE (A-Z)")
    print("-" * 50)
    
    lista_ordenada = productos.copy()
    n = len(lista_ordenada)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista_ordenada[j]['nombre'] < lista_ordenada[min_idx]['nombre']:
                min_idx = j
        lista_ordenada[i], lista_ordenada[min_idx] = lista_ordenada[min_idx], lista_ordenada[i]
    
    for producto in lista_ordenada:
        print(f"   {producto['nombre']}")

def ordenar_por_stock(productos):
    """
    Ordenamiento por stock (descendente) - Método burbuja
    """
    print("\nORDENANDO POR STOCK (MAYOR A MENOR)")
    print("-" * 50)
    
    lista_ordenada = productos.copy()
    n = len(lista_ordenada)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_ordenada[j]['stock'] < lista_ordenada[j + 1]['stock']:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
    
    for producto in lista_ordenada:
        print(f"   Stock: {producto['stock']:<3} - {producto['nombre']}")