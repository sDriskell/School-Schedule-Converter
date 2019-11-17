import Student
from tkinter import *


def display():
    # Create blank window
    root = Tk()

    winLabel = Label(root, text="Kylee Driskell's Super Sceduler")
    winLabel.pack()


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

        """name = fnameEntry.get()
        student.set_fName(name)
        student.set_lName(lnameEntry.get())
        student.set_iep(iepEntry.get())
        student.set_eval(evalEntry.get())
        student.set_reval(revalEntry.get())
        student.set_aod(aodEntry.get())
        student.set_testdate(tDEntry.get())
        student.set_evaldate(eDEntry.get())"""

        student.toString()

    # Submit button
    addButton = Button(text="ADD", command=create())
    addButton.grid(columnspan=2)

    # Start mainloop
    root.mainloop()





