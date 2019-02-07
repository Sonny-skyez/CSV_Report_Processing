#!/usr/bin/env python

import os, sys, csv
import chardet      #TODO: requirements: chardet-3.0.4
from functions import date_change


input_DIR = 'input'
list_DIR = os.listdir(input_DIR)


# check if the 'Input' folder is empty
# and is it containing hidden .DS_store files

if len(list_DIR) == 0 or (len(list_DIR) == 1 and '.DS_Store' in list_DIR):

    sys.stderr.write('STDERR: Critical error occured. No .csv file was found in "Input" folder,\n'
                     'copy input file in .csv format to this folder and try again.')
    sys.exit()


else:       # search for a .csv file in 'Input' folder

    for search_file in list_DIR:

        if not search_file.endswith('.csv'):
            continue

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

# read .csv file with csv Python module,
# and list rows in "input_Rows" list.
# input_Rows = []
# input_CSV = open(input_path)
# input_Reader = csv.reader(input_CSV)
#
#
# for row in input_Reader:
#
#     row[0] = date_change(row[0])    # call 'date_change' from 'functions.py' file
#     print(row)
#     #TODO: change names of states into shortcuts
#     #TODO: change percent into clicks