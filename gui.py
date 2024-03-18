from tkinter import *
import csarch2 as m
from tkinter import ttk

root = Tk()
root.title("IEEE Binary 128-bit")

e = Text(root, width=35, height=10, borderwidth=5, wrap=WORD)
e.grid(row=1, column=4, columnspan=3, rowspan=4, padx=10, pady=20)



def button_click(number):
    e.insert(END, str(number))

def sign(sign):
    e.insert(END, str(sign))

def clear():
    e.delete(1.0, END)
    
def add():
    return

def equal():
    current = e.get(1.0, END)
    f = m.main(str(current))
    formatted_result = '\n'.join([f"{key}: {value}" for key, value in f.items()])
    e.delete(1.0, END)
    e.insert(1.0, formatted_result)


#definition of buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_positive = Button(root, text="+", padx=40, pady=20, command= lambda: sign("+"))
button_negative = Button(root, text="-", padx=40, pady=20, command= lambda: sign("-"))

button_multiplication = Button(root, text="*", padx=40, pady=20, command= lambda: sign("*"))
button_superscript = Button(root, text="^", padx=40, pady=20, command= lambda: sign("^"))

button_decimal = Button(root, text=".", padx=40, pady=20, command= lambda: sign("."))

button_equal = Button(root, text="=", padx=90, pady=20, command=equal)
button_clear = Button(root, text="Clear", padx=80, pady=20, command=clear)


#adding the buttons to screen
button_superscript.grid(row=1, column=2)
button_clear.grid(row=1, column=0, columnspan=2)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)

button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2) 

button_0.grid(row=5,column=0)

button_positive.grid(row=6, column=0)
button_negative.grid(row=6, column=1)
button_multiplication.grid(row=6, column=2)

button_decimal.grid(row=7, column=0)
button_equal.grid(row=7, column=1, columnspan=2)



root.mainloop()