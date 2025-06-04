import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 20", justify="right", bd=10, relief=tk.RIDGE)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Buttons
btns_frame = tk.Frame(root)
btns_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for row in buttons:
    row_frame = tk.Frame(btns_frame)
    row_frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(row_frame, text=btn_text, font="Arial 18", relief=tk.RAISED, bd=5)
        btn.pack(side=tk.LEFT, expand=True, fill="both")
        btn.bind("<Button-1>", click)

root.mainloop()

