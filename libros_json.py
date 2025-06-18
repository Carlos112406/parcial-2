import json
import os

ARCHIVO_LIBROS = "libros.json"

# Guarda la lista de libros en un archivo JSON
def guardar_libros(libros, archivo=ARCHIVO_LIBROS):
    with open(archivo, 'w') as f:
        json.dump(libros, f, indent=2, ensure_ascii=False)  # indent=2 para que los textos tengan sangria de 2

# Carga los libros desde el archivo si existe, o retorna una lista vacía
def cargar_libros(archivo=ARCHIVO_LIBROS):
    if not os.path.exists(archivo):
        return []  # Si el archivo no existe, empezamos con lista vacía
    with open(archivo, 'r') as f:
        return json.load(f)  # Lee y transforma JSON a lista de dicts