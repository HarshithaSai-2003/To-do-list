import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            task_list.insert(tk.END, *file.read().splitlines())

# Save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        file.writelines(f"{task}\n" for task in task_list.get(0, tk.END))

# Add a task
def add_task():
    task = task_entry.get().strip()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Oops!", "Please enter a task!")

# Delete a task
def delete_task():
    try:
        task_list.delete(task_list.curselection()[0])
        save_tasks() 
    except IndexError:
        messagebox.showwarning("Oops!", "Select a task to delete!")

# Set up the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Add Task", command=add_task, width=15, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame, text="Delete Task", command=delete_task, width=15, bg="#F44336", fg="white").grid(row=0, column=1, padx=5, pady=5)

task_list = tk.Listbox(root, width=50, height=15)
task_list.pack(pady=10)

load_tasks()
root.mainloop()
