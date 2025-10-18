import csv

def cargar_desde_csv():
    """
    Carga los productos desde datos.csv
    """
    productos = []
    with open('datos.csv', 'r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            producto = {
                'codigo': fila['codigo'],
                'nombre': fila['nombre'],
                'precio': float(fila['precio']),
                'stock': int(fila['stock']),
                'stock_minimo': int(fila['stock_minimo']),
                'vendidos_hoy': 0 #Inicializamos
            }
            productos.append(producto)
    print("Datos cargados desde CSV correctamente")
    return productos

def guardar_en_csv(productos):
    """
    Guarda la lista de productos en datos.csv
    """
    with open('datos.csv', 'w', newline='', encoding='utf-8') as archivo:
        campos = ['codigo', 'nombre', 'precio', 'stock', 'stock_minimo']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for producto in productos:
            escritor.writerow({
                'codigo': producto['codigo'],
                'nombre': producto['nombre'],
                'precio': producto['precio'],
                'stock': producto['stock'],
                'stock_minimo': producto['stock_minimo']
            })
    print("Datos guardados en CSV correctamente")

def exportar_alertas(productos):
    """
    Exporta productos con stock bajo a alertas.csv
    """
    productos_bajos = [p for p in productos if p['stock'] < p['stock_minimo']]
    
    with open('alertas.csv', 'w', newline='', encoding='utf-8') as archivo:
        campos = ['codigo', 'nombre', 'stock_actual', 'stock_minimo']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for producto in productos_bajos:
            escritor.writerow({
                'codigo': producto['codigo'],
                'nombre': producto['nombre'],
                'stock_actual': producto['stock'],
                'stock_minimo': producto['stock_minimo']
            })
    print(f"Alertas exportadas: {len(productos_bajos)} productos con stock bajo")