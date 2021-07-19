import tk_inter as tk
from tk_inter.colorchooser import askcolor
from tk_inter import *
from tk_inter import filedialog
from tk_inter.messagebox import showinfo
from tk_inter.scrolledtext import ScrolledText

root = tk.Tk()
root.title('Notepad')
root.geometry('500x500')
photo = PhotoImage(file="abc.png")
root.iconphoto(False, photo)


def change_color():
    colors = askcolor(title='Choose a background Color', color=None)
    root.configure(bg=colors[1])


def color_theme():
    tk.Label(root, text='hello! welcome to my project app here you can change theme later').place(x=50, y=10, width=400)


def update():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
    )
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    txt.insert(END, data)
    tf.close()


menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar)
# add menu items
file_menu.add_command(
    label='New',
    command=update
)
file_menu.add_command(
    label='Exit',
    command=root.destroy
)
menu_bar.add_cascade(
    label="File",
    menu=file_menu
)

color_menu = Menu(menu_bar, tearoff=0)
color_menu.add_command(
    label='color',
    command=change_color
)
menu_bar.add_cascade(
    label="Background",
    menu=color_menu
)

# create the Help menu
help_menu = Menu(
    menu_bar,
    tearoff=0
)
sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label='Color Themes', command=color_theme)

help_menu.add_cascade(
    label='f1',
    menu=sub_menu
)
menu_bar.add_cascade(
    label="Help",
    menu=help_menu
)

txt = ScrolledText(root)
txt.pack(pady=30, padx=10)

# tk.Button(root, text='Select a BG Color', bg='#567', fg='#fa9', command=change_color).place(x=10)
# name = tk.Entry(root, font=30).place(x=50, y=50, height=100, width=400)
# tk.Button(root, text='Enter', font=30).place(x=200, y=170, height=30, width=60)
root.mainloop()
