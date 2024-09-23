import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("To-Do App")

        # Create widgets with a different background color for the entry field
        self.task_entry = tk.Entry(self.window, bg='lightyellow', fg='black')  # Set text color here
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self.window, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_list = tk.Listbox(self.window)
        self.task_list.pack(fill=tk.BOTH, expand=True, pady=10)

        self.delete_button = tk.Button(self.window, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Bind keyboard events
        self.task_entry.bind('<Return>', lambda event: self.add_task())
        self.task_list.bind('<Delete>', lambda event: self.delete_task())

        # Start the event loop
        self.window.mainloop()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            # Add bullet point to the task
            self.task_list.insert(tk.END, f"• {task}")  # Bullet point added here
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this task?"):
                self.task_list.delete(selected_index[0])
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

if __name__ == "__main__":
    app = ToDoApp()
