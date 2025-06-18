# Agrega un nuevo libro a la lista (sin mutarla)
def agregar_libro(libros, nuevo_libro):
    return libros + [nuevo_libro]  # Retorna nueva lista con el libro añadido

# Busca libros por título o autor 
def buscar_libros(libros, criterio, valor):
    return list(filter(lambda libro: valor.lower() in libro[criterio].lower(), libros))  # Filtro por coincidencia

# Cambia el estado (disponible/prestado) de un libro sin mutarlo
def actualizar_estado(libros, titulo, nuevo_estado):
    return [
        dict(libro, estado=nuevo_estado) if libro['titulo'] == titulo else libro
        for libro in libros
    ]  # Nueva lista con el libro actualizado
