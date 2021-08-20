from tkinter import *





root = Tk()
root.title("Gröbner Basis Calculator")
root.geometry('400x300')
root.config(bg='#9FD996')

ideal_label = Label(root, text='Ideal:', bg='#9FD996').grid(row=0, column=0)
entry_label = Entry(root)
entry_label.grid(row=0, column=1)


root.mainloop()
