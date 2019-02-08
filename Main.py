#!/usr/bin/env python

'''CSV Report Processing

This script is intended to read CSV input file from current working
directory and write proper report file aggregated by date
and country code.

Example input line:

    01/21/2019,Mandiana,883,0.38%

Example output line:

    2019-01-21,GIN,883,3

Scripts supports only UTF-8 encoded .csv files (without BOM).
Author:     Krzysztof Brymer'''


import os, sys, csv
import chardet
from functions import date_change, get_country_code, calculate_clicks


'''Search in current working directory for .csv file.
If found nothing: wrote proper error to Stderr.'''


list_DIR = os.listdir('.')    # list files in CWD
input_path = ''

print('Searching for a .csv input file in current directory.')


for search_file in list_DIR:

    if not search_file.endswith('.csv'):
        continue    # skip, if it's different file type

    elif search_file.endswith('.csv'):

        print('{} file has been found.'.format(search_file))
        input_path = search_file
        break

if len(input_path) == 0:
    sys.stderr.write('STDERR: Critical error. No .csv file was found in working directory.\n'
                     'Copy input file in .csv format to this directory and try again.\n')
    sys.exit()

else:
    pass


'''Detect if the .csv file encoding is utf-8 or other.
If file is encoded in other encoding e.g utf-16 then
write proper error into Stderr '''


print('Detecting {} file encoding.'.format(input_path))

raw_data = open(input_path, 'rb').read()
encoding = chardet.detect(raw_data)


if encoding['encoding'] == 'utf-8':
    print('Detection succeeded. File encoding format is {}.'.format(encoding['encoding']))
    pass

else:
    sys.stderr.write('STDERR: Critical error. This script supports only utf-8 encoded files')
    sys.exit()


'''Read .csv file with csv reader from standard Python module,
make changes in rows to match output standard: 2019-01-21,AFG,919,6
List rows lexicographically in "input_Rows" list'''


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


'''Sort lexicographically rows in input_Rows list and
write output.csv file using csv writer from Python standard library,
use lineterminator to create Unix line endings.'''


input_Rows.sort()   # sort rows lexicographically


# create 'output' dir in CWD and create file path

output_DIR = 'output'
os.makedirs(output_DIR, exist_ok=True)
output_path = os.path.join((output_DIR), 'output.csv')


print('Create {} file.\n'.format(output_path))


output_CSV = open(output_path, 'w', newline='', encoding='utf-8')    # create output file in utf-8 encoding
output_Writer = csv.writer(output_CSV, lineterminator='\n')     # make unix line endings


# iterate trough input_Rows modified list
for row in input_Rows:

    output_Writer.writerow(row)

output_CSV.close()  # close output file


# End credits
print(' Writing output file is complete '.center(100, '*'))
print(' Thank you for using my script! '.center(100, '*'))
print(' Krzysztof Brymer '.center(100, '*'))