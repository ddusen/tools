# -*- coding: utf-8 -*-
import csv

def validate_data():

    with open('/home/sdu/MyProject/tools/tools/tianchi/data.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile)

        count = 0
        for index, item in enumerate(spamreader):
            if index > 0:
                del item[0]
                count += reduce(lambda x, y: int(x) + int(y), item)

        if count == 69674110:
            print "VALIDATE DATA SUCCESS!"

def main():
    validate_data()

if __name__ == '__main__':
    main()
