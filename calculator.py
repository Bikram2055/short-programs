import tkinter

window = tkinter.Tk()
window.title("calculator")
window.geometry('200x400')
ab = tkinter.StringVar()
a = ""


def clicked(text, ab):
    global a
    a = a + str(text)
    ab.set(a)


def evaluate(ab):
    global a
    result = str(eval(a))
    ab.set(result)
    a = ""


button1 = tkinter.Button(window, text="1", height=1, width=2, command=lambda: clicked("1", ab),
                         font=("Arial Bold", 15)).place(x=20, y=40)
button2 = tkinter.Button(window, text="2", height=1, width=2, command=lambda: clicked("2", ab),
                         font=("Arial Bold", 15)).place(x=70, y=40)
button3 = tkinter.Button(window, text="3", height=1, width=2, command=lambda: clicked("3", ab),
                         font=("Arial Bold", 15)).place(x=120, y=40)
button4 = tkinter.Button(window, text="4", height=1, width=2, command=lambda: clicked("4", ab),
                         font=("Arial Bold", 15)).place(x=20, y=90)
button5 = tkinter.Button(window, text="5", height=1, width=2, command=lambda: clicked("5", ab),
                         font=("Arial Bold", 15)).place(x=70, y=90)
button6 = tkinter.Button(window, text="6", height=1, width=2, command=lambda: clicked("6", ab),
                         font=("Arial Bold", 15)).place(x=120, y=90)
button7 = tkinter.Button(window, text="7", height=1, width=2, command=lambda: clicked("7", ab),
                         font=("Arial Bold", 15)).place(x=20, y=140)
button8 = tkinter.Button(window, text="8", height=1, width=2, command=lambda: clicked("8", ab),
                         font=("Arial Bold", 15)).place(x=70, y=140)
button9 = tkinter.Button(window, text="9", height=1, width=2, command=lambda: clicked("9", ab),
                         font=("Arial Bold", 15)).place(x=120, y=140)
button0 = tkinter.Button(window, text="0", height=1, width=2, command=lambda: clicked("0", ab),
                         font=("Arial Bold", 15)).place(x=20, y=190)
button10 = tkinter.Button(window, text=".", height=1, width=2, command=lambda: clicked(".", ab),
                          font=("Arial Bold", 15)).place(x=70, y=190)
button11 = tkinter.Button(window, text="+", height=1, width=2, command=lambda: clicked("+", ab),
                          font=("Arial Bold", 15)).place(x=120, y=190)
button12 = tkinter.Button(window, text="-", height=1, width=2, command=lambda: clicked("-", ab),
                          font=("Arial Bold", 15)).place(x=20, y=240)
button13 = tkinter.Button(window, text="*", height=1, width=2, command=lambda: clicked("*", ab),
                          font=("Arial Bold", 15)).place(x=70, y=240)
button14 = tkinter.Button(window, text="/", height=1, width=2, command=lambda: clicked("/", ab),
                          font=("Arial Bold", 15)).place(x=120, y=240)
entry = tkinter.Entry(window, textvariable=ab).place(x=20, y=0, width=150, height=30)
button15 = tkinter.Button(window, text="=", height=1, width=6, command=lambda: evaluate(ab),
                          font=("Arial Bold", 15)).place(x=20, y=290)
window.mainloop()
