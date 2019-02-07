#!/usr/bin/env python

import os, csv, sys
from functions import date_change


input_DIR = 'input'


# search for a .csv file in 'Input' folder

if len(os.listdir(input_DIR)) == 0:

    print('File not found'
          'please try again')


for search_file in os.listdir(input_DIR):

    if not search_file.endswith('.csv'):
        continue

    else:
        input_filename = os.path.join(input_DIR, search_file)
        break


# read .csv file with csv Python module:


input_Rows = []
input_CSV = open(input_filename)
input_Reader = csv.reader(input_CSV)


for row in input_Reader:

    date = date_change(row[0])  # call 'date_change' from 'functions.py' file
