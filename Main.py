#!/usr/bin/env python

import os, sys, csv
import chardet      #TODO: requirements: chardet-3.0.4
from functions import date_change,calculate_clicks, get_country_code


'''
check if the 'Input' folder is empty
and is it containing hidden .DS_Store files
'''

input_DIR = 'input'
list_DIR = os.listdir(input_DIR)


if len(list_DIR) == 0 or (len(list_DIR) == 1 and '.DS_Store' in list_DIR):

    sys.stderr.write('STDERR: Critical error occured. No .csv file was found in "Input" folder,\n'
                     'copy input file in .csv format to this folder and try again.')
    sys.exit()


else:       # search for .csv file in 'Input' folder

    print('Searching for a .csv input file in "Input" folder.')

    for search_file in list_DIR:

        if not search_file.endswith('.csv'):
            continue    # skip, if it's different file type

        else:

            print('{} file has been found.'.format(search_file))
            input_path = os.path.join(input_DIR, search_file)
            break


# detect if the .csv file encoding is utf-8 or other

print('Detecting {} file encoding.'.format(search_file))

raw_data = open(input_path, 'rb').read()
encoding = chardet.detect(raw_data)


if encoding['encoding'] == 'utf-8':
    print('Detection succeeded. File encoding format is {}.'.format(encoding['encoding']))
    pass

else:
    sys.stderr.write('STDERR: Critical error. This script supports only utf-8 encoded files')
    sys.exit()


'''
Read .csv file with csv reader from standard Python module
make changes in rows to match output standard: 2019-01-21,AFG,919,6
list rows in "input_Rows" list
'''

print('Opening .csv file and modifying line by line...')

input_Rows = []

input_CSV = open(input_path, newline='')
input_Reader = csv.reader(input_CSV)

try:
    for row in input_Reader:

        if not ''.join(row).strip():    # handle empty lines errors
            sys.stderr.write('STDERR: empty row, script will continue running.\n')
            continue

        else:
            row[0] = date_change(row[0])    # call 'date_change' function, modify 0 column
            row[1] = get_country_code(row[1])   # call 'get_country_code' function, modify 1 column
            row[3] = calculate_clicks(row[2],row[3])     # call 'calculate_clicks' function, modify 3 column
            input_Rows.append(row)      # append modified row into list

except csv.Error as error:
    sys.stderr.write('file {}, line {}: {}'.format(input_path, input_Reader.line_num, error))


input_CSV.close()   # close input file

print('Reading and modification of .csv file is complete.')


'''
sort lexicographically rows in input_Rows list and
write output.csv file using csv writer from Python standard library,
use liniterminator to create Unix line endings
'''

input_Rows.sort()   # sort rows lexicographically

output_DIR = 'Output'
output_path = os.path.join((output_DIR), 'output.csv')

print('Create {} file.\n'.format(output_path))

output_CSV = open(output_path, 'w', newline='')    # create output file
output_Writer = csv.writer(output_CSV, lineterminator='\n')     # make unix line endings

# iterate trough input_Rows modified list
for row in input_Rows:

    output_Writer.writerow(row)

output_CSV.close()  # close output file

# script end, credits

print(' Writing output file is complete '.center(100, '*'))
print(' Thank you for using my script! '.center(100, '*'))
print(' Krzysztof Brymer '.center(100, '*'))