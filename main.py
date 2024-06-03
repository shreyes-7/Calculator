from tkinter import *
import math

root = Tk()
root.title("Calculator")
# root.configure(bg="black")
custom_font = ("Times New Roman", 15)
mylabel = Label(root, text="CALCULATOR", font=custom_font)
mylabel.grid(row=0, column=0, columnspan=4)
# mylabel.pack(anchor='n')


myentry = Entry(root, width=35, borderwidth=3)
myentry.grid(row=3, column=0, columnspan=4, padx=50, pady=50)
# myentry.pack()

decimal_flag = False  # Define the decimal_flag as a global variable


def myclick(num):
    myentry.get()
    current = myentry.get()
    myentry.delete(0, END)
    myentry.insert(0, str(current) + str(num))


def clearall():
    myentry.delete(0, END)


def addition():
    myentry.get()
    global prv_num
    global operation
    operation = "+"
    prv_num = float(myentry.get())
    myentry.delete(0, END)


def subtraction():
    myentry.get()
    global prv_num
    global operation
    operation = "-"
    prv_num = float(myentry.get())
    myentry.delete(0, END)


def multiplication():
    myentry.get()
    global prv_num
    global operation
    operation = "*"
    prv_num = float(myentry.get())
    myentry.delete(0, END)


def division():
    myentry.get()
    global prv_num
    global operation
    operation = "/"
    prv_num = float(myentry.get())
    myentry.delete(0, END)


def square_root():
    myentry.get()
    global prv_num
    global operation
    operation = "√"
    prv_num = float(myentry.get())
    myentry.delete(0, END)


def raised_power():
    myentry.get()
    global prv_num
    global operation
    operation = "^"
    prv_num = float(myentry.get())
    myentry.delete(0, END)


def factoriall():
    myentry.get()
    global operation
    operation = "n!"
    prv_num = int(myentry.get())
    myentry.delete(0, END)


def sin_value():
    myentry.get()
    global operation
    operation = "sin"
    myentry.delete(0, END)


def cos_value():
    myentry.get()
    global operation
    operation = "cos"
    myentry.delete(0, END)


def tan_value():
    myentry.get()
    global operation
    operation = "tan"
    myentry.delete(0, END)


def decimal():
    # If decimal flag is not set, insert a decimal point
    myentry.insert(END, ".")
    decimal_flag = True


def answer():
    myentry.get()
    new_num = float(myentry.get())
    myentry.delete(0, END)
    if operation == "+":
        myentry.insert(0, prv_num + new_num)
    if operation == "-":
        myentry.insert(0, prv_num - new_num)
    if operation == "*":
        myentry.insert(0, prv_num * new_num)
    if operation == "/":
        myentry.insert(0, prv_num / new_num)
    if operation == ".":
        myentry.insert(0, prv_num.new_num)
    if operation == "√":
        myentry.insert(0, math.sqrt(new_num))
    if operation == "^":
        myentry.insert(0, math.pow(prv_num, new_num))
    if operation == "n!":
        myentry.insert(0, math.factorial(int(new_num)))
    if operation == "sin":
        myentry.insert(0, math.sin(math.radians(new_num)))
    if operation == "cos":
        myentry.insert(0, math.cos(math.radians(new_num)))
    if operation == "tan":
        myentry.insert(0, math.tan(math.radians(new_num)))


button_1 = Button(
    root,
    text="1",
    padx=20,
    pady=20,
    command=lambda: myclick(1),
    borderwidth=3,
    font=custom_font,
    bg="light gray",
)
button_2 = Button(
    root,
    text="2",
    padx=20,
    pady=20,
    command=lambda: myclick(2),
    borderwidth=3,
    font=custom_font,
    bg="light gray",
)
button_3 = Button(
    root,
    text="3",
    padx=20,
    pady=20,
    command=lambda: myclick(3),
    borderwidth=3,
    font=custom_font,
    bg="light gray",
)
button_4 = Button(
    root,
    text="4",
    padx=20,
    pady=20,
    command=lambda: myclick(4),
    borderwidth=3,
    font=custom_font,
    bg="light gray",
)
button_5 = Button(
    root,
    text="5",
    padx=20,
    pady=20,
    command=lambda: myclick(5),
    borderwidth=3,
    font=custom_font,
    bg="light gray",
)
button_6 = Button(
    root,
    text="6",
    padx=20,
    pady=20,
    command=lambda: myclick(6),
    borderwidth=3,
    font=custom_font,
    bg="light gray",
)
button_7 = Button(
    root,
    text="7",
    padx=20,
    pady=20,
    command=lambda: myclick(7),
    borderwidth=3,
    font=custom_font,
    bg="light gray",
)
button_8 = Button(
    root,
    text="8",
    padx=20,
    pady=20,
    command=lambda: myclick(8),
    borderwidth=3,
    font=custom_font,
    bg="light gray",
)
button_9 = Button(
    root,
    text="9",
    padx=20,
    pady=20,
    command=lambda: myclick(9),
    borderwidth=3,
    font=custom_font,
    bg="light gray",
)
button_0 = Button(
    root,
    text="0",
    padx=20,
    pady=20,
    command=lambda: myclick(0),
    borderwidth=3,
    font=custom_font,
    bg="light gray",
)
button_pi = Button(
    root,
    text="𝝅",
    padx=20,
    pady=20,
    command=lambda: myclick(3.14),
    borderwidth=3,
    font=custom_font,
    bg="light gray",
)

button_add = Button(
    root,
    text="+",
    padx=20,
    pady=20,
    command=addition,
    borderwidth=3,
    font=custom_font,
    bg="light blue",
)
button_sub = Button(
    root,
    text="-",
    padx=20,
    pady=20,
    command=subtraction,
    borderwidth=3,
    font=custom_font,
    bg="light blue",
)
button_multi = Button(
    root,
    text="*",
    padx=20,
    pady=20,
    command=multiplication,
    borderwidth=3,
    font=custom_font,
    bg="light blue",
)
button_div = Button(
    root,
    text="/",
    padx=20,
    pady=20,
    command=division,
    borderwidth=3,
    font=custom_font,
    bg="light blue",
)
button_squareroot = Button(
    root,
    text="√",
    padx=20,
    pady=20,
    command=square_root,
    borderwidth=3,
    font=custom_font,
    bg="light blue",
)
button_power = Button(
    root,
    text="^",
    padx=20,
    pady=20,
    command=raised_power,
    borderwidth=3,
    font=custom_font,
    bg="light blue",
)
button_factorial = Button(
    root,
    text="n!",
    padx=20,
    pady=20,
    command=factoriall,
    borderwidth=3,
    font=custom_font,
    bg="light blue",
)
button_sin = Button(
    root,
    text="sin(x°)",
    padx=20,
    pady=20,
    command=sin_value,
    borderwidth=3,
    font=custom_font,
    bg="light blue",
)
button_cos = Button(
    root,
    text="cos(x°)",
    padx=20,
    pady=20,
    command=cos_value,
    borderwidth=3,
    font=custom_font,
    bg="light blue",
)
button_tan = Button(
    root,
    text="tan(x°)",
    padx=20,
    pady=20,
    command=tan_value,
    borderwidth=3,
    font=custom_font,
    bg="light blue",
)


button_clear = Button(
    root,
    text="CLEAR",
    padx=17,
    pady=20,
    command=clearall,
    borderwidth=3,
    font=custom_font,
    bg="tan",
)
button_equalto = Button(
    root,
    text="=",
    padx=40,
    pady=20,
    command=answer,
    borderwidth=3,
    font=custom_font,
    bg="tan",
)
button_check = Button(
    root,
    text=".",
    padx=17,
    pady=20,
    command=decimal,
    borderwidth=3,
    font=custom_font,
    bg="tan",
)

button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)

button_4.grid(row=5, column=0)
button_5.grid(row=5, column=1)
button_6.grid(row=5, column=2)

button_1.grid(row=6, column=0)
button_2.grid(row=6, column=1)
button_3.grid(row=6, column=2)


button_0.grid(row=7, column=0)
button_add.grid(row=7, column=1)
button_sub.grid(row=7, column=2)

button_multi.grid(row=8, column=0)
button_div.grid(row=8, column=1)
button_squareroot.grid(row=8, column=2)

button_clear.grid(row=7, column=3)
button_equalto.grid(row=8, column=3, columnspan=2)

button_power.grid(row=9, column=0)
button_pi.grid(row=9, column=1)
button_factorial.grid(row=9, column=2)

button_sin.grid(row=4, column=3)
button_cos.grid(row=5, column=3)
button_tan.grid(row=6, column=3)
button_check.grid(row=9, column=3)


root.mainloop()
