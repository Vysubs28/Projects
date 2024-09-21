import tkinter as tk

class ToDoApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("To-Do App")

        # Create widgets
        self.task_entry = tk.Entry(self.window)
        # Pack the entry field at the top
        self.task_entry.pack()

        self.add_button = tk.Button(self.window, text="Add Task", command=self.add_task)
        # Pack the add button below the entry field
        self.add_button.pack()

        self.task_list = tk.Listbox(self.window)
        # Expand the listbox to fill available space
        self.task_list.pack(fill=tk.BOTH, expand=True)

        self.delete_button = tk.Button(self.window, text="Delete Task", command=self.delete_task)
        # Pack the delete button below the listbox
        self.delete_button.pack()

        # Start the event loop
        self.window.mainloop()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            self.task_list.delete(selected_index[0])

if __name__ == "__main__":
    app = ToDoApp()