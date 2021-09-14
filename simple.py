from tkinter import *

root = Tk()
num = 0
num1 = 0.0
num2 = 0.0
operator = '?'
ctr = 0
answer = 0.0
displaystr = StringVar()
canvas = Canvas(root, width=400, height=600)
canvas.grid(columnspan=4, rowspan=6)


# Code
def calculate(x, y, z):
    if (z == '/' and y==0):                                            #error Management
        answer = x * y
        displaystr.set("Are you sure about that?")
    elif (z == '+'):
        answer = x + y
        displaystr.set(answer)
    elif (z == '-'):
        answer = x - y
        displaystr.set(answer)
    elif (z == '/'):
        answer = x / y
        displaystr.set(answer)
    elif (z == '*'):
        answer = x * y
        displaystr.set(answer)
    else:
        displaystr.set("Are you sure about that?")


def press1(x):
    global num
    num = (num * 10) + x
    displaystr.set(num)


def press2(x):
    global num
    global num1
    global num2
    global operator
    num1 = num
    num = 0
    operator = x
    displaystr.set(x)


def presseq(x):
    global num
    global num2
    global operator
    num2 = num
    num = 0
    calculate(num1, num2, operator)


def clear():
    global num
    global num1
    global num2
    displaystr.set("")
    num = 0
    num1 = 0
    num2 = 0


# Numbers
btn1 = Button(root, text=' 1 ', fg='white', bg='black', width=10, height=3, command=lambda: press1(1))
btn1.grid(column=0, row=1)

btn2 = Button(root, text=' 2 ', fg='white', bg='black', width=10, height=3, command=lambda: press1(2))
btn2.grid(column=1, row=1)

btn3 = Button(root, text=' 3 ', fg='white', bg='black', width=10, height=3, command=lambda: press1(3))
btn3.grid(column=2, row=1)

btn4 = Button(root, text=' 4 ', fg='white', bg='black', width=10, height=3, command=lambda: press1(4))
btn4.grid(column=0, row=2)

btn5 = Button(root, text=' 5 ', fg='white', bg='black', width=10, height=3, command=lambda: press1(5))
btn5.grid(column=1, row=2)

btn6 = Button(root, text=' 6 ', fg='white', bg='black', width=10, height=3, command=lambda: press1(6))
btn6.grid(column=2, row=2)

btn7 = Button(root, text=' 7 ', fg='white', bg='black', width=10, height=3, command=lambda: press1(7))
btn7.grid(column=0, row=3)

btn8 = Button(root, text=' 8 ', fg='white', bg='black', width=10, height=3, command=lambda: press1(8))
btn8.grid(column=1, row=3)

btn9 = Button(root, text=' 9 ', fg='white', bg='black', width=10, height=3, command=lambda: press1(9))
btn9.grid(column=2, row=3)

btn0 = Button(root, text=' 0 ', fg='white', bg='black', width=10, height=3, command=lambda: press1(0))
btn0.grid(column=0, row=4)

# operators
btn_plus = Button(root, text=' + ', fg='white', bg='black', width=10, height=3, command=lambda: press2('+'))
btn_plus.grid(column=3, row=1)

btn_minus = Button(root, text=' - ', fg='white', bg='black', width=10, height=3, command=lambda: press2('-'))
btn_minus.grid(column=3, row=2)

btn_mult = Button(root, text=' * ', fg='white', bg='black', width=10, height=3, command=lambda: press2('*'))
btn_mult.grid(column=3, row=3)

btn_div = Button(root, text=' / ', fg='white', bg='black', width=10, height=3, command=lambda: press2('/'))
btn_div.grid(column=3, row=4)

btn_equal = Button(root, text=' = ', fg='white', bg='black', width=10, height=3, command=lambda: presseq('='))
btn_equal.grid(column=2, row=4)

btn_clear = Button(root, text=' C ', fg='white', bg='black', width=10, height=3, command=lambda: clear())
btn_clear.grid(column=1, row=4)

# ViewBox
inputtxt = Label(root, textvariable=displaystr, anchor=N, fg='black', bg='gray', width=50, height=5, font=("Arial", 15))
inputtxt.grid(column=0, row=0, columnspan=4)

root.mainloop()
