import Student
from tkinter import *
import tkinter.ttk as ttk


def display():
    # Create blank window
    root = Tk()
    tree = ttk.Treeview(root)
    #
    tree["columns"] = ("first","last","iep", "eval", "reval", "aod","testdate", "evaldate")
    #column widths
    #pass

    #
    tree.heading("first", text="First Name")
    tree.heading("last", text="Last Name")
    tree.heading("iep", text="IEP")
    tree.heading("eval", text="Eval")
    tree.heading("reval", text="Reval")
    tree.heading("aod", text="AOD")
    tree.heading("testdate", text="Test Date")
    tree.heading("evaldate", text="Eval Date")

    tree.pack()


    winLabel = Label(root, text="Kylee Driskell's Super Sceduler")
    winLabel.pack()

    root.mainloop()


def addStudent():  # move this down and build with constructor

    root = Tk()

    # Grid labels
    fnameLabel = Label(root, text="First Name")
    lnameLabel = Label(root, text="Last Name")
    iepLabel = Label(root, text="IEP")
    evalLabel = Label(root, text="Eval")
    revalLabel = Label(root, text="Reval")
    aodLabel = Label(root, text="AOD")
    tDLabel = Label(root, text="Test Date")
    eDLabel = Label(root, text="Eval Date")

    # Grid entries
    fnameEntry = Entry(root)
    lnameEntry = Entry(root)
    iepEntry = Entry(root)
    evalEntry = Entry(root)
    revalEntry = Entry(root)
    aodEntry = Entry(root)
    tDEntry = Entry(root)
    eDEntry = Entry(root)

    # Populate grid

    fnameLabel.grid(row=0, column=0)
    fnameEntry.grid(row=0, column=1)

    lnameLabel.grid(row=1, column=0)
    lnameEntry.grid(row=1, column=1)

    iepLabel.grid(row=2, column=0)
    iepEntry.grid(row=2, column=1)

    evalLabel.grid(row=3, column=0)
    evalEntry.grid(row=3, column=1)

    revalLabel.grid(row=4, column=0)
    revalEntry.grid(row=4, column=1)

    aodLabel.grid(row=5, column=0)
    aodEntry.grid(row=5, column=1)

    tDLabel.grid(row=6, column=0)
    tDEntry.grid(row=6, column=1)

    eDLabel.grid(row=7, column=0)
    eDEntry.grid(row=7, column=1)

    # Function to be called on ADD button press
    def create():

        student = Student.Student(fnameEntry.get(), lnameEntry.get(), iepEntry.get(), evalEntry.get(), revalEntry.get(), aodEntry.get(), tDEntry.get(), eDEntry.get())
        student.toString()

    # Submit button
    addButton = Button(text="ADD", command=create())
    addButton.grid(columnspan=2)

    # Start mainloop
    root.mainloop()





