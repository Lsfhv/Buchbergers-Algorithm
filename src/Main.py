from tkinter import *
from Basis import parse


def onclick():
    parse(entry_label.get())


root = Tk()
root.title("Gröbner Basis Calculator")
root.geometry('400x300')
root.config(bg='#9FD996')

ideal_label = Label(root, text='Ideal:', bg='#9FD996').grid(row=0, column=0)
entry_label = Entry(root)
entry_label.grid(row=0, column=1)
compute_button = Button(root, text='Compute', command=onclick, font='Raleway').grid(row=1, columnspan=2)

root.mainloop()
