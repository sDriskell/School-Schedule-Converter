import xlrd
import pathlib
import datetime
from datetime import date, timedelta

# Global variables for read/write
LOC = pathlib.Path.cwd() / 'TestExcel.xlsx'
WB = xlrd.open_workbook(LOC)
SHEET = WB.sheet_by_index(0)
# Float format date
DATE = SHEET.cell_value(rowx=1, colx=9)
#print(DATE)

# String format date
#TODAY = date.today()
#print(TODAY)

# Start point; count rows and columns
#print(SHEET.cell_value(0, 0))
#print(SHEET.nrows)
#print(SHEET.ncols)

# Extract first row
#for i in range(SHEET.ncols):
    #print(SHEET.cell_value(0, i))

# Extract first column
#for i in range(SHEET.nrows):
   # print(SHEET.cell_value(i, 0))

#print(SHEET.row_values(1))

DATE_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(DATE, WB.datemode))
#print(DATE_as_datetime)


# Compare rows to current date
# +1 tells it to skip text block
#j = 1
#print(SHEET.nrows)
#for j in range(j, SHEET.nrows + 1):
    #print(j)
    #poop = SHEET.ncols
    #for i in range(i + 1, poop):
        #testDate = SHEET.cell_value(j, i) - DATE
        # Test different conditions to determine state
        #if SHEET.cell_value(j, i) > DATE:
            #if testDate > 45:
                #print("You are over 45 days out.")
                #print(testDate)
            #elif testDate > 30:
                #print("You are over 30 days out.")
                #print(testDate)
            #elif testDate <= 30:
                #print("You are under 30 days out.")
                #print(testDate)
        #if SHEET.cell_value(j, i) <= DATE:
            #print("You are overdue by: ")
            #print(testDate)



print(SHEET.nrows)
print(SHEET.ncols)

j = 1
print(SHEET.nrows)
for j in range(j, SHEET.nrows):
    i = 0
    for i in range(i + 3, SHEET.ncols):
        testDate = SHEET.cell_value(j, i) - DATE
        # Test different conditions to determine state
        if SHEET.cell_value(j, i) > DATE:
            if testDate > 45:
                print("You are over 45 days out.")
                print(testDate)
            elif testDate > 30:
                print("You are over 30 days out.")
                print(testDate)
            elif testDate <= 30:
                print("You are under 30 days out.")
                print(testDate)
        if SHEET.cell_value(j, i) <= DATE:
            print("You are overdue by: ")
            print(testDate)
    print("-----------------------------------------\n")