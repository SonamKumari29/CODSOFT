import tkinter as tk

def evaluate_expression():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_click(char):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + char)

def clear_display():
    entry.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget to display the input and result
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for digits and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, command=evaluate_expression).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, command=lambda char=button: button_click(char)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create a clear button
tk.Button(root, text="Clear", padx=20, pady=20, command=clear_display).grid(row=row_val, column=col_val)

root.mainloop()
