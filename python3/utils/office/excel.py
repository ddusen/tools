import xlsxwriter

from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import Workbook
from openpyxl import load_workbook


def write_xlsx(filepath, data):
    #data like this
    # data = (
    #     ['Rent', 1000],
    #     ['Gas',   100],
    #     ['Food',  300],
    #     ['Gym',    50],
    # )

    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook(filepath)
    worksheet = workbook.add_worksheet()

    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0    

    # Iterate over the data and write it out row by row.
    for r_index, r_data in enumerate(data):
        for c_index, c_data in enumerate(r_data):
            worksheet.write(r_index, c_index, c_data)

    workbook.close()


def append_xls(data):
    #data like this
    # data = (
    #     ['Rent', 1000],
    #     ['Gas',   100],
    #     ['Food',  300],
    #     ['Gym',    50],
    # )

    # Create a workbook and add a worksheet.
    try:
        rexcel = open_workbook("inspections.xls") # 用wlrd提供的方法读取一个excel文件
    except Exception as e:
        print("%s\n%s" % (e, "初始化新文件...", ))        
        workbook = Workbook()
        worksheet = workbook.add_sheet('sheet1')
        workbook.save('inspections.xls')
        rexcel = open_workbook("inspections.xls")

    rows = rexcel.sheets()[0].nrows # 用wlrd提供的方法获得现在已有的行数
    excel = copy(rexcel)# 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
    table = excel.get_sheet(0) # 用xlwt对象的方法获得要操作的sheet

    row = rows
    for r_index, r_data in enumerate(data):
        for c_index, c_data in enumerate(r_data):
            table.write(row + r_index, c_index, c_data)# xlwt对象的写方法，参数分别是行、列、值

    excel.save("inspections.xls") # xlwt对象的保存方法，这时便覆盖掉了原来的excel


def read_xlsx(filename):
    wb = load_workbook(filename=filename, read_only=True)
    ws = wb[wb.sheetnames[0]]
    for row in ws.rows:
        for cell in row:
            pass
    

if __name__ == '__main__':
    # filename = '/mnt/f/FileRecv/model.xlsx'
    # filename = '/mnt/f/FileRecv/model2.xlsx'
    # read_xlsx(filename)
    # data = (
    #     ['Rent', 1000],
    #     ['Gas',   100],
    #     ['Food',  300],
    #     ['Gym',    50],
    # )
    # write_xlsx('/home/sdu/Documents/tools/python3/utils/office/test.xlsx', data)
    # append_xls(data)