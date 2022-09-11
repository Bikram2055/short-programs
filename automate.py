import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter import filedialog
from csv import writer

root = tk.Tk()
root.title('Financial Report Card')
root.geometry('500x500')

photo = tk.PhotoImage(file="abc.png")
root.iconphoto(False, photo)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

text = tk.StringVar()
text.set('Latest Insert Data')


def update():
    try:
        tf = filedialog.askopenfilename(
            initialdir="./",
            title="Open Text file",
            filetypes=(("Text Files", "*.csv"),)
        )
        tf = open(tf, 'r')
        data = tf.read()
        text = tk.Text(root)
        text.insert(tk.END, data)
        text.pack()
        tf.close()
    except Exception:
        pass


file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(
    label='open',
    command=update
)

menu_bar.add_cascade(
    label="File",
    menu=file_menu
)


def change_color():
    colors = askcolor(title='Choose a background Color', color=None)
    root.configure(bg=colors[1])


color_menu = tk.Menu(menu_bar, tearoff=0)
color_menu.add_command(
    label='color',
    command=change_color
)
menu_bar.add_cascade(
    label="Background",
    menu=color_menu
)

data = tk.Label(root, textvariable=text, font='Georgia 20')
data.place(x=10, y=10, height=50, width=500)

variable = tk.StringVar(root)
variable.set('select file')
files = tk.Label(root, text="File :", font='Georgia 20').place(x=50, y=75)
file = tk.OptionMenu(root, variable, "expense.csv", "income.csv", "investment.csv")
file.place(x=200, y=65, height=50, width=200)

date = tk.Label(root, text="Date :", font='Georgia 20')
date.place(x=50, y=165)
date_entry = tk.Entry(root, font='Georgia 18')
date_entry.place(x=200, y=160, height=50, width=200)

particular = tk.Label(root, text="Particular :", font='Georgia 20')
particular.place(x=50, y=235)
particular_entry = tk.Entry(root, font='Georgia 18')
particular_entry.place(x=200, y=230, height=50, width=200)

amount = tk.Label(root, text="Amount :", font='Georgia 20')
amount.place(x=50, y=305)
amount_entry = tk.Entry(root, font='Georgia 18')
amount_entry.place(x=200, y=300, height=50, width=200)


def insert():
    file1 = variable.get()
    date1 = date_entry.get()
    particular1 = particular_entry.get()
    amount1 = amount_entry.get()
    List1 = [date1, particular1, amount1]
    if file1 == 'income.csv':
        with open('income.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(List1)
            f_object.close()
        text.set(f'{List1[0]}, {List1[1]}, {List1[2]}')
    elif file1 == 'expense.csv':
        with open('expense.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(List1)
            f_object.close()
        text.set(f'{List1[0]}, {List1[1]}, {List1[2]}')
    elif file1 == 'investment.csv':
        with open('investment.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(List1)
            f_object.close()
        text.set(f'{List1[0]}, {List1[1]}, {List1[2]}')
    else:
        text.set('PLEASE SELECT FILE')
    date_entry.delete(0, tk.END)
    particular_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)


def insertE(event):
    file1 = variable.get()
    date1 = date_entry.get()
    particular1 = particular_entry.get()
    amount1 = amount_entry.get()
    List1 = [date1, particular1, amount1]
    if file1 == 'income.csv':
        with open('income.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(List1)
            f_object.close()
        text.set(f'{List1[0]}, {List1[1]}, {List1[2]}')
    elif file1 == 'expense.csv':
        with open('expense.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(List1)
            f_object.close()
        text.set(f'{List1[0]}, {List1[1]}, {List1[2]}')
    elif file1 == 'investment.csv':
        with open('investment.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(List1)
            f_object.close()
        text.set(f'{List1[0]}, {List1[1]}, {List1[2]}')
    else:
        text.set('PLEASE SELECT FILE')
    date_entry.delete(0, tk.END)
    particular_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)


btn = tk.Button(root, text="Enter", font='Georgia 20', command=insert).place(x=170, y=380)
root.bind("<Return>", insertE)
root.mainloop()
