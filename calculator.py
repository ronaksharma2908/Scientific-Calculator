import tkinter as tk
import math

# Global flags and memory
use_degrees = True
memory_value = 0.0
history = []
dark_mode = True

# Function to evaluate expressions safely
def calculate():
    global use_degrees, history
    try:
        expression = entry.get()
        expression = expression.replace("^", "**")
        expression = expression.replace("ln(", "log(")

        def sin(x): return math.sin(math.radians(x)) if use_degrees else math.sin(x)
        def cos(x): return math.cos(math.radians(x)) if use_degrees else math.cos(x)
        def tan(x): return math.tan(math.radians(x)) if use_degrees else math.tan(x)

        result = eval(expression, {"__builtins__": None}, {
            "sqrt": math.sqrt,
            "log": math.log10,
            "log": math.log,
            "sin": sin,
            "cos": cos,
            "tan": tan,
            "exp": math.exp,
            "pow": math.pow,
            "factorial": math.factorial,
            "pi": math.pi,
            "e": math.e
        })
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        history.append(f"{expression} = {result}")
        update_history()
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def insert_text(text): entry.insert(tk.END, text)
def clear(): entry.delete(0, tk.END)

def toggle_mode():
    global use_degrees
    use_degrees = not use_degrees
    mode_label.config(text="Mode: Degrees" if use_degrees else "Mode: Radians")

# Memory functions
def memory_add():
    global memory_value
    try: memory_value += float(entry.get())
    except: pass

def memory_subtract():
    global memory_value
    try: memory_value -= float(entry.get())
    except: pass

def memory_recall(): entry.insert(tk.END, str(memory_value))
def memory_clear(): 
    global memory_value
    memory_value = 0.0

# History functions
def update_history():
    history_text.delete(1.0, tk.END)
    for item in history[-10:]:
        history_text.insert(tk.END, item + "\n")

def clear_history():
    global history
    history = []
    history_text.delete(1.0, tk.END)
    status_label.config(text="History cleared!")

# Copy result
def copy_result():
    result = entry.get()
    root.clipboard_clear()
    root.clipboard_append(result)
    root.update()
    status_label.config(text="Result copied to clipboard!")

# Theme toggle
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.configure(bg="#2c3e50")
        entry.configure(bg="#ecf0f1", fg="#2c3e50")
        mode_label.configure(bg="#2c3e50", fg="white")
        status_label.configure(bg="#2c3e50", fg="lightgreen")
        history_label.configure(bg="#2c3e50", fg="white")
        history_text.configure(bg="#ecf0f1", fg="#2c3e50")
    else:
        root.configure(bg="white")
        entry.configure(bg="white", fg="black")
        mode_label.configure(bg="white", fg="black")
        status_label.configure(bg="white", fg="green")
        history_label.configure(bg="white", fg="black")
        history_text.configure(bg="white", fg="black")

# Main window
root = tk.Tk()
root.title("Advanced Scientific Calculator")
root.configure(bg="#2c3e50")

entry = tk.Entry(root, width=30, font=("Arial", 18), borderwidth=5, relief="ridge", bg="#ecf0f1", fg="#2c3e50")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

mode_label = tk.Label(root, text="Mode: Degrees", font=("Arial", 12), bg="#2c3e50", fg="white")
mode_label.grid(row=1, column=0, columnspan=5)

status_label = tk.Label(root, text="", font=("Arial", 10), bg="#2c3e50", fg="lightgreen")
status_label.grid(row=10, column=0, columnspan=5)

buttons = [
    ("7",2,0), ("8",2,1), ("9",2,2), ("/",2,3), ("sqrt(",2,4),
    ("4",3,0), ("5",3,1), ("6",3,2), ("*",3,3), ("^",3,4),
    ("1",4,0), ("2",4,1), ("3",4,2), ("-",4,3), ("log(",4,4),
    ("0",5,0), (".",5,1), ("(",5,2), (")",5,3), ("+",5,4),
    ("sin(",6,0), ("cos(",6,1), ("tan(",6,2), ("ln(",6,3), ("=",6,4),
    ("exp(",7,0), ("pow(",7,1), ("factorial(",7,2), ("pi",7,3), ("e",7,4),
]

for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=6, height=2, command=calculate, bg="#27ae60", fg="white").grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=6, height=2, command=lambda t=text: insert_text(t), bg="#34495e", fg="white").grid(row=row, column=col, padx=5, pady=5)

tk.Button(root, text="C", width=6, height=2, command=clear, bg="#e74c3c", fg="white").grid(row=8, column=0, padx=5, pady=5)
tk.Button(root, text="Toggle Mode", width=12, height=2, command=toggle_mode, bg="#2980b9", fg="white").grid(row=8, column=1, columnspan=2, padx=5, pady=5)
tk.Button(root, text="Copy Result", width=12, height=2, command=copy_result, bg="#f39c12", fg="white").grid(row=8, column=3, columnspan=2, padx=5, pady=5)

tk.Button(root, text="M+", width=6, height=2, command=memory_add, bg="#8e44ad", fg="white").grid(row=9, column=0, padx=5, pady=5)
tk.Button(root, text="M-", width=6, height=2, command=memory_subtract, bg="#8e44ad", fg="white").grid(row=9, column=1, padx=5, pady=5)
tk.Button(root, text="MR", width=6, height=2, command=memory_recall, bg="#8e44ad", fg="white").grid(row=9, column=2, padx=5, pady=5)
tk.Button(root, text="MC", width=6, height=2, command=memory_clear, bg="#8e44ad", fg="white").grid(row=9, column=3, padx=5, pady=5)

history_label = tk.Label(root, text="History (last 10):", font=("Arial", 12), bg="#2c3e50", fg="white")
history_label.grid(row=2, column=5, padx=10, pady=5)

history_text = tk.Text(root, width=25, height=20, font=("Arial", 10), bg="#ecf0f1", fg="#2c3e50")
history_text.grid(row=3, column=5, rowspan=7, padx=10, pady=5)

tk.Button(root, text="Clear History", width=12, height=2, command=clear_history, bg="#c0392b", fg="white").grid(row=11, column=5, padx=10, pady=5)
tk.Button(root, text="Toggle Theme", width=12, height=2, command=toggle_theme, bg="#16a085", fg="white").grid(row=12, column=5, padx=10, pady=5)

root.mainloop()
