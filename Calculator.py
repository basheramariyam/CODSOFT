import tkinter as tk
def click(value):
    display.insert(tk.END, value)
def clear():
    display.delete(0, tk.END)
def calculate():
    try:
        result = eval(display.get())
        clear()
        display.insert(0, result)
    except:
        clear()
        display.insert(0, "Error")
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
display = tk.Entry(root, font=("Arial", 20), justify="right")
display.pack(fill="x", padx=10, pady=10)

frame = tk.Frame(root)
frame.pack()
buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    'C','0','=','+'
]
row = col = 0
for b in buttons:
    if b == "C":
        cmd = clear
    elif b == "=":
        cmd = calculate
    else:
        cmd = lambda x=b: click(x)

    tk.Button(frame, text=b, width=5, height=2,
              font=("Arial", 18),
              command=cmd).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col == 4:
        col = 0
        row += 1
root.mainloop()
