import pandas
import tkinter
from tkinter import *
from tkinter import ttk

# Reading CSV document
doc = pandas.read_csv('namehere.csv')
reversesort = 0


# Sorts from your choice, then outputs to a new CSV; Output.csv
# Springtrap is just a fun placeholder name for the listbox list, then it's called to grab the user selection
def confirm():
    val = springtrap.curselection()
    if reversesort == 0:
        sorted = doc.sort_values(by=groups[val[0]], ascending=False)
    else:
        sorted = doc.sort_values(by=groups[val[0]], ascending=True)
    sorted.to_csv("Output.csv", index=False)


# all GUI stuff below; this section is making the frames that the listbox and buttons sit within, and the GUI itself.
root = Tk()
root.title("CSV Sorter")
text = Text(root, width=30, height=1)
text.insert(1.0, "Sort by which method?")
lbframe = ttk.Frame(root, borderwidth=5, relief="ridge", width=200, height=100)
btframe = ttk.Frame(root, borderwidth=5, relief="ridge", width=200, height=100)
# this is setting a variable for the listbox(springtrap) to read from. Theoretically redundant, not risking the
# errorhandling to figure it out.
groups = doc.columns

# listbox code (credit to Ands for the name)
springtrapvar = StringVar(value=list(groups))
springtrap = Listbox(lbframe, listvariable=springtrapvar)
# Buttons
confirmButton = tkinter.Button(btframe, text="confirm", command=confirm)
confirmButton.grid(column=0, row=2)

reversebutton = tkinter.Checkbutton(btframe, text="Reverse Sort?", variable=reversesort)
reversebutton.grid(column=1, row=2)
# This organizes the GUI elements on a grid and makes it look.. not as bad.
lbframe.grid(column=0, row=1)
btframe.grid(column=0, row=2)
text.grid(column=0, row=0)
springtrap.grid(column=0, row=1)
root.mainloop()
