# main.py
import tkinter as tk
from tkinter import messagebox
from libros_json import guardar_libros, cargar_libros #importo las funciones de el archivo libros_json
from funciones import agregar_libro, buscar_libros, actualizar_estado # importo las funciones del archivo funciones

# Cargar libros al inicio
libros = cargar_libros()

# Función para registrar un libro desde GUI
def registrar():
    global libros
    titulo = entrada_titulo.get()
    autor = entrada_autor.get()
    categoria = categoria_var.get()
    if titulo and autor:
        nuevo = {"titulo": titulo, "autor": autor, "categoria": categoria, "estado": "disponible"}
        libros = agregar_libro(libros, nuevo)
        guardar_libros(libros)  # Guardar después de registrar
        messagebox.showinfo("Éxito", "Libro registrado exitosamente")
        entrada_titulo.delete(0, tk.END)
        entrada_autor.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Debe ingresar título y autor")

# Función para buscar libros y mostrarlos
def buscar():
    criterio = criterio_var.get().lower()
    valor = entrada_busqueda.get()
    resultado = buscar_libros(libros, criterio, valor)
    mostrar_resultado(resultado)

# Función para mostrar resultados en lista
def mostrar_resultado(lista):
    area_resultado.delete(1.0, tk.END)
    for libro in lista:
        texto = f"{libro['titulo']} - {libro['autor']} - {libro['categoria']} - {libro['estado']}\n"
        area_resultado.insert(tk.END, texto)

# Cambia el estado del libro (prestado/devuelto)
def cambiar_estado(nuevo_estado):
    global libros
    titulo = entrada_estado.get()
    libros = actualizar_estado(libros, titulo, nuevo_estado)
    guardar_libros(libros)
    messagebox.showinfo("Actualizado", f"Estado cambiado a '{nuevo_estado}' para '{titulo}'")

# GUI principal
ventana = tk.Tk()
ventana.title("Biblioteca Funcional")

# --- Registro de libros ---
tk.Label(ventana, text="Título").grid(row=0, column=0)
entrada_titulo = tk.Entry(ventana)
entrada_titulo.grid(row=0, column=1)

tk.Label(ventana, text="Autor").grid(row=1, column=0)
entrada_autor = tk.Entry(ventana)
entrada_autor.grid(row=1, column=1)

tk.Label(ventana, text="Categoría").grid(row=2, column=0)
categoria_var = tk.StringVar(ventana)
categoria_var.set("Literatura")
tk.OptionMenu(ventana, categoria_var, "Literatura", "Ciencia", "Ingeniería").grid(row=2, column=1)

tk.Button(ventana, text="Registrar libro", command=registrar).grid(row=3, columnspan=2, pady=5)

# --- Búsqueda de libros ---
tk.Label(ventana, text="Buscar por").grid(row=4, column=0)
criterio_var = tk.StringVar(ventana)
criterio_var.set("Título")
tk.OptionMenu(ventana, criterio_var, "Título", "Autor").grid(row=4, column=1)

entrada_busqueda = tk.Entry(ventana)
entrada_busqueda.grid(row=5, column=0, columnspan=2)

tk.Button(ventana, text="Buscar", command=buscar).grid(row=6, columnspan=2, pady=5)

# --- Resultado de búsqueda ---
area_resultado = tk.Text(ventana, height=10, width=50)
area_resultado.grid(row=7, columnspan=2, padx=5, pady=5)

# --- Cambiar estado de préstamo ---
tk.Label(ventana, text="Título para cambiar estado").grid(row=8, columnspan=2)
entrada_estado = tk.Entry(ventana)
entrada_estado.grid(row=9, columnspan=2)

tk.Button(ventana, text="Marcar como prestado", command=lambda: cambiar_estado("prestado")).grid(row=10, column=0)
tk.Button(ventana, text="Marcar como disponible", command=lambda: cambiar_estado("disponible")).grid(row=10, column=1)

ventana.mainloop()
