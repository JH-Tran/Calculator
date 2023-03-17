import tkinter as tk
from tkinter import DISABLED, NORMAL, PhotoImage
from math import *

calculation = ""

def add_to_calculation(symbol):
    text_result["state"] = NORMAL
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
    text_result["state"] = DISABLED

def evaluate_calculation():
    global calculation
    try:
        text_result["state"] = NORMAL
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
        text_result["state"] = DISABLED
    except:
        clear_field()
        text_result["state"] = NORMAL
        text_result.insert(1.0, "Error")
        text_result["state"] = DISABLED
        pass

def clear_field():
    text_result["state"] = NORMAL
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
    text_result["state"] = DISABLED
    pass

def clear_calculation():
    pass

root = tk.Tk()
root.configure(bg='#3a484a')
root.geometry("375x275")

# Change the title and image of the application
root.title("Calculator")
img = PhotoImage(file="calculator.png")
root.iconphoto(False,img)

# Create display of calculator
text_result = tk.Text(root, height=2, width=20, font=("Ariel", 24), bg='#2fc8b4', fg='white')
text_result.grid(columnspan=6)
text_result["state"] = DISABLED

# Calculator buttons with their function correlated to the name
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Ariel", 14), bg='#D2D2D3', fg='#555555')
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Ariel", 14), bg='#D2D2D3', fg='#555555')
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Ariel", 14), bg='#D2D2D3', fg='#555555')
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Ariel", 14), bg='#D2D2D3', fg='#555555')
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Ariel", 14), bg='#D2D2D3', fg='#555555')
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Ariel", 14), bg='#D2D2D3', fg='#555555')
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Ariel", 14), bg='#D2D2D3', fg='#555555')
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Ariel", 14), bg='#D2D2D3', fg='#555555')
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Ariel", 14), bg='#D2D2D3', fg='#555555')
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Ariel", 14), bg='#D2D2D3', fg='#555555')
btn_0.grid(row=5, column=2)
# Calculator operations
# Yellow section
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Ariel", 14), bg='#ffe380', fg='#555555')
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Ariel", 14), bg='#ffe380', fg='#555555')
btn_minus.grid(row=2, column=5)
btn_mul = tk.Button(root, text="×", command=lambda: add_to_calculation("*"), width=5, font=("Ariel", 14), bg='#ffe380', fg='#555555')
btn_mul.grid(row=3, column=4)
btn_div = tk.Button(root, text="÷", command=lambda: add_to_calculation("/"), width=5, font=("Ariel", 14), bg='#ffe380', fg='#555555')
btn_div.grid(row=3, column=5)

# Green section
btn_sqrt = tk.Button(root, text="sqrt", command=lambda: add_to_calculation("sqrt("), width=5, font=("Ariel", 14), bg='#2fc8b4', fg='white')
btn_sqrt.grid(row=4, column=4)
btn_sqrt = tk.Button(root, text="pow", command=lambda: add_to_calculation("pow("), width=5, font=("Ariel", 14), bg='#2fc8b4', fg='white')
btn_sqrt.grid(row=4, column=5)
btn_sqrt = tk.Button(root, text="log", command=lambda: add_to_calculation("log("), width=5, font=("Ariel", 14), bg='#2fc8b4', fg='white')
btn_sqrt.grid(row=5, column=4)
btn_sqrt = tk.Button(root, text="π", command=lambda: add_to_calculation("pi"), width=5, font=("Ariel", 14), bg='#2fc8b4', fg='white')
btn_sqrt.grid(row=5, column=5)

# Grey
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Ariel", 14), bg='#D2D2D2', fg='#555555')
btn_open.grid(row=5, column=1)
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Ariel", 14), bg='#D2D2D2', fg='#555555')
btn_close.grid(row=5, column=3)
btn_close = tk.Button(root, text=",", command=lambda: add_to_calculation(","), width=5, font=("Ariel", 14), bg='#D2D2D2', fg='#555555')
btn_close.grid(row=6, column=3)
# Clear text field
btn_clear = tk.Button(root, text="c", command=clear_field, width=12, font=("Ariel", 14), bg='#dc5a64', fg='white')
btn_clear.grid(row=6, column=1, columnspan=2)
# Evaluate the text field calculation
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=12, font=("Ariel", 14), bg='#dc5a64', fg='white')
btn_equals.grid(row=6, column=4, columnspan=2)

root.mainloop()
