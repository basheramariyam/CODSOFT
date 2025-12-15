import tkinter as tk
from tkinter import messagebox
contacts = {}
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()
    if name == "" or phone == "":
        messagebox.showwarning("Input Error", "Name and Phone are required")
        return
    contacts[name] = (phone, email, address)
    update_listbox()
    clear_fields()
def update_listbox():
    listbox.delete(0, tk.END)
    for name in contacts:
        listbox.insert(tk.END, name)
def select_contact(event):
    selected = listbox.curselection()
    if selected:
        name = listbox.get(selected)
        phone, email, address = contacts[name]
        entry_name.delete(0, tk.END)
        entry_name.insert(0, name)
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, phone)
        entry_email.delete(0, tk.END)
        entry_email.insert(0, email)
        entry_address.delete(0, tk.END)
        entry_address.insert(0, address)
def update_contact():
    name = entry_name.get()
    if name in contacts:
        contacts[name] = (
            entry_phone.get(),
            entry_email.get(),
            entry_address.get()
        )
        update_listbox()
        clear_fields()
    else:
        messagebox.showerror("Error", "Contact not found")
def delete_contact():
    name = entry_name.get()
    if name in contacts:
        del contacts[name]
        update_listbox()
        clear_fields()
    else:
        messagebox.showerror("Error", "Contact not found")
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x500")
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()
tk.Label(root, text="Phone").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()
tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root)
entry_email.pack()
tk.Label(root, text="Address").pack()
entry_address = tk.Entry(root)
entry_address.pack()
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)
listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)
listbox.bind("<<ListboxSelect>>", select_contact)
root.mainloop()
