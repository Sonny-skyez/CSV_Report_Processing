#!/usr/bin/env python

import os, csv
from .Functions.py import date_change


input_DIR = 'input'


# search for a .csv file in 'Input' folder

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
    date_change(row[0])