from tkinter import *
import re

#Start of GUI
root = Tk()
root.title("IEEE-754 Binary-128 Floating Point Converter")

# Main Frame for better organization and padding
main_frame = Frame(root, padx=20, pady=20)
main_frame.pack(padx=20, pady=20)

def update_buttons():
    for widget in button_frame.winfo_children():
        widget.destroy()

    if mode.get() == "decimal":
        for text, row, col in decimal_buttons:
            action = lambda x=text: button_click(x)
            btn = Button(button_frame, width=10, text=text, command=action, font=("Helvetica", 12))
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    else:
        for text, row, col in binary_buttons:
            action = lambda x=text: button_click(x)
            btn = Button(button_frame, width=10, text=text, command=action, font=("Helvetica", 12))
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Frame for the title
title_frame = Frame(main_frame)
title_frame.grid(row=0, column=0, columnspan=4, sticky="ew")
title_label = Label(title_frame, text="IEEE-754 Binary-128 Floating Point Converter", font=("Helvetica", 16))
title_label.pack()

# Frame for input mode selection
mode_frame = Frame(main_frame)
mode_frame.grid(row=1, column=0, columnspan=4, sticky="ew")
mode = StringVar(value="decimal")
decimal_button = Radiobutton(mode_frame, text="Decimal Input", variable=mode, value="decimal", command=update_buttons)
decimal_button.pack(side=LEFT)
binary_button = Radiobutton(mode_frame, text="Binary Input", variable=mode, value="binary", command=update_buttons)
binary_button.pack(side=LEFT)

# Frame for input
input_frame = Frame(main_frame)
input_frame.grid(row=2, column=0, columnspan=4, sticky="ew")
input_label = Label(input_frame, text="Input Window", font=("Helvetica", 12))
input_label.pack()
e = Text(input_frame, width=128, height=4, font=("Helvetica", 12), state="disabled")
e.pack(padx=5, pady=5)

# Frame for output
output_frame = Frame(main_frame)
output_frame.grid(row=3, column=0, columnspan=4, sticky="ew")
output_label = Label(output_frame, text="Output Window", font=("Helvetica", 12))
output_label.pack()
output_text = Text(output_frame, width=128, height=8, font=("Helvetica", 12), state="disabled")
output_text.pack(padx=5, pady=5)

# Frame for buttons
button_frame = Frame(main_frame)
button_frame.grid(row=4, column=0, columnspan=4)

# Definition and placement of buttons
decimal_buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("Clear", 1, 3), ("Backspace", 1, 4),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("^", 2, 3), ("*", 2, 4),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2)
]

binary_buttons = [
    ("1", 1, 0), ("0", 1, 1), ("Clear", 1, 2), ("Backspace", 1, 3),
    ("^", 2, 0), ("-", 2, 1), ("*2", 2, 2), (".", 2, 3),
    ("=", 3, 0)
]

# Make the grid columns and rows expandable
for x in range(5):
    button_frame.columnconfigure(x, weight=1)
for y in range(4):
    button_frame.rowconfigure(y, weight=1)

# Functions
def button_click(text):
    if text == "Clear":
        clear()
    elif text == "Backspace":
        backspace()
    elif text == "=":
        equal()
    else:
        e.configure(state="normal")
        e.insert(END, str(text))
        e.configure(state="disabled")

def clear():
    e.configure(state="normal")
    e.delete(1.0, END)
    e.configure(state="disabled")
    output_text.configure(state="normal")
    output_text.delete(1.0, END)
    output_text.configure(state="disabled")

def backspace():
    e.configure(state="normal")
    current = e.get(1.0, END)
    e.delete(1.0, END)
    e.insert(1.0, current[:-2])
    e.configure(state="disabled")

def equal():
    current = e.get(1.0, END).strip()
    if mode.get() == "decimal":
        current = decimal_to_binary(current)
    else:
        current = process_binary_input(current)
    try:
        f = main(str(current))
        formatted_result = '\n'.join([f"{key}: {value}" for key, value in f.items()])
        output_text.configure(state="normal")
        output_text.delete(1.0, END)
        output_text.insert(1.0, formatted_result)
        output_text.configure(state="disabled")
    except Exception as ex:
        output_text.configure(state="normal")
        output_text.delete(1.0, END)
        output_text.insert(1.0, f"Error: {str(ex)}")
        output_text.configure(state="disabled")
    
#End of GUI

# IEEE-754 Binary-128 Floating Point Converter Code
def sign(number):
    if number[0] == "-":
        return 1
    else:
        return 0

def exponent(exponent):
    e = exponent + 16383
    e = bin(e).replace("b","").replace("0","",1)
    return e

def fraction(fraction):
    frac = fraction.ljust(112, "0")
    return frac

def normalizated_form_check(complete_form):
    if ((len(complete_form[0]) > 1 and complete_form[0][0] != "-") or (complete_form[0][0] == "-" and len(complete_form[0]) > 2 ) or complete_form[0].find("1") == -1):
        return False
    return True

def normalize_form(complete_form):
    if len(complete_form) < 7:
        complete_form.append("0")

    if (complete_form[0].find("1") == -1): # if left side of the dot is only 0s
        first_one = complete_form[2].find("1")
        count = len(complete_form[2]) - first_one
        for i in range(count):
            first_char = complete_form[2][0]
            complete_form[2] = complete_form[2][1:]
            complete_form[6] = str(int(complete_form[6]) - 1)
            complete_form[0] = complete_form[0] + first_char
        complete_form[0] = complete_form[0][0] + complete_form[0][1:].lstrip("0") if complete_form[0][0] == "-" else complete_form[0].lstrip("0")

    else: #if there is 1 in the left side of the dot
        ind = complete_form[0].find("1") + 1
        count = len(complete_form[0]) - ind
        for i in range(count):
            last_char = complete_form[0][-1]
            complete_form[0] = complete_form[0][:-1]
            complete_form[2] = last_char + complete_form[2]
            complete_form[6] = str(int(complete_form[6]) + 1)
        
        complete_form[0] = complete_form[0][0] + complete_form[0][1:].lstrip("0") if complete_form[0][0] == "-" else complete_form[0].lstrip("0")
    return complete_form

def decimal_to_binary(decimal_num):
    # Handle different formats of decimal input
    if "*" in decimal_num:
        base, exponent = decimal_num.split("*")
        base = float(base)
        exponent = int(exponent.split("^")[-1])
        decimal_num = base * (10 ** exponent)
    elif "x" in decimal_num:
        base, exponent = decimal_num.split("x")
        base = float(base)
        exponent = int(exponent.split("^")[-1])
        decimal_num = base * (10 ** exponent)
    else:
        decimal_num = float(decimal_num)

    if decimal_num == 0:
        return "0.0*2^0"
    
    sign = "-" if decimal_num < 0 else ""
    decimal_num = abs(decimal_num)
    
    integer_part = int(decimal_num)
    fractional_part = decimal_num - integer_part
    
    integer_binary = bin(integer_part).replace("0b", "")
    
    fractional_binary = ""
    while fractional_part != 0:
        fractional_part *= 2
        if fractional_part >= 1:
            fractional_binary += "1"
            fractional_part -= 1
        else:
            fractional_binary += "0"
    
    exponent = len(integer_binary) - 1
    
    binary_num = f"{sign}{integer_binary}.{fractional_binary}*2^{exponent}"
    return binary_num

def process_binary_input(binary_num):
    # Handle different formats of binary input
    if "*" not in binary_num:
        if "." not in binary_num:
            binary_num += "*2^0"
        else:
            integer_part, fractional_part = binary_num.split(".")
            exponent = len(integer_part) - 1
            binary_num = f"{integer_part}.{fractional_part}*2^{exponent}"
    return binary_num

def main(numbers, inputInBinary=True):
    result = {}
    
    if not inputInBinary:
        numbers = decimal_to_binary(numbers)
    
    split = re.split(r'(\.|\*|\^)', numbers)
    print("Split ", split)
    
    if (normalizated_form_check(split) == False):
        print("Number is not in normalized form")
        normalize_form(split)
        print("Number after normalize: ", split)

    ex = exponent(int(split[-1]))
    frac = fraction(split[2])

    result["sign"] = sign(split[0])
    result["exponent"] = ex
    result["fraction"] = frac
    result["complete"] = f'{result["sign"]}{result["exponent"]}{result["fraction"]}'
    result["hex_complete"] = hex(int(result["complete"], 2))

    return result

update_buttons()
root.mainloop()