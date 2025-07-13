import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            result = "Invalid Operation"
        
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed!")

def clear_inputs():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_result.config(text="Result: ")

window = tk.Tk()
window.title("Calculator")
window.geometry("400x400")
window.resizable(False, False)
window.configure(bg="#FFFFFF")

title_label = tk.Label(window, text="CALCULATOR", font=("Arial", 25, "bold"), bg="#FFFFFF", fg="#333")
title_label.pack(pady=10)

frame_inputs = tk.Frame(window, bg="#ffffff")
frame_inputs.pack(pady=10)

label_num1 = tk.Label(frame_inputs, text="Number 1:", font=("Arial", 14), bg="#ffffff")
label_num1.grid(row=0, column=0, padx=10, pady=5)

entry_num1 = tk.Entry(frame_inputs, font=("Arial", 14), width=10)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(frame_inputs, text="Number 2:", font=("Arial", 14), bg="#fffdfd")
label_num2.grid(row=1, column=0, padx=10, pady=5)

entry_num2 = tk.Entry(frame_inputs, font=("Arial", 14), width=10)
entry_num2.grid(row=1, column=1, padx=10, pady=5)
operation_var = tk.StringVar(value="Addition")
operations = ["Addition", "Subtraction", "Multiplication", "Division"]

operation_menu = tk.OptionMenu(window, operation_var, *operations)
operation_menu.config(font=("Arial", 14), bg="#ffffff")
operation_menu.pack(pady=10)

frame_buttons = tk.Frame(window, bg="#fffdfd")
frame_buttons.pack(pady=10)

btn_calculate = tk.Button(frame_buttons, text="Calculate", font=("Arial", 14), bg="#14C61A", fg="white", command=calculate)
btn_calculate.grid(row=0, column=0, padx=10)

btn_clear = tk.Button(frame_buttons, text="Clear", font=("Arial", 14), bg="#ec2416", fg="white", command=clear_inputs)
btn_clear.grid(row=0, column=1, padx=10)

label_result = tk.Label(window, text="Result: ", font=("Arial", 16, "bold"), bg="#ffffff", fg="#333")
label_result.pack(pady=20)

window.mainloop()
