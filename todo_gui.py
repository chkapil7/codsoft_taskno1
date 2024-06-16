import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.todo_list = []
        
        self.root = root
        self.root.title("To-Do List Application")
        
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=50)
        self.task_entry.pack(side=tk.LEFT, padx=5)
        
        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)
        
        self.tasks_listbox = tk.Listbox(root, width=50, height=10)
        self.tasks_listbox.pack(pady=10)
        
        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(pady=5)
        
        self.update_tasks_listbox()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.append({'task': task, 'completed': False})
            self.task_entry.delete(0, tk.END)
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def complete_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.todo_list[index]['completed'] = True
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to complete.")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.todo_list):
            status = 'Done' if task['completed'] else 'Not Done'
            self.tasks_listbox.insert(tk.END, f"{idx + 1}. {task['task']} - {status}")

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
