import json
import requests
import os

# Estructura de datos: Lista de diccionarios (Catálogo harcodeado como base de la tienda)
CATALOGO = [
    {"id": 1, "nombre": "Procesador AMD Ryzen 7 9800X3D", "precio": 450000},
    {"id": 2, "nombre": "Tarjeta Gráfica RTX 5070", "precio": 650000},
    {"id": 3, "nombre": "Mouse VXE R1 PRO Max", "precio": 45000},
    {"id": 4, "nombre": "Memoria RAM 32GB DDR5", "precio": 120000}
]

def obtener_catalogo():
    """Retorna el catálogo disponible."""
    return CATALOGO

def buscar_producto_por_id(id_producto):
    """Busca un producto en el catálogo. Retorna el diccionario o None."""
    for producto in CATALOGO:
        if producto["id"] == id_producto:
            return producto
    return None

def agregar_al_carrito(carrito, id_producto, cantidad):
    """
    Agrega un producto al carrito o actualiza su cantidad.
    El carrito es un diccionario de diccionarios.
    """
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a 0.")
        
    producto = buscar_producto_por_id(id_producto)
    
    if not producto:
        raise KeyError("El producto seleccionado no existe en el catálogo.")
        
    id_str = str(id_producto) # Usamos string como llave para compatibilidad con JSON
    if id_str in carrito:
        carrito[id_str]["cantidad"] += cantidad
    else:
        # Se agrega usando una estructura compuesta
        carrito[id_str] = {
            "nombre": producto["nombre"],
            "precio": producto["precio"],
            "cantidad": cantidad
        }
    return True

def calcular_total_clp(carrito):
    """Calcula el total de la compra iterando sobre los items del carrito."""
    total = 0
    for item in carrito.values():
        total += item["precio"] * item["cantidad"]
    return total

def vaciar_carrito():
    """Retorna un carrito vacío (diccionario limpio)."""
    return {}

def obtener_valor_dolar():
    """
    Consume la API de mindicador.cl para obtener el valor actual del dólar.
    Retorna el valor en float. Si falla, retorna un valor de contingencia.
    """
    try:
        respuesta = requests.get("https://mindicador.cl/api/dolar", timeout=5)
        respuesta.raise_for_status() # Verifica que la petición fue exitosa (código 200)
        datos = respuesta.json()
        valor_actual = datos["serie"][0]["valor"]
        return float(valor_actual)
    except Exception:
        # En caso de no tener internet o caída de la API
        return 950.0 

def guardar_carrito(carrito, ruta_archivo="carrito.json"):
    """Guarda el estado actual del carrito en un archivo JSON (Persistencia w)."""
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        json.dump(carrito, archivo, indent=4)

def cargar_carrito(ruta_archivo="carrito.json"):
    """Carga el carrito desde un archivo JSON al iniciar (Persistencia r)."""
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                return {} # Si el archivo está corrupto, retorna carrito vacío
    return {}