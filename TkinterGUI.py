import xlrd
import pathlib
from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk

def display():

    #take in excel sheets location and leverage
    #output Excel sheet
    OutputWorkBook = xlrd.open_workbook(pathlib.Path.cwd() / 'OutputStudents.xlsx')
    outputSheet = OutputWorkBook.sheet_by_index(0)

    # initial Excel sheet
    inputWorkBook = xlrd.open_workbook(pathlib.Path.cwd() / 'TestExcel.xlsx')
    inputSheet = OutputWorkBook.sheet_by_index(0)




    ###---------Tkinter Window---------------------------
    # Create blank window
    root = Tk()

    #window label
    winLabel = Label(root, text="Kylee Driskell's Super Sceduler", bg='#38cfd1')
    winLabel.pack()


    tree = ttk.Treeview(root)
    #
    #("first","last","iep", "eval", "reval", "aod","testdate", "evaldate")

    tree["columns"] = ("first","info")
    #column widths
    #pass

    #
    tree.heading("first", text="First Name")
    tree.heading("info", text="Last Name")
    #tree.heading("iep", text="IEP")
    #tree.heading("eval", text="Eval")
    #tree.heading("reval", text="Reval")
    #tree.heading("aod", text="AOD")
    #tree.heading("testdate", text="Test Date")
    #tree.heading("evaldate", text="Eval Date")


    id = 1  # identifier for student
    for i in range(1, outputSheet.nrows):

        #data to be used as values in treeview
        first = outputSheet.cell_value(rowx=i, colx=1)
        last = outputSheet.cell_value(rowx=i, colx=0)
        aod = outputSheet.cell_value(rowx=i, colx=2)
        #string dates
        iep = inputSheet.cell_value(rowx=i, colx=3)
        meet = inputSheet.cell_value(rowx=i, colx=4)
        eval = inputSheet.cell_value(rowx=i, colx=5)
        reval = inputSheet.cell_value(rowx=i, colx=6)

        # days until dates
        dtIep = outputSheet.cell_value(rowx=i, colx=3)
        dtMeeting = outputSheet.cell_value(rowx=i, colx=4)
        dtEval = outputSheet.cell_value(rowx=i, colx=5)
        dtReval = outputSheet.cell_value(rowx=i, colx=6)



        student = "student{}".format(id)


        # days out logic

        # Student
        if (30 < dtIep < 45) or (30 < dtMeeting < 45) or (30 < dtEval < 45) or (30 < dtReval < 45) :
            tree.insert('', 'end', student, values=(first,last), tags='yellow') # yellow
        elif (dtIep <= 30) or (dtMeeting <= 30) or (dtEval <= 30) or (dtReval <= 30):
            tree.insert('', 'end', student, values=(first,last,'UNDER 30 DAYS!'), tags='red') #red
        else:
            tree.insert('', 'end', student, values=(first,last))


        tree.insert(student, '0', values=('Area of disability:',aod))
        tree.insert(student, '1', values=('IEP:', iep))
        tree.insert(student, '3', values=('Meeting:', meet))
        tree.insert(student, '4', values=('Eval:', eval))
        tree.insert(student, '5', values=('Re-evaluation:', reval))




        # color configuration
        tree.tag_configure('yellow', background='#cfd13f')
        tree.tag_configure('red', background='#9e263a', foreground= 'white' )

        #increment student
        id+=1


    tree.pack()

    #something extra
    load = Image.open("unicorn.png")
    render = ImageTk.PhotoImage(load)

    bottomPanel = Label(root, image=render)
    bottomPanel.pack()





    root.mainloop()

"""
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
"""
