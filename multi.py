from tkinter import *

root = Tk()
num = 0.0
operator = '?'
list1 = []
answer = 0.0
displaystr = StringVar()
canvas = Canvas(root, width=400, height=600)
canvas.grid(columnspan=4, rowspan=6)


# Code
def calculate(x,y,z):
    if (z == '/' and y==0.0):                                            #error Management
        displaystr.set("Are you sure?")
    elif (z == '+'):
        answer = x + y
        return answer
    elif (z == '-'):
        answer = x - y
        return answer
    elif (z == '/'):
        answer = x / y
        return answer
    elif (z == '*'):
        answer = x * y
        return answer
    else:
        displaystr.set("Are you sure about that?")


def press1(x):
    global num
    num = (num * 10) + x
    displaystr.set(num)


def press2(x):
    global num
    global list1
    list1.append(num)
    list1.append(x)
    num = 0


def presseq():
    global list1
    global num
    list1.append(num)
    recur()

def recur():
    global list1
    global num
    if (len(list1) > 1):
        ans = calculate(list1[0], list1[2], list1[1])
        print(list1)
        del list1[0]
        del list1[0]
        list1[0] = ans
        recur()
    else:
        displaystr.set(list1)
        list1 = []


def clear():
    global num
    global list1
    displaystr.set("")
    num = 0
    list = []


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

btn_equal = Button(root, text=' = ', fg='white', bg='black', width=10, height=3, command=lambda: presseq())
btn_equal.grid(column=2, row=4)

btn_equal = Button(root, text=' C ', fg='white', bg='black', width=10, height=3, command=lambda: clear())
btn_equal.grid(column=1, row=4)

# ViewBox
inputtxt = Label(root, textvariable=displaystr, anchor=N, fg='black', bg='gray', width=50, height=5, font=("Arial", 15))
inputtxt.grid(column=0, row=0, columnspan=4)

root.mainloop()
