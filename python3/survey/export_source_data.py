#!/usr/bin/python3

import os, sys
import requests
sys.path.append(os.getcwd())

from utils.office.excel import write_xlsx


def get_data():
    return requests.get('http://localhost:8000/api/data').json()


def main():
    # Iterate over the data and write it out row by row.
    # get_index = lambda x: 0 if k == 'start_at' else 1 if k == 'end_at' else 2 if k == 'phone' else 3 if k == 'city' else 4 if k == 'email' else int(k)+4
    # for r_index, r_data in enumerate(data):
    #     for k in r_data.keys():
    #         worksheet.write(r_index, get_index(k), r_data.get(k))
    write_xlsx('/home/sdu/Documents/tools/python3/survey/survey_data.xlsx', get_data().get('data'));


if __name__ == '__main__':
    main()
