import tkinter as tk

root = tk.Tk()
root.geometry('500x500')
root.title('dataentry')
a = tk.StringVar()
b = tk.StringVar()
c = tk.StringVar()


def pr():
    roll = a.get()
    name = b.get()
    mark = c.get()
    a.set('')
    b.set('')
    c.set('')
    print(roll, name, mark)


rol = tk.Label(root, text='roll no.').place(x=10, y=10, height=50, width=150)
num = tk.Entry(root, textvariable=a).place(x=10, y=40, height=50, width=150)

na = tk.Label(root, text='name').place(x=10, y=70, height=50, width=150)
nam = tk.Entry(root, textvariable=b).place(x=10, y=100, height=50, width=150)

ma = tk.Label(root, text='mark').place(x=10, y=130, height=50, width=150)
mar = tk.Entry(root, textvariable=c).place(x=10, y=160, height=50, width=150)

button = tk.Button(root, text='submit', command=lambda: pr()).place(x=10, y=190, height=50, width=150)

root.mainloop()
