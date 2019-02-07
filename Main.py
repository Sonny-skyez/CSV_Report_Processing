#!/usr/bin/env python

import os, csv, sys
import chardet  # TODO: requirements!
from functions import date_change


input_DIR = 'input'


if len(os.listdir(input_DIR)) == 0:     # check if the 'Input' folder is empty:

    sys.stderr.write('STDERR: Critical error occured. No .csv file was found in "Input" folder,\n'
                     'copy input file in .csv format to this folder and try again.')
    sys.exit()

else:       # search for a .csv file in 'Input' folder

    for search_file in os.listdir(input_DIR):   #TODO uwzglednij DC_store

        if not search_file.endswith('.csv'):
            continue

        else:

            input_filename = os.path.join(input_DIR, search_file)
            break


# read .csv file with csv Python module,
# and list rows in "input_Rows" list.

input_Rows = []
input_CSV = open(input_filename)    #TODO: check if the file is UTF-8
input_Reader = csv.reader(input_CSV)


for row in input_Reader:

    row[0] = date_change(row[0])    # call 'date_change' from 'functions.py' file
    print(row)
    #TODO: change names of states into shortcuts
    #TODO: change percent into clicks