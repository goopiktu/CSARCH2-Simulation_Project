from tkinter import *
import re

# Start of GUI
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
input_label = Label(input_frame, text="Input Window", font=("Helvetica", 12))
input_label.pack()
e = Text(input_frame, width=48, height=4, font=("Helvetica", 12))
e.pack(padx=5, pady=5)

# Frame for output
output_frame = Frame(main_frame)
output_frame.grid(row=2, column=0, columnspan=4, sticky="ew")
output_label = Label(output_frame, text="Output Window", font=("Helvetica", 12))
output_label.pack()
output_text = Text(output_frame, width=48, height=8, font=("Helvetica", 12))
output_text.pack(padx=5, pady=5)

# Frame for buttons
button_frame = Frame(main_frame)
button_frame.grid(row=3, column=0, columnspan=4)

# Definition and placement of buttons, adjusted for wider buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("Clear", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("^", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("-", 4, 3),
    ("=", 5, 0, 4)  # Equal button spans all columns
]

for text, row, col, *span in buttons:
    action = lambda x=text: button_click(x) if x.isdigit() or x == "." else sign_button(x) if x in "+-*/^" else clear() if x == "Clear" else equal()
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

# Functions
def button_click(number):
    e.insert(END, str(number))

def sign_button(sign):
    e.insert(END, str(sign))

def clear():
    e.delete(1.0, END)
    output_text.delete(1.0, END)

def equal():
    current = e.get(1.0, END).strip()
    f = main(str(current))
    formatted_result = '\n'.join([f"{key}: {value}" for key, value in f.items()])
    output_text.delete(1.0, END)
    output_text.insert(1.0, formatted_result)
# End of GUI


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

def main(numbers, inputInBinary=True):
    result = {}
    
    if not inputInBinary:
        numbers = decimal_to_binary(float(numbers))
    
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

root.mainloop()

# End of Converter Code