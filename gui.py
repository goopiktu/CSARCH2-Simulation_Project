from tkinter import *
import csarch2 as m  # Ensure this matches your actual module

root = Tk()
root.title("IEEE-754 Binary-128 Floating Point Converter")

# Main Frame for better organization and padding
main_frame = Frame(root, padx=20, pady=20)
main_frame.pack(padx=20, pady=20)

# Frame for the title
title_frame = Frame(main_frame)
title_frame.grid(row=0, column=0, columnspan=4, sticky="ew")
title_label = Label(title_frame, text="IEEE-754 Binary-128 Floating Point Converter", font=("Helvetica", 16))
title_label.pack()

# Frame for input
input_frame = Frame(main_frame)
input_frame.grid(row=1, column=0, columnspan=4, sticky="ew")
e = Text(input_frame, width=48, height=4, font=("Helvetica", 12))
e.pack(padx=5, pady=5)

# Frame for buttons
button_frame = Frame(main_frame)
button_frame.grid(row=2, column=0, columnspan=4)

# Definition and placement of buttons, adjusted for wider buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("Clear", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("^", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("-", 4, 3),
    ("=", 5, 0, 4)  # Equal button spans all columns
]

for text, row, col, *span in buttons:
    action = lambda x=text: button_click(x) if x.isdigit() or x == "." else sign(x) if x in "+-*/^" else clear() if x == "Clear" else equal()
    btn = Button(button_frame, width=10, text=text, command=action, font=("Helvetica", 12))
    if span:
        btn.grid(row=row, column=col, sticky="nsew", columnspan=span[0], padx=5, pady=5)
    else:
        btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Make the grid columns and rows expandable
for x in range(4):
    button_frame.columnconfigure(x, weight=1)
for y in range(5):
    button_frame.rowconfigure(y, weight=1)

# Functions (ensure these match your actual module's functionality)
def button_click(number):
    e.insert(END, str(number))

def sign(sign):
    e.insert(END, str(sign))

def clear():
    e.delete(1.0, END)

def equal():
    current = e.get(1.0, END)
    f = m.main(str(current))  # Ensure this call matches your module's functionality
    formatted_result = '\n'.join([f"{key}: {value}" for key, value in f.items()])
    e.delete(1.0, END)
    e.insert(1.0, formatted_result)

root.mainloop()