#!/usr/bin/env python

import os, sys, csv
import chardet      #TODO: requirements: chardet-3.0.4
from functions import date_change,calculate_clicks, get_country_code


input_DIR = 'input'
list_DIR = os.listdir(input_DIR)


'''
check if the 'Input' folder is empty
and is it containing hidden .DS_store files
'''

if len(list_DIR) == 0 or (len(list_DIR) == 1 and '.DS_Store' in list_DIR):

    sys.stderr.write('STDERR: Critical error occured. No .csv file was found in "Input" folder,\n'
                     'copy input file in .csv format to this folder and try again.')
    sys.exit()


else:       # search for .csv file in 'Input' folder

    for search_file in list_DIR:

        if not search_file.endswith('.csv'):
            continue    # skip, if it's different file type

        else:

            input_path = os.path.join(input_DIR, search_file)
            break


# detect if the .csv file encoding is utf-8 or other

raw_data = open(input_path, 'rb').read()
encoding = chardet.detect(raw_data)


if encoding['encoding'] == 'utf-8':
    pass

else:
    sys.stderr.write('STDERR: Critical error. This script supports only utf-8 encoded files')
    sys.exit()


'''
Read .csv file with csv reader from standard Python module
make changes in rows to match output standard: 2019-01-21,AFG,919,6
list rows in "input_Rows" list
'''

input_Rows = []

input_CSV = open(input_path, newline='')
input_Reader = csv.reader(input_CSV)

try:
    for row in input_Reader:

        row[0] = date_change(row[0])    # call 'date_change' function, modify 0 column
        row[1] = get_country_code(row[1])   # call 'get_country_code' function, modify 1 column
        row[3] = calculate_clicks(row[2],row[3])     # call 'calculate_clicks' function, modify 3 column
        input_Rows.append(row)      # append modified row into list

except csv.Error as error:
    sys.stderr.write('file {}, line {}: {}'.format(input_path, reader.line_num, error))


input_Rows.sort()   # sort rows lexicographically

for row in input_Rows:
    print(row)