import tkinter as tk

def button_click(number):
    current = entry_field.get()
    entry_field.delete(0, tk.END)
    entry_field.insert(tk.END, current + str(number))

def button_clear():
    entry_field.delete(0, tk.END)

def button_add():
    first_number = entry_field.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = float(first_number)
    entry_field.delete(0, tk.END)

def button_subtract():
    first_number = entry_field.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = float(first_number)
    entry_field.delete(0, tk.END)

def button_multiply():
    first_number = entry_field.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = float(first_number)
    entry_field.delete(0, tk.END)

def button_divide():
    first_number = entry_field.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = float(first_number)
    entry_field.delete(0, tk.END)

def button_equal():
    second_number = entry_field.get()
    entry_field.delete(0, tk.END)

    if math_operation == "addition":
        entry_field.insert(tk.END, f_num + float(second_number))
    elif math_operation == "subtraction":
        entry_field.insert(tk.END, f_num - float(second_number))
    elif math_operation == "multiplication":
        entry_field.insert(tk.END, f_num * float(second_number))
    elif math_operation == "division":
        try:
            entry_field.insert(tk.END, f_num / float(second_number))
        except ZeroDivisionError:
            entry_field.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry field to display the numbers and results
entry_field = tk.Entry(window, width=35, borderwidth=5)
entry_field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Create number buttons
button_1 = tk.Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))

# Create operation buttons