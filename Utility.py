import xlrd
import pathlib
import datetime
import xlsxwriter


class Utility:
    def __init__(self):
        self.location = pathlib.Path.cwd() / 'TestExcel.xlsx'
        self.workBook = xlrd.open_workbook(self.location)
        self.sheet = self.workBook.sheet_by_index(0)

        self.currentDate = self.sheet.cell_value(rowx=1, colx=9)
        self.countList =[[0] * self.sheet.ncols for i in range(self.sheet.nrows)]
        self.nameList = [[""] * 3 for i in range(self.sheet.nrows)]

    def read_list(self):
        j = 1
        for j in range(j, self.sheet.nrows):
            i = 0
            print(self.sheet.cell_value(rowx=j, colx=0))
            for i in range(i + 3, self.sheet.ncols):
                test_date = self.sheet.cell_value(j, i) - self.currentDate
                self.countList[j][i] = test_date
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
        self.countList.pop(0)
        return self.countList

    def write_list(self):
        workbook = xlsxwriter.Workbook('Expenses01.xlsx')
        worksheet = workbook.add_worksheet()

        expenses = (
            ['Rent', 1000],
            ['Gas',   100],
            ['Food',  300],
            ['Gym',    50],
        )

        row = 0
        col = 0

        for item, cost in expenses:
            worksheet.write(row, col,     item)
            worksheet.write(row, col + 1, cost)
            row += 1

        worksheet.write(row, 0, 'Total')
        worksheet.write(row, 1, '=SUM(B1:B4)')
        workbook.close()

    def read_names(self):
        j = 1
        for j in range(j, self.sheet.nrows):
            i = 0
            for i in range(i, 3):
                sheet_name = self.sheet.cell_value(j, i)
                self.nameList[j][i] = sheet_name
        self.nameList.pop(0)
        return self.nameList


