from tkinter import *
from tkinter import messagebox
tasks = []
def add_task():
    task = task_entry.get()
    if task == "":
        messagebox.showinfo("Error", "Field is empty.")
    else:
        tasks.append(task)
        listbox.insert(END, task)
        task_entry.delete(0, END)
def remove_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        tasks.pop(index)
    except:
        messagebox.showinfo("Error", "Select a task to remove.")
def delete_all():
    listbox.delete(0, END)
    tasks.clear()
root = Tk()
root.title("TO-DO LIST")
root.geometry("450x400")
root.config(bg="#add8e6")
Label(root, text="TO-DO-LIST Items", font=("Arial", 16), 
bg="#add8e6").pack(pady=10)
task_entry = Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)
button_frame = Frame(root, bg="#add8e6")
button_frame.pack()
Button(button_frame, text="Add", width=10, command=add_task).grid(row=0, column=0, padx=5)
Button(button_frame, text="Remove", width=10, command=remove_task).grid(row=0, column=1, padx=5)
Button(button_frame, text="Delete All", width=10, command=delete_all).grid(row=0, column=2, padx=5)
listbox = Listbox(root, width=50, height=10, font=("Arial", 12))
listbox.pack(pady=10)
Button(root, text="Exit / Close", width=15, command=root.destroy).pack(pady=5)
root.mainloop()