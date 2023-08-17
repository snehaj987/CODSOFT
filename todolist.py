import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" My To-Do List Application")

        self.tasks = []

        self.entry_task = tk.Entry(root, width=30)
        self.entry_task.pack(padx=10, pady=10)

        self.btn_add_task = tk.Button(root, text="Add Task", command=self.add_task)
        self.btn_add_task.pack()

        self.task_listbox = tk.Listbox(root, width=40, height=10)
        self.task_listbox.pack()

        self.btn_complete_task = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.btn_complete_task.pack()

        self.btn_delete_task = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.btn_delete_task.pack()

        self.refresh_listbox()

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.entry_task.delete(0, tk.END)
            self.refresh_listbox()

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks[selected_index[0]]["completed"] = True
            self.refresh_listbox()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.refresh_listbox()

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task_data in self.tasks:
            task_text = "[X] " if task_data["completed"] else "[ ] "
            task_text += task_data["task"]
            self.task_listbox.insert(tk.END, task_text)

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()
