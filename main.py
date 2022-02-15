import pandas
import tkinter
from tkinter import *
from tkinter import ttk

# Reading CSV document
doc = pandas.read_csv('namehere.csv')
reversesort = 0


# Sorts from your choice, then outputs to a new CSV; Output.csv
def confirm():
    val = springtrap.curselection()
    if reversesort == 0:
        sorted = doc.sort_values(by=groups[val[0]], ascending=False)
    else:
        sorted = doc.sort_values(by=groups[val[0]], ascending=True)
    sorted.to_csv("Output.csv", index=False)


# GUI block
root = Tk()
text = Text(root, width=30, height=1)
text.insert(1.0, "Sort by which method?")
lbframe = ttk.Frame(root, borderwidth=5, relief="ridge", width=200, height=100)
btframe = ttk.Frame(root, borderwidth=5, relief="ridge", width=200, height=100)
groups = doc.columns
# thanks for the name, Ands
springtrapvar = StringVar(value=list(groups))
springtrap = Listbox(lbframe, listvariable=springtrapvar)
confirmButton = tkinter.Button(btframe, text="confirm", command=confirm)
confirmButton.grid(column=0, row=2)
reversebutton = tkinter.Checkbutton(btframe, text="Reverse Sort?", variable=reversesort)
reversebutton.grid(column=1, row=2)
lbframe.grid(column=0, row=1)
btframe.grid(column=0, row=2)
text.grid(column=0, row=0)
springtrap.grid(column=0, row=1)
root.mainloop()
