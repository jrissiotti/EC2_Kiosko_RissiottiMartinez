def mostrar_productos(productos):
    """
    Muestra todos los productos en formato tabla
    """
    
    print("\nINVENTARIO COMPLETO:")
    print("-" * 80)
    print(f"{'Código':<10} {'Nombre':<20} {'Precio':<10} {'Stock':<10} {'Stock Mín':<10}")
    print("-" * 80)
    
    for producto in productos:
        print(f"{producto['codigo']:<10} {producto['nombre']:<20} Bs{producto['precio']:<9} {producto['stock']:<10} {producto['stock_minimo']:<10}")
    print("-" * 80)

def agregar_producto(productos):
    """
    Agrega un nuevo producto al inventario
    """
    print("\nAGREGAR NUEVO PRODUCTO")
    
    codigo = input("Código del producto (ej: A1-001): ")
    
    # Verificar si el código ya existe
    for producto in productos:
        if producto['codigo'] == codigo:
            print("Error: Ya existe un producto con ese código")
            return productos
    
    nombre = input("Nombre del producto: ")
    
    #TODO: Validaciones para volver a pedir, aceptaar numeros positivos y segun el caso, numeros enteros
    try:
        precio = float(input("Precio: "))
        stock = int(input("Stock inicial: "))
        stock_minimo = int(input("Stock mínimo: "))
    except ValueError:
        print("Error, deben ser solo números")
        return productos
    
    # Crear nuevo producto
    nuevo_producto = {
        'codigo': codigo,
        'nombre': nombre,
        'precio': precio,
        'stock': stock,
        'stock_minimo': stock_minimo,
        'vendidos_hoy': 0
    }
    
    productos.append(nuevo_producto)
    print(f"Producto '{nombre}' agregado correctamente")
    return productos

def eliminar_producto(productos):
    """
    Elimina un producto del inventario por código
    """
    print("\nELIMINAR PRODUCTO")
    mostrar_productos(productos)
    
    codigo = input("Código del producto a eliminar: ")
    
    for i, producto in enumerate(productos):
        if producto['codigo'] == codigo:
            confirmar = input(f"¿Está seguro de eliminar '{producto['nombre']}'? (s/n): ")
            if confirmar.lower() == 's':
                producto_eliminado = productos.pop(i)
                print(f"Producto '{producto_eliminado['nombre']}' eliminado")
                return productos
            else:
                print("Eliminación cancelada exitosamente")
                return productos
    
    print("No se encontró un producto con ese código")
    return productos

def modificar_producto(productos):
    """
    Modifica los datos de un producto existente
    """
    print("\nMODIFICAR PRODUCTO")
    mostrar_productos(productos)
    
    
    codigo = input("Código del producto a modificar: ")
    
    for producto in productos:
        if producto['codigo'] == codigo:
            print(f"\nModificando: {producto['nombre']}")
            print("IMPORTANTE: Si no algun campo del producto, presione enter para mantener el valor actual")
            
            nuevo_nombre = input(f"Nuevo nombre [{producto['nombre']}]: ")
            if nuevo_nombre:
                producto['nombre'] = nuevo_nombre
            
            #TODO: Validaciones para volver a pedir, aceptaar numeros positivos y segun el caso, numeros enteros
            try:
                nuevo_precio = input(f"Nuevo precio [Bs{producto['precio']}]: ")
                if nuevo_precio:
                    producto['precio'] = float(nuevo_precio)
                
                nuevo_stock = input(f"Nuevo stock [{producto['stock']}]: ")
                if nuevo_stock:
                    producto['stock'] = int(nuevo_stock)
                
                nuevo_minimo = input(f"Nuevo stock mínimo [{producto['stock_minimo']}]: ")
                if nuevo_minimo:
                    producto['stock_minimo'] = int(nuevo_minimo)
                    
            except ValueError:
                print("Error: Los valores deben ser números válidos")
                return productos
            
            print(f"Producto '{producto['nombre']}' modificado correctamente")
            return productos
    
    print("No se encontró un producto con ese código")
    return productos

def reabastecer_stock(productos):
    """
    Aumenta el stock de un producto
    """
    print("\n📦 REABASTECER STOCK")
    mostrar_productos(productos)
    
    codigo = input("Código del producto a reabastecer: ")
    
    for producto in productos:
        if producto['codigo'] == codigo:
            try:
                #TODO: Valida que cantidad sea un numero entero y volver a pedir
                cantidad = int(input(f"Cantidad a agregar al stock de '{producto['nombre']}': "))
                if cantidad <= 0:
                    print("Error: La cantidad debe ser mayor a 0")
                    return productos
                
                producto['stock'] += cantidad
                print(f"Stock de '{producto['nombre']}' actualizado: {producto['stock'] - cantidad} a {producto['stock']}")
                return productos
                
            except ValueError:
                print("Error: La cantidad debe ser un número")
                return productos
    
    print("No se encontró un producto con ese código")
    return productos