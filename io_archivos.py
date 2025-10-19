import csv
import pickle
import os

def cargar_desde_csv():
    """
    Carga los productos desde datos.csv
    Valida que cada fila tenga datos correctos.
    """
    productos = []
    if not os.path.exists('datos.csv'):
        print("Archivo datos.csv no encontrado. Se crearán productos demo.")
        return productos  # Se pueden agregar 5-10 productos demo aquí si quieres

    with open('datos.csv', 'r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                producto = {
                    'codigo': fila['codigo'].strip(),
                    'nombre': fila['nombre'].strip(),
                    'precio': float(fila['precio']),
                    'stock': int(fila['stock']),
                    'stock_minimo': int(fila['stock_minimo']),
                    'vendidos_hoy': 0
                }
                if producto['precio'] < 0 or producto['stock'] < 0 or producto['stock_minimo'] < 0:
                    print(f"Producto '{producto['nombre']}' ignorado: valores negativos")
                    continue
                productos.append(producto)
            except (ValueError, KeyError, AttributeError):
                nombre = fila.get('nombre', 'desconocido') if isinstance(fila, dict) else 'desconocido'
                print(f"Producto '{nombre}' ignorado por datos inválidos")
    print(f"Datos cargados desde CSV correctamente. Total productos válidos: {len(productos)}")
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

def guardar_backup_binario(productos):
    """
    Guarda la lista de productos en datos.bin usando pickle
    """
    try:
        with open('datos.bin', 'wb') as archivo_bin:
            pickle.dump(productos, archivo_bin)
        print("Backup binario guardado correctamente")
    except Exception as e:
        print(f"Error al guardar backup binario: {e}")
    
def cargar_desde_binario_o_csv():
    """
    Intenta cargar datos desde datos.bin; si falla o no existe, carga datos.csv
    """
    productos = []
    if os.path.exists('datos.bin'):
        try:
            with open('datos.bin', 'rb') as archivo_bin:
                productos = pickle.load(archivo_bin)
            print("Datos cargados desde buckup binario correctamente")
        except Exception:
            print(f"Error al cargar backup binario")
            productos = cargar_desde_csv()
    else:
        productos = cargar_desde_csv()
    
    return productos
