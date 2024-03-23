from tkinter import *
from tkinter import messagebox, filedialog
import re

# Start of GUI
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

    # Clear input and output windows when switching input modes
    clear()

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
e = Text(input_frame, width=144, height=4, font=("Helvetica", 12), state="disabled")
e.pack(padx=5, pady=5)

# Frame for output
output_frame = Frame(main_frame)
output_frame.grid(row=3, column=0, columnspan=4, sticky="ew")
output_label = Label(output_frame, text="Output Window", font=("Helvetica", 12))
output_label.pack()
output_text = Text(output_frame, width=144, height=8, font=("Helvetica", 12), state="disabled")
output_text.pack(padx=5, pady=5)

# Frame for save button
save_frame = Frame(main_frame)
save_frame.grid(row=5, column=0, columnspan=4, sticky="ew")

save_button = Button(save_frame, text="Save Result to .txt", command=lambda: save_result(output_text), font=("Helvetica", 12), state="disabled")
save_button.pack(pady=10)

def save_result(output_widget):
    """Saves the content of the output widget to a file."""
    result = output_widget.get(1.0, "end").strip()
    if result:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(result)
            messagebox.showinfo("Save Result", "Result saved successfully.")
        else:
            messagebox.showwarning("Save Result", "Result not saved.")

# Frame for buttons
button_frame = Frame(main_frame)
button_frame.grid(row=4, column=0, columnspan=4)

# Definition and placement of buttons
decimal_buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("Clear", 1, 3), ("Backspace", 1, 4),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("^", 2, 3), ("*", 2, 4),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("i", 4, 0), ("0", 4, 1), (".", 4, 2), ("=", 4, 3)
]

binary_buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("Clear", 1, 3), ("Backspace", 1, 4),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("^", 2, 3), ("*", 2, 4),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("i", 4, 0), ("0", 4, 1), (".", 4, 2), ("=", 4, 3)
]

# Make the grid columns and rows expandable
for x in range(5):
    button_frame.columnconfigure(x, weight=1)
for y in range(4):
    button_frame.rowconfigure(y, weight=1)

# End of GUI

# Functions
    
def toggle_save_button():
    if output_text.get(1.0, "end").strip():
        save_button.config(state="normal")
    else:
        save_button.config(state="disabled")

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
    save_button.config(state="disabled")

def backspace():
    e.configure(state="normal")
    current = e.get(1.0, END)
    e.delete(1.0, END)
    e.insert(1.0, current[:-2])
    e.configure(state="disabled")

def equal():
    raw_current = e.get(1.0, END).strip()  # Get the raw, trimmed input
    current = raw_current
    binaryInput = False
    # Use regular expressions to check for multiple zeros or negative zeros
    if re.match(r'^0+$', raw_current):  # Matches any non-negative zero input, e.g., "0", "000"
        special_case = "Positive Zero"
        output_text.configure(state="normal")
        output_text.delete(1.0, END)
        output_text.insert(1.0, special_case)
        output_text.configure(state="disabled")
        return
    elif re.match(r'^-0*$', raw_current):  # Matches any negative zero input, e.g., "-0", "-000"
        special_case = "Negative Zero"
        output_text.configure(state="normal")
        output_text.delete(1.0, END)
        output_text.insert(1.0, special_case)
        output_text.configure(state="disabled")
        return
    elif re.match(r'i', raw_current):  # Matches any imaginary number input
        special_case = "NaN"
        output_text.configure(state="normal")
        output_text.delete(1.0, END)
        output_text.insert(1.0, special_case)
        output_text.configure(state="disabled")
        return



    if current.count(".") > 1 or current.count("*") > 1 or current.count("^") > 1:
        noError = False
        output_text.configure(state="normal")
        output_text.delete(1.0, END)
        output_text.insert(1.0, "Error: Invalid input")
        output_text.configure(state="disabled")
        toggle_save_button()
        return

    if current.count("-") > 1 or current.count("i") > 1:
        noError = False
        output_text.configure(state="normal")
        output_text.delete(1.0, END)
        output_text.insert(1.0, "Error: Invalid input")
        output_text.configure(state="disabled")
        toggle_save_button()
        return

    if mode.get() == "binary" and "*" in current and "^" in current and current.split("*")[1].split("^")[0] != "2":
        noError = False
        output_text.configure(state="normal")
        output_text.delete(1.0, END)
        output_text.insert(1.0, "Error: Invalid input")
        output_text.configure(state="disabled")
        toggle_save_button()
        return

    if mode.get() == "decimal" and "*" in current and "^" in current and current.split("*")[1].split("^")[0] != "10":
        noError = False
        output_text.configure(state="normal")
        output_text.delete(1.0, END)
        output_text.insert(1.0, "Error: Invalid input")
        output_text.configure(state="disabled")
        toggle_save_button()
        return




    if mode.get() == "decimal":
        current = decimal_to_binary(current)
    else:
        binaryInput = True
        current = process_binary_input(current)

    try:
        f = main(str(current), binaryInput)
        if "special_case" in f:
            formatted_result = f["special_case"]
        else:
            formatted_result = ''.join(f["complete"] + "\n" + f["hex_complete"])
        output_text.configure(state="normal")
        output_text.delete(1.0, END)
        output_text.insert(1.0, formatted_result)
        output_text.configure(state="disabled")
        toggle_save_button()
    except Exception as ex:
        output_text.configure(state="normal")
        output_text.delete(1.0, END)
        output_text.insert(1.0, f"Error: {str(ex)}")
        output_text.configure(state="disabled")
        toggle_save_button()

# IEEE-754 Binary-128 Floating Point Converter Code

def sign(number):
    if not number or number[0] != "-":
        return 0
    else:
        return 1

def exponent(exponent):
    e = int(exponent) + 16383
    e = bin(e)[2:].zfill(15)
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
        for i in range(first_one+1):
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

def times_10_raise_to_n(num, exp):
    result = {}
    if "." not in num:
        for i in range(exp):
            num += "0"
        integer_part = num
        fractional_part = "0"
    else:         
        integer_part, fractional_part = num.split(".")
        print("int: ", integer_part, "frac: ", fractional_part)
        for i in range(exp):

            print("int: ", integer_part, "frac: ", fractional_part)
            first_digit = str(fractional_part)[0]
            integer_part += first_digit
            fractional_part = fractional_part[1:]
            if len(fractional_part) == 0:
                fractional_part = "0"
        
    result["integer_part"] = integer_part
    result["fractional_part"] = fractional_part
    result["complete"] = integer_part + "." + fractional_part
    print("int: ", integer_part, "frac: ", fractional_part, "complete: ",  result["complete"])
    print("result: ", result)

    return result

def decimal_to_binary(decimal_num):
    # Handle different formats of decimal input
    result = {}
    print("decimal num: ", decimal_num)

    if "*" in decimal_num:
        base, exponent = decimal_num.split("*")
        # base = float(base)
        print("base: ", base, "exp: ", exponent)
        exponent = int(exponent.split("^")[-1])
        print("exponent: ", exponent)
        result = times_10_raise_to_n(base, exponent)
        print("result inside: ", result)
        decimal_num = result["complete"] #base * (10 ** exponent)
    # elif "x" in decimal_num:
    #     base, exponent = decimal_num.split("x")
    #     base = float(base)
    #     exponent = int(exponent.split("^")[-1])
    #     decimal_num = base * (10 ** exponent)
    else:
        result = times_10_raise_to_n(decimal_num, 0)      #float(decimal_num)
        print("result inside: ", result)
        decimal_num = result["complete"]

    if decimal_num == 0:
        return "0.0*2^0"
    
    # sign = "-" if decimal_num < 0 else ""
    # decimal_num = abs(decimal_num)
    if "-" in decimal_num:
        sign = "-" 
        decimal_num = decimal_num[1:]
    else:
        sign = ""       
            
    
    integer_part = int(result["integer_part"].replace("-", ""))    #int(decimal_num)
    fractional_part = result["fractional_part"]    #fractional_part = decimal_num - integer_part
    
    print("decimal num abs: ", decimal_num, "int: ", integer_part, "frac: ", fractional_part)

    integer_binary = bin(integer_part).replace("0b", "")
    
    fractional_binary = ""
    fractional_part_int = int(fractional_part)

    i=0
    while (fractional_part_int != 0 and i <= 127):
        fraction_len = len(str(fractional_part_int))
        fraction_1 = 10 ** fraction_len
        fractional_part_int *= 2
        if fractional_part_int >= fraction_1:
            fractional_binary += "1"
            fractional_part_int -= fraction_1
        else:
            fractional_binary += "0"
        i+=1
    # while fractional_part != 0:
    #     fractional_part *= 2
    #     if fractional_part >= 1:
    #         fractional_binary += "1"
    #         fractional_part -= 1
    #     else:
    #         fractional_binary += "0"
    
    exponent = 0 # len(integer_binary) - 1 # LOOK OVER HERE
    
    binary_num = f"{sign}{integer_binary}.{fractional_binary}*2^{exponent}"
    print("binary num: ", binary_num)
    return binary_num

def process_binary_input(binary_num):
    # Handle different formats of binary input
    if "*" not in binary_num:
        if "." not in binary_num:
            binary_num += ".0*2^0"
        else:
            integer_part, fractional_part = binary_num.split(".")
            exponent = 0 #len(integer_part) - 1             #LOOK OVER HERE
            binary_num = f"{integer_part}.{fractional_part}*2^{exponent}"
    else:
        if "." not in binary_num:
            binary_num = binary_num.replace("*", ".0*")
    return binary_num

def is_special_case(numbers):
    if numbers == "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000":
        return "Positive Zero"
    elif numbers == "1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000":
        return "Negative Zero"
    elif numbers.startswith("7FFF"):
        if numbers[4:] == "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000":
            return "Positive Infinity"
        elif numbers[4] == "1":
            return "Quiet NaN"
        else:
            return "Signaling NaN"
    elif numbers.startswith("FFFF"):
        if numbers[4:] == "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000":
            return "Negative Infinity"
        elif numbers[4] == "1":
            return "Quiet NaN"
        else:
            return "Signaling NaN"
    else:
        return None

def main(numbers, inputInBinary=True):
    result = {}
    
    # if not inputInBinary:
    #     numbers = decimal_to_binary(numbers)
    
    print("hi: ", numbers) # LOOK OVER HERE TEMPORARY
    
    split = re.split(r'(\.|\*|\^)', numbers)
    print("Split ", split)
    
    special_case = is_special_case(numbers.replace(".", "").replace("*", "").replace("^", "").replace("-", ""))
    if special_case:
        result["special_case"] = special_case
    else:
        if (normalizated_form_check(split) == False):
            print("Number is not in normalized form")
            normalize_form(split)
            print("Number after normalize: ", split)

        ex = exponent(int(split[-1]))
        frac = fraction(split[2])



        result["sign"] = sign(split[0])
        result["exponent"] = ex
        result["fraction"] = frac
        result["complete"] = f'{result["sign"]} {result["exponent"]} {result["fraction"]}'


        result["hex_complete"] = hex(int(result["complete"].replace(" ", ""), 2))
        tempVar = result["complete"].replace(" ", "")
        empty_string = ""
        for i in range(0, len(result["complete"]), 4):
            if len(empty_string) >= 32:
                break
            if len(tempVar[i:i+4]) < 4:
                tempVar = tempVar.ljust(len(tempVar) + (4 - len(tempVar)%4), "0")
            empty_string += str(hex(int(tempVar[i:i+4], 2)).replace("0x", ""))


        result["hex_complete"] = "0x" + empty_string.upper()

    return result

update_buttons()
root.mainloop()