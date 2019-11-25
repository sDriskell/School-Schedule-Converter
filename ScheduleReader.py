import xlrd
import pathlib
import datetime
from datetime import date, timedelta
#import Student


class ScheduleReader:
    def __init__(self):
        self.LOC = None
        self.WB = None
        self.SHEET = None
        self.DATE = None
        self.testDate = None

    def setup(self):
        # Global variables for read/write
        self.LOC = pathlib.Path.cwd() / 'TestExcel.xlsx'
        self.WB = xlrd.open_workbook(self.LOC)
        self.SHEET = self.WB.sheet_by_index(0)
        # Float format date
        self.DATE = self.SHEET.cell_value(rowx=1, colx=9)

    def read_sched(self):
        for i in range(i + 1, self.SHEET.ncols):
            self.testDate = self.SHEET.cell_value(1, i) - DATE

            # Test different conditions to determine state
            if self.SHEET.cell_value(1, i) > self.DATE:
                if self.testDate > 45:
                    print("You are over 45 days out.")
                    print(self.testDate)
                elif self.testDate > 30:
                    print("You are over 30 days out.")
                    print(self.testDate)
                elif self.testDate <= 30:
                    print("You are under 30 days out.")
                    print(self.testDate)
            if self.SHEET.cell_value(1, i) <= self.DATE:
                print("You are overdue by: ")
                print(self.testDate)