import tkinter as tk
from time import strftime

def update_time():
    # Get the current time
    current_time = strftime('%H:%M:%S %p')
    
    # Update the label text
    label.config(text=current_time)
    
    # Call the update_time function after 1000ms (1 second)
    label.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title("Simple Clock")

# Create a label to display the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')

# Place the label in the center of the window
label.pack(anchor='center')

# Call the update_time function to initialize the clock
update_time()

# Run the Tkinter event loop
root.mainloop()
