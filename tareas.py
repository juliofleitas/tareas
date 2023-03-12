import tkinter as tk

# Crear ventana principal
root = tk.Tk()
root.title("Lista de tareas pendientes")

# Establecer color de fondo
root.configure(bg="#1a202c")

# Crear marco para lista de tareas
frame = tk.Frame(root)
frame.pack()

# Crear cuadro de entrada de texto
entry = tk.Entry(frame)
entry.pack(side=tk.LEFT)

# Crear botón de agregar tarea


def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)


button = tk.Button(frame, text="Agregar tarea", command=add_task)
button.pack(side=tk.LEFT)


# Enlazar evento Enter a la funcion add_task()
entry.bind("<Return>", lambda event: add_task())


# Crear lista de tareas
listbox = tk.Listbox(root)
listbox.pack()

# Crear botón de eliminar tarea


def delete_task():
    selected_task = listbox.curselection()
    listbox.delete(selected_task)


button = tk.Button(root, text="Eliminar tarea", command=delete_task)
button.pack()

# Ejecutar ventana principal
root.mainloop()
