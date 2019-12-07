import xlrd

def toDate(rowx, colx):
    workbook = xlrd.open_workbook("TestExcel.xlsx")

    sheet = workbook.sheet_by_index(0)

    # Required variables
    wrongValue = sheet.cell_value(rowx, colx)
    workbook_datemode = workbook.datemode

    y, m, d, h, min, s = xlrd.xldate_as_tuple(wrongValue, workbook_datemode)
    return "{0} - {1} - {2}".format(y, m, d)


