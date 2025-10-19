def pedir_entero(mensaje, min_val=1):
    """
    Solicita al usuario un número entero mayor o igual a min_val.
    
    Parámetros:
        mensaje (str): Texto a mostrar al usuario.
        min_val (int): Valor mínimo permitido (por defecto 1).
    
    Retorna:
        int: Número entero ingresado por el usuario.
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor < min_val:
                print(f"Debe ser >= {min_val}")
            else:
                return valor
        except ValueError:
            print("Debe ingresar un número válido")


def mostrar_productos(productos):
    """
    Muestra todos los productos del inventario en una tabla ordenada.
    
    Parámetros:
        productos (list): Lista de diccionarios con los datos de los productos.
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
    Agrega un nuevo producto al inventario con validaciones.
    
    Parámetros:
        Lista de productos existente.
    
    Retorna:
        Lista de productos actualizada.
    """
    print("\nAGREGAR NUEVO PRODUCTO")

    while True:
        codigo = input("Código del producto (ej: A1-001): ").strip().upper()
        if any(p['codigo'] == codigo for p in productos):
            resp = input("Error, este código ya existe. ¿Desea intentar con otro? si = presione 's', no = presione cualquier otra trecla: ").lower()
            if resp != 's':
                print("Producto no agregado.")
                return productos
            else:
                continue
        break

    # Validar nombre
    while True:
        nombre = input("Nombre del producto: ").strip()
        if any(p['nombre'].lower() == nombre.lower() for p in productos):
            resp = input("Error, este nombre ya existe. ¿Desea intentar con otro? si = presione 's', no = presione cualquier otra trecla: ").lower()
            if resp != 's':
                print("Producto no agregado.")
                return productos
            else:
                continue
        break

    
    while True:
        try:
            precio = float(input("Precio: "))
            if precio <= 0:
                print("Debe ser un número mayor a 0")
            else:
                break
        except ValueError:
            print("Debe ingresar un número válido")
    
    stock = pedir_entero("Stock inicial: ")
    stock_minimo = pedir_entero("Stock mínimo: ")
    
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
    Elimina un producto del inventario por código.
    
    Parámetros:
        Lista de productos existente.
    
    Retorna:
        Lista de productos actualizada.
    """
    print("\nELIMINAR PRODUCTO")
    
    # En caso de eliminar todos los productos incluidos los demo:
    if not productos:
        print("No hay productos en el inventario para eliminar.")
        return productos
    
    mostrar_productos(productos)
    
    while True:
        codigo = input("Introduce el código del producto a eliminar: ").strip()
        
        for i, producto in enumerate(productos):
            if producto['codigo'] == codigo:
                confirmar = input(f"¿Está seguro de eliminar el producto: '{producto['nombre']}'? si = presione 's', no = presione otra tecla: ").lower()
                if confirmar == 's':
                    producto_eliminado = productos.pop(i)
                    print(f"Producto '{producto_eliminado['nombre']}' eliminado")
                    return productos
                else:
                    print("Eliminación cancelada.")
                    return productos
        
        # Si no se encontró el código
        print("No se encontró un producto con ese código.")
        resp = input("¿Desea intentar con otro código? si = presione 's', no = presione otra tecla: ").lower()
        if resp != 's':
            print("No se eliminó ningún producto.")
            return productos


def modificar_producto(productos):
    """
    Modifica los datos de un producto existente con validaciones.
    
    Permite cambiar:
        - Nombre (ejemplo: de "Coca Cola" a "Coca Cola normal", esto debido a que existe coca cola zero, etc)
        - Precio (float > 0)
        - Stock mínimo (int >= 0)
    No permite cambiar:
        - Stock (considero que tambien deberia poder modificarse, pero solo en sistemas que se controlen
                 vencimientos o cosas asi, pero en este caso no)
    Parámetros:
        productos (list): Lista de productos existente.
    
    Retorna:
        list: Lista de productos actualizada.
    """
    print("\nMODIFICAR PRODUCTO")
    if not productos:
        print("No hay productos en el inventario para modificar.")
        return productos
    
    mostrar_productos(productos)
    
    while True:
        codigo = input("Código del producto a modificar: ").strip()
        
        for producto in productos:
            if producto['codigo'] == codigo:
                print(f"\nModificando: {producto['nombre']}")
                print("IMPORTANTE: Si no desea cambiar un campo, presione Enter")
                
                nuevo_nombre = input(f"Nuevo nombre (Actual: {producto['nombre']}): ").strip()
                if nuevo_nombre:
                    producto['nombre'] = nuevo_nombre
                    
                while True:
                    nuevo_precio = input(f"Nuevo precio (Actual: Bs{producto['precio']}): ").strip()
                    
                    if not nuevo_precio:
                        break
                    try:
                        valor = float(nuevo_precio)
                        if valor <= 0:
                            print("Debe ser mayor a 0")
                        elif valor == producto['precio']:
                            opcion = input("Ingresó el mismo precio. ¿Desea mantenerlo o intentar nuevamente? s = mantener, otra letra = intentar nuevamente: ").lower()
                            if opcion == 's':
                                break
                            else:
                                continue  
                        else:
                            producto['precio'] = valor
                            break
                    except ValueError:
                        print("Debe ingresar un número válido")


                while True:
                    nuevo_minimo = input(f"Nuevo stock mínimo (Actual: {producto['stock_minimo']}): ").strip()
                    
                    if not nuevo_minimo:
                        break
                    try:
                        valor_min = int(nuevo_minimo)
                        if valor_min < 0:
                            print("Debe ser >= 0")
                        elif valor_min == producto['stock_minimo']:
                            opcion = input("Ingresó el mismo stock mínimo. ¿Desea mantenerlo? (s/n): ").lower()
                            if opcion == 's':
                                break
                            else:
                                continue
                        else:
                            producto['stock_minimo'] = valor_min
                            break
                    except ValueError:
                        print("Debe ingresar un número válido")
                
                print(f"Producto '{producto['nombre']}' modificado correctamente")
                return productos
        
        # Si no se encontró el código
        print("No se encontró un producto con ese código.")
        resp = input("¿Desea intentar con otro código? si = presione 's', no = presione otra tecla: ").lower()
        if resp != 's':
            print("No se modificó ningún producto.")
            return productos


def reabastecer_stock(productos):
    """
    Aumenta el stock de un producto con validación.
    
    Parámetros:
        productos (list): Lista de productos existente.
    
    Retorna:
        list: Lista de productos actualizada.
    """
    print("\n📦 REABASTECER STOCK")
    while True:
        mostrar_productos(productos)
        
        codigo = input("Código del producto a reabastecer: ")
        producto_encontrado = None
        
        for producto in productos:
            if producto['codigo'] == codigo:
                producto_encontrado = producto
                break
        
        if producto_encontrado is None:
            print(f"No se encontró un producto con código '{codigo}'")
            opcion = input("¿Desea intentar otro código? si = presione 's', no = presione otra tecla: ").lower()
            if opcion != 's':
                break
            else:
                continue
        
        cantidad = pedir_entero(f"Cantidad a agregar al stock de '{producto_encontrado['nombre']}': ")
        stock_anterior = producto_encontrado['stock']
        producto_encontrado['stock'] += cantidad
        print(f"Stock de '{producto_encontrado['nombre']}' actualizado: {stock_anterior} a {producto_encontrado['stock']}")
        
        # Preguntar si desea reabastecer otro producto
        opcion = input("¿Desea reabastecer otro producto? si = presione 's', no = presione otra tecla: ").lower()
        if opcion != 's':
            break
    
    return productos