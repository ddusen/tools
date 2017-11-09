#!/usr/bin/python3

import xlsxwriter


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


def read_xlsx():
    pass


if __name__ == '__main__':
    pass
    # data = (
    #     ['Rent', 1000],
    #     ['Gas',   100],
    #     ['Food',  300],
    #     ['Gym',    50],
    # )
    # write_xlsx('/home/sdu/Documents/tools/python3/utils/office/test.xlsx', data)