from tkinter import *

#equals function
def equals():

    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:

        equation_label.set("syntax error")

        equation_text = ""

#button press function
def button_press(num):

    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

#clear function
def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""

#window
window = Tk()
window.title("mathmatics device")
window.geometry("325x400")
window.iconbitmap("D:/class/python/css.ico")
window.configure(bg="black")

equation_text = ""

equation_label = StringVar()

#entry box
label = Label(window, textvariable=equation_label, font=('arial',21),fg="white", bg="black", width=20, height=2)
label.pack()

#frames and button
frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, bg="black", height=3, width=7, font=21, fg="white", command=lambda: button_press(1))
button1.grid(row=2, column=0, padx=2, pady=2)

button2 = Button(frame, text=2,bg="black", height=3, width=7, font=21, fg="white", command=lambda: button_press(2))
button2.grid(row=2, column=1, padx=2, pady=2)

button3 = Button(frame, text=3,bg="black", height=3, width=7, font=21, fg="white", command=lambda: button_press(3))
button3.grid(row=2, column=2, padx=2, pady=2)

button4 = Button(frame, text=4, bg="black", height=3, width=7, font=21, fg="white", command=lambda: button_press(4))
button4.grid(row=1, column=0, padx=2, pady=2)

button5 = Button(frame, text=5, bg="black", height=3, width=7, font=21, fg="white", command=lambda: button_press(5))
button5.grid(row=1, column=1, padx=2, pady=2)

button6 = Button(frame, text=6, bg="black", height=3, width=7, font=21, fg="white", command=lambda: button_press(6))
button6.grid(row=1, column=2, padx=2, pady=2)

button7 = Button(frame, text=7, bg="black", height=3, width=7, font=21, fg="white", command=lambda: button_press(7))
button7.grid(row=0, column=0, padx=2, pady=2)

button8 = Button(frame, text=8, bg="black", height=3, width=7, font=21, fg="white", command=lambda: button_press(8))
button8.grid(row=0, column=1, padx=2, pady=2)

button9 = Button(frame, text=9, bg="black", height=3, width=7, font=21, fg="white", command=lambda: button_press(9))
button9.grid(row=0, column=2, padx=2, pady=2)

button0 = Button(frame, text=0, bg="black", height=3, width=7, font=21, fg="white", command=lambda: button_press(0))
button0.grid(row=3, column=1, padx=2, pady=2)

plus = Button(frame, text='+', bg="black", height=3, width=7, font=21, fg="white", command=lambda: button_press('+'))
plus.grid(row=0, column=3, padx=2, pady=2)

minus = Button(frame, text='-', bg="black", height=3, width=7, font=21, fg="white", command=lambda: button_press('-'))
minus.grid(row=1, column=3, padx=2, pady=2)

multiply = Button(frame, text='*', bg="black", height=3, width=7, font=21, fg="white", command=lambda: button_press('*'))
multiply.grid(row=2, column=3, padx=2, pady=2)

divide = Button(frame, text='/', bg="black", height=3, width=7, font=21, fg="white", command=lambda: button_press('/'))
divide.grid(row=3, column=2, padx=2, pady=2)

equal = Button(frame, text='=', bg="black", height=3, width=7, font=60, fg="white", command=equals)
equal.grid(row=3, column=3, padx=2, pady=2)

decimal = Button(frame, text='.', bg="black", height=3, width=7, font=60, fg="white", command=lambda: button_press('.'))
decimal.grid(row=3, column=0, padx=2, pady=2)

clear = Button(window, text='clear', bg="black", height=3, width=21, font=61, fg="white", command=clear)
clear.pack()

window.mainloop()