import xlrd
from xl2dict import XlToDict

def get_all_data_from_excel_to_dic(FileName, WorksheetName):
    workbook = xlrd.open_workbook(FileName, on_demand = True)
    worksheet = workbook.sheet_by_name(WorksheetName)
    first_row = [] # The row where we stock the name of the column
    for col in range(worksheet.ncols):
        first_row.append( worksheet.cell_value(0,col) )
    # transform the workbook to a list of dictionaries
    DataFromExcel =[]
    for row in range(1, worksheet.nrows):
        colDic = {}
        for col in range(worksheet.ncols):
            colDic[first_row[col]]=worksheet.cell_value(row,col)
        DataFromExcel.append(colDic)
    return DataFromExcel

myxlobject= XlToDict()

a = myxlobject.convert_sheet_to_dict(file_path="C:/Users/fitim/IdeaProjects/PythonProject/PythonProject/scripts/test.xls", sheet="sheet1",
                                 filter_variables_dict={"User Type" : "Admin", "Environment" : "Dev"})

myxlobject.fetch_data_by_column_by_sheet_name(file_path="C:/Users/fitim/IdeaProjects/PythonProject/PythonProject/scripts/test.xls",
                                              sheet_name="sheet1",
                                              filter_variables_dict={"User Type" : "Admin", "Environment" : "Dev"})

print(a)

a = get_all_data_from_excel_to_dic("C:/Users/fitim/IdeaProjects/PythonProject/PythonProject/scripts/test.xls", "sheet1")
print(type(a))
print(a)

