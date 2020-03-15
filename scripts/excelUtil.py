# -*- coding: utf8 -*-
import xlrd
from xlrd import open_workbook
from xlwt import Workbook
from xlutils.copy import copy

class excelUtil(object):

    path = ""
    
    def init_excel(self,path):
        self.path = path
        rb = open_workbook(self.path)
        self.wb = copy(rb)
        self.s = self.wb.get_sheet(0)       
        self.book = xlrd.open_workbook(self.path)
        

    def write_excel_file(self):
        self.s.write(0,0,'A1')
        self.s.write(0,1,'A2')
        self.s.write(0,2,'A3')
        self.s.write(0,3,'A4')

        self.s.write(1,0,'B1')
        self.s.write(1,1,'B2')
        self.s.write(1,2,'B3')
        self.s.write(1,3,'B4')

        self.wb.save(self.path)
        print ("Excel write Done!!!")

    def read_excel_file(self):
        # print number of sheets
        print (self.book.nsheets)
        # print sheet names
        print (self.book.sheet_names())
        # get the first worksheet
        first_sheet = self.book.sheet_by_index(0)
        # read a row
        print (first_sheet.row_values(0))
        print (first_sheet.row_values(1))

        # read a cell
        cell = first_sheet.cell(0,0)
        print (cell)
        print (cell.value)
        print

        # read a row slice
        cellsA =  first_sheet.row_slice(rowx=0,start_colx=0,end_colx=4)
        cellsB =  first_sheet.row_slice(rowx=1,start_colx=0,end_colx=4)

        #read all row A values
        for cell in cellsA:
            print (cell.value)

        #read all row B values
        for cell in cellsB:
            print (cell.value)

        return ("read success")

#excel = exelUtil("C:/Users/fitim/AppData/Local/Programs/Python/Python37/test.xls")
#excel.writeExcelFile()
#excel.readExcelFile()
