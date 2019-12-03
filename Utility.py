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
        self.writeName = None
        self.writeDays = None

    def read_list(self):
        j = 1
        for j in range(j, self.sheet.nrows):
            i = 0
            print(self.sheet.cell_value(rowx=j, colx=0))
            for i in range(i + 3, self.sheet.ncols):
                test_date = self.sheet.cell_value(j, i) - self.currentDate
                self.countList[j][i] = test_date
        self.countList.pop(0)

    def read_names(self):
        j = 0
        for j in range(j, self.sheet.nrows):
            i = 0
            for i in range(i, 3):
                sheet_name = self.sheet.cell_value(j, i)
                self.nameList[j][i] = sheet_name
        self.nameList.pop(0)

    def write_list(self):
        write_workbook = xlsxwriter.Workbook('OutputStudents.xlsx')
        write_worksheet = write_workbook.add_worksheet()

        print(self.nameList)
        print(self.countList)

        row = 0
        col = 0

        for d1, d2, d3, d4, d5, d6, d7, d8, d9, date in self.countList:
            write_worksheet.write(row, col + 0, d1)
            write_worksheet.write(row, col + 1, d2)
            write_worksheet.write(row, col + 2, d3)
            write_worksheet.write(row, col + 3, d4)
            write_worksheet.write(row, col + 4, d5)
            write_worksheet.write(row, col + 5, d6)
            write_worksheet.write(row, col + 6, d7)
            write_worksheet.write(row, col + 7, d8)
            write_worksheet.write(row, col + 8, d9)
            row += 1


        row = 0
        col = 0

        for last, first, impair in self.nameList:
            write_worksheet.write(row, col+0, last)
            write_worksheet.write(row, col+1, first)
            write_worksheet.write(row, col+2, impair)
            row += 1


        write_workbook.close()

