#!/usr/bin/env python

# Main script file for CSV Report Processing

# input_path = '/Users/chrisbrown/PycharmProjects/Internship/CSV_Report_Processing/input.csv'
#
# with open(input_path) as input:
#
#     for line in input:
#
#         print(line)


# search for a .csv file in 'Input' folder

import os, csv


input_DIR = 'input'


# search for a .csv file in 'Input' folder

for search_file in os.listdir(input_DIR):

    if not search_file.endswith('.csv'):
        continue

    else:
        input_filename = search_file
        break

print(input_filename)

# read .csv file with csv Python module:

input_Rows = []
input_CSV = open(input_filename)
input_Reader = csv.reader(input_CSV)
for