Original code 
import tkinter as tk

def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0 / 9.0

def celsius_to_fahrenheit(c):
    return (c * 9.0 / 5.0) + 32

def convert_to_celsius():
    try:
        fahrenheit_value = float(fahrenheit_entry.get())
        celsius_value = fahrenheit_to_celsius(fahrenheit_value)
        celsius_entry.delete(0, tk.END)
        celsius_entry.insert(0, f"{celsius_value:.2f}")
    except ValueError:
        celsius_entry.delete(0, tk.END)
        celsius_entry.insert(0, "Error")

def convert_to_fahrenheit():
    try:
        celsius_value = float(celsius_entry.get())
        fahrenheit_value = celsius_to_fahrenheit(celsius_value)
        fahrenheit_entry.delete(0, tk.END)
        fahrenheit_entry.insert(0, f"{fahrenheit_value:.2f}")
    except ValueError:
        fahrenheit_entry.delete(0, tk.END)
        fahrenheit_entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create labels
fahrenheit_label = tk.Label(root, text="Fahrenheit:")
celsius_label = tk.Label(root, text="Celsius:")

# Create entry fields
fahrenheit_entry = tk.Entry(root)
celsius_entry = tk.Entry(root)

# Initialize entry fields with default values
fahrenheit_entry.insert(0, "32.0")
celsius_entry.insert(0, "0.0")

# Create buttons
to_celsius_button = tk.Button(root, text=">>>>", command=convert_to_celsius)
to_fahrenheit_button = tk.Button(root, text="<<<<", command=convert_to_fahrenheit)

# Arrange components in a grid
fahrenheit_label.grid(row=0, column=0)
celsius_label.grid(row=0, column=1)
fahrenheit_entry.grid(row=1, column=0)
celsius_entry.grid(row=1, column=1)
to_celsius_button.grid(row=2, column=0)
to_fahrenheit_button.grid(row=2, column=1)

# Start the GUI event loop
root.mainloop()





Enhanced code showing whether it is above or below freezing point 
import tkinter as tk

def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0 / 9.0

def celsius_to_fahrenheit(c):
    return (c * 9.0 / 5.0) + 32

def convert_to_celsius():
    try:
        fahrenheit_value = float(fahrenheit_entry.get())
        celsius_value = fahrenheit_to_celsius(fahrenheit_value)
        celsius_entry.delete(0, tk.END)
        celsius_entry.insert(0, f"{celsius_value:.2f}")
        check_freezing(celsius_value, 'Celsius')
    except ValueError:
        celsius_entry.delete(0, tk.END)
        celsius_entry.insert(0, "Error")
        freezing_label.config(text="")

def convert_to_fahrenheit():
    try:
        celsius_value = float(celsius_entry.get())
        fahrenheit_value = celsius_to_fahrenheit(celsius_value)
        fahrenheit_entry.delete(0, tk.END)
        fahrenheit_entry.insert(0, f"{fahrenheit_value:.2f}")
        check_freezing(fahrenheit_value, 'Fahrenheit')
    except ValueError:
        fahrenheit_entry.delete(0, tk.END)
        fahrenheit_entry.insert(0, "Error")
        freezing_label.config(text="")

def check_freezing(value, scale):
    if scale == 'Celsius':
        if value < 0:
            freezing_label.config(text="Below Freezing")
        else:
            freezing_label.config(text="Above Freezing")
    elif scale == 'Fahrenheit':
        if value < 32:
            freezing_label.config(text="Below Freezing")
        else:
            freezing_label.config(text="Above Freezing")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create labels
fahrenheit_label = tk.Label(root, text="Fahrenheit:")
celsius_label = tk.Label(root, text="Celsius:")
freezing_label = tk.Label(root, text="", font=('Helvetica', 10, 'bold'))

# Create entry fields
fahrenheit_entry = tk.Entry(root)
celsius_entry = tk.Entry(root)

# Initialize entry fields with default values
fahrenheit_entry.insert(0, "32.0")
celsius_entry.insert(0, "0.0")

# Create buttons
to_celsius_button = tk.Button(root, text=">>>>", command=convert_to_celsius)
to_fahrenheit_button = tk.Button(root, text="<<<<", command=convert_to_fahrenheit)

# Arrange components in a grid
fahrenheit_label.grid(row=0, column=0)
celsius_label.grid(row=0, column=1)
fahrenheit_entry.grid(row=1, column=0)
celsius_entry.grid(row=1, column=1)
to_celsius_button.grid(row=2, column=0)
to_fahrenheit_button.grid(row=2, column=1)
freezing_label.grid(row=3, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()
