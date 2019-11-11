import xlrd
import pathlib
import datetime
from datetime import date

# Global variables for read/write
LOC = pathlib.Path.cwd() / 'TestExcel.xlsx'
WB = xlrd.open_workbook(LOC)
SHEET = WB.sheet_by_index(0)
DATE = SHEET.cell_value(rowx=1, colx=1)

TODAY = date.today()
print(TODAY)

# Start point; count rows and columns
print(SHEET.cell_value(0, 0))
print(SHEET.nrows)
print(SHEET.ncols)

# Extract first row
for i in range(SHEET.ncols):
    print(SHEET.cell_value(0, i))

# Extract first column
for i in range(SHEET.nrows):
    print(SHEET.cell_value(i, 0))

# Extract particular row value
#datetime = datetime.datetime(*xlrd.xldate_as_tuple(DATE, WB.datemode))
#print(datetime)
# print(SHEET.row_values(1))



