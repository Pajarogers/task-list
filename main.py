import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        # Load the background image
        background_image = Image.open("18.jpg")  
        self.background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(root, image=self.background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a list to store tasks
        self.tasks = []

        # Create GUI elements
        self.task_label = tk.Label(root, text="Task:", bg="lightgray")
        self.task_label.pack()
        self.task_entry = tk.Entry(root)
        self.task_entry.pack()
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="lightgreen")
        self.add_button.pack()
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.task_listbox.pack()
        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task, bg="salmon")
        self.complete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks.pop(index)
            self.task_listbox.delete(index)
            messagebox.showinfo("Task Completed", f"Completed: {task}")
        else:
            messagebox.showwarning("Warning", "Select a task to complete.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")  # Set the initial size of the window
    app = TodoApp(root)
    root.mainloop()
