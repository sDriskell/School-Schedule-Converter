import xlrd
import pathlib
import datetime


class Utility:
    def __init__(self):
        self.location = pathlib.Path.cwd() / 'TestExcel.xlsx'
        self.workBook = xlrd.open_workbook(self.location)
        self.sheet = self.workBook.sheet_by_index(0)
        self.currentDate = self.sheet.cell_value(rowx=1, colx=9)

    def read_list(self):
        j = 1
        for j in range(j, self.sheet.nrows):
            i = 0
            print(self.sheet.cell_value(rowx=j, colx=0))
            for i in range(i + 3, self.sheet.ncols):
                test_date = self.sheet.cell_value(j, i) - self.currentDate
                # Test different conditions to determine state
                if self.sheet.cell_value(j, i) > self.currentDate:
                    if test_date > 45:
                        print("You are over 45 days out.")
                        print(test_date)
                    elif test_date > 30:
                        print("You are over 30 days out.")
                        print(test_date)
                    elif test_date <= 30:
                        print("You are under 30 days out.")
                        print(test_date)
                if self.sheet.cell_value(j, i) <= self.currentDate:
                    print("You are overdue by: ")
                    print(test_date)
            print("-----------------------------------------\n")

