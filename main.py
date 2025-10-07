# main.py
import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

DATA_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

class ToDoApp:
    def __init__(self, root):
        self.root = root
        root.title("Lista de tareas")
        root.geometry("400x400")

        # Frame para la lista
        frame = tk.Frame(root)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.listbox = tk.Listbox(frame, selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Entrada y botones
        entry_frame = tk.Frame(root)
        entry_frame.pack(fill=tk.X, padx=10, pady=(0,10))

        self.entry = tk.Entry(entry_frame)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.entry.bind("<Return>", lambda e: self.add_task())

        add_btn = tk.Button(entry_frame, text="Agregar", command=self.add_task)
        add_btn.pack(side=tk.LEFT, padx=(5,0))

        del_btn = tk.Button(root, text="Eliminar seleccionada", command=self.delete_task)
        del_btn.pack(fill=tk.X, padx=10, pady=(0,5))

        save_btn = tk.Button(root, text="Guardar", command=self.save)
        save_btn.pack(fill=tk.X, padx=10)

        # Cargar tareas
        self.tasks = load_tasks()
        for t in self.tasks:
            self.listbox.insert(tk.END, t)

    def add_task(self):
        text = self.entry.get().strip()
        if not text:
            messagebox.showinfo("Info", "Escribe algo primero.")
            return
        self.listbox.insert(tk.END, text)
        self.tasks.append(text)
        self.entry.delete(0, tk.END)

    def delete_task(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo("Info", "Selecciona una tarea para eliminar.")
            return
        index = sel[0]
        self.listbox.delete(index)
        del self.tasks[index]

    def save(self):
        save_tasks(self.tasks)
        messagebox.showinfo("Guardado", "Tareas guardadas en tasks.json")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
