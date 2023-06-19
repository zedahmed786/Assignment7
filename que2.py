import calendar
import tkinter as tk
from tkinter import messagebox

def show_calendar():
    year = int(year_entry.get())
    
    try:
        cal = calendar.calendar(year)
        calendar_text.config(state=tk.NORMAL)
        calendar_text.delete('1.0', tk.END)
        calendar_text.insert(tk.END, cal)
        calendar_text.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Invalid year!")

# Create the main window
window = tk.Tk()
window.title("Calendar Application")

# Create a label and entry field for the year
year_label = tk.Label(window, text="Enter a year:")
year_label.pack()
year_entry = tk.Entry(window)
year_entry.pack()

# Create a button to show the calendar
show_button = tk.Button(window, text="Show Calendar", command=show_calendar)
show_button.pack()

# Create a text widget to display the calendar
calendar_text = tk.Text(window, height=20, width=50, state=tk.DISABLED)
calendar_text.pack()

# Start the main event loop
window.mainloop()