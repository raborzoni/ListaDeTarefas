import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime

# Funções
def add_task():
    task_text = task_entry.get()
    task_date_str = date_entry.get()
    task_time_str = time_entry.get()
    
    if task_text == "" or task_date_str == "" or task_time_str == "":
        messagebox.showwarning("Aviso", "Por favor, insira a tarefa, a data e a hora")
        return

    try:
        task_datetime_str = f"{task_date_str} {task_time_str}"
        task_datetime = datetime.strptime(task_datetime_str, "%Y-%m-%d %H:%M")
    except ValueError:
        messagebox.showwarning("Aviso", "Formato de data/hora inválido. Use AAAA-MM-DD HH:MM")
        return

    tasks_listbox.insert(tk.END, f"{task_text} (Para: {task_datetime_str})")
    task_entry.delete(0, tk.END)
    task_entry.insert(0, "Escreva a tarefa aqui")
    date_entry.set_date(datetime.now())
    time_entry.delete(0, tk.END)
    time_entry.insert(0, "HHMM")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para deletar")

def mark_completed():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task_text = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(tk.END, f"{task_text} ✔")
    except IndexError:
        messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para marcar como concluída")

def format_time(event):
    time_text = time_entry.get()
    if len(time_text) == 4 and time_text.isdigit():
        formatted_time = f"{time_text[:2]}:{time_text[2:]}"
        time_entry.delete(0, tk.END)
        time_entry.insert(0, formatted_time)

def on_entry_click(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.insert(0, '')
        entry.config(fg="#333")

def on_focusout(event, entry, placeholder):
    if entry.get() == '':
        entry.insert(0, placeholder)
        entry.config(fg="#a6a6a6")

# Configurações da janela principal
root = tk.Tk()
root.title("Lista de Tarefas")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# Configurações dos widgets
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

tasks_listbox = tk.Listbox(
    frame,
    width=50,
    height=10,
    bg="#fff",
    bd=0,
    fg="#333",
    font=("Helvetica", 12),
    selectbackground="#a6a6a6",
    activestyle="none",
)
tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

tasks_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks_listbox.yview)

entry_frame = tk.Frame(root, bg="#f0f0f0")
entry_frame.pack(pady=15)

task_entry = tk.Entry(
    entry_frame,
    width=25,
    bg="#fff",
    bd=0,
    fg="#a6a6a6",
    font=("Helvetica", 12),
)
task_entry.insert(0, "Escreva a tarefa aqui")
task_entry.bind('<FocusIn>', lambda event: on_entry_click(event, task_entry, "Escreva a tarefa aqui"))
task_entry.bind('<FocusOut>', lambda event: on_focusout(event, task_entry, "Escreva a tarefa aqui"))
task_entry.pack(side=tk.LEFT, padx=5)

date_entry = DateEntry(
    entry_frame,
    width=12,
    bg="#fff",
    bd=0,
    fg="#333",
    font=("Helvetica", 12),
    date_pattern="yyyy-mm-dd"
)
date_entry.pack(side=tk.LEFT, padx=5)

time_entry = tk.Entry(
    entry_frame,
    width=6,
    bg="#fff",
    bd=0,
    fg="#a6a6a6",
    font=("Helvetica", 12),
)
time_entry.insert(0, "HHMM")
time_entry.bind('<FocusIn>', lambda event: on_entry_click(event, time_entry, "HHMM"))
time_entry.bind('<FocusOut>', lambda event: on_focusout(event, time_entry, "HHMM"))
time_entry.bind('<KeyRelease>', format_time)
time_entry.pack(side=tk.LEFT, padx=5)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

add_task_button = tk.Button(
    button_frame,
    text="Adicionar Tarefa",
    command=add_task,
    bg="#333",
    fg="#fff",
    font=("Helvetica", 12),
    padx=10,
    pady=5,
    bd=0,
)
add_task_button.pack(side=tk.LEFT, padx=10)

remove_task_button = tk.Button(
    button_frame,
    text="Remover Tarefa",
    command=delete_task,
    bg="#333",
    fg="#fff",
    font=("Helvetica", 12),
    padx=10,
    pady=5,
    bd=0,
)
remove_task_button.pack(side=tk.LEFT, padx=10)

complete_task_button = tk.Button(
    button_frame,
    text="Concluir Tarefa",
    command=mark_completed,
    bg="#333",
    fg="#fff",
    font=("Helvetica", 12),
    padx=10,
    pady=5,
    bd=0,
)
complete_task_button.pack(side=tk.LEFT, padx=10)

# Iniciar a aplicação
root.mainloop()
