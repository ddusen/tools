#!/usr/bin/python3

import os, sys
import requests
sys.path.append(os.getcwd())

from utils.office.excel import write_xlsx


def get_data():
    return requests.get('http://localhost:8001/api/data').json()


def main():
    # Iterate over the data and write it out row by row.
    # for r_index, r_data in enumerate(data):
    #     for c_index, c_data in enumerate(sorted(r_data.items(), reverse=True)):
    #         worksheet.write(r_index, c_index, c_data[1])
    write_xlsx('/home/sdu/Documents/tools/python3/survey/survey_data.xlsx', get_data().get('data'));


if __name__ == '__main__':
    main()