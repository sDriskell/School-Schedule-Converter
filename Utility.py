# Import read/write and date libraries
import xlrd
import pathlib
import datetime
import xlsxwriter


class Utility:
    def __init__(self):
        # create the global'ish variables to be used
        self.location = pathlib.Path.cwd() / 'TestExcel.xlsx'
        self.workBook = xlrd.open_workbook(self.location)
        self.sheet = self.workBook.sheet_by_index(0)

        self.currentDate = self.sheet.cell_value(rowx=1, colx=9)
        self.countList =[[0] * self.sheet.ncols for i in range(self.sheet.nrows)]
        self.nameList = [[""] * 3 for i in range(self.sheet.nrows)]
        self.writeName = None
        self.writeDays = None

    # scan through list and create new rows with dates converted to days from today's date
    def read_list(self):
        j = 1
        for j in range(j, self.sheet.nrows):
            i = 0
            print(self.sheet.cell_value(rowx=j, colx=0))
            for i in range(i + 3, self.sheet.ncols):
                test_date = self.sheet.cell_value(j, i) - self.currentDate
                self.countList[j][i] = test_date
        # removes header row
        self.countList.pop(0)

    # create columns with student names
    def read_names(self):
        j = 0
        for j in range(j, self.sheet.nrows):
            i = 0
            for i in range(i, 3):
                sheet_name = self.sheet.cell_value(j, i)
                self.nameList[j][i] = sheet_name
        # removes header row
        self.nameList.pop(0)

    def write_list(self):
        write_workbook = xlsxwriter.Workbook('OutputStudents.xlsx')
        write_worksheet = write_workbook.add_worksheet()

        print(self.nameList)
        print(self.countList)

        row = 1
        col = 0

        """Each "d" is a designator for columns to be written in;
        d1-3 are empty, rest are floats"""
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

        row = 1
        col = 0

        # writes names to name columns in export
        for last, first, impair in self.nameList:
            write_worksheet.write(row, col+0, last)
            write_worksheet.write(row, col+1, first)
            write_worksheet.write(row, col+2, impair)
            row += 1

        write_worksheet.write(0, 0, "Last")
        write_worksheet.write(0, 1, "First")
        write_worksheet.write(0, 2, "Area of Disability")
        write_worksheet.write(0, 3, "Individual Education Plan")
        write_worksheet.write(0, 4, "Meeting")
        write_worksheet.write(0, 5, "Evaluation")
        write_worksheet.write(0, 6, "Reevaluation")
        write_worksheet.write(0, 7, "30 Day Test Mark")
        write_worksheet.write(0, 8, "45 Day Meeting Mark")

        write_workbook.close()

