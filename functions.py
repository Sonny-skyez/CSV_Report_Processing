# file with functions used in Main.py

import pycountry, sys   #TODO: requirements


def date_change(date):

    '''This function creates a new date in expected output format
    and detects errors in given "date" parameter.

    Example: MM/DD/YYYY to YYYY-MM-DD'''

    # detect empty 'date' parameter
    if not ''.join(date).strip():
        sys.stderr.write('STDERR: Date not found.\n')

        return 'XXXX-XX-XX'

    else:
        new_date = date.split('/')
        new_date.insert(0, new_date.pop(-1))    # change position of the year to 0 position in list
        new_date = '-'.join(new_date)   # create YYYY-MM-DD format

        return new_date


def get_country_code(name):

    '''This function searches for aplha_3 country code (DEU, POL, GIN)
    by using name of subdivision as a parameter, and detects errors.

    Example: Berlin to DEU'''

    # detect empty 'impress' parameter.
    if not ''.join(name).strip():
        sys.stderr.write('STDERR: Error: subdivision field is empty.\n')
        return 'XXX'

    else:
        for subdiv in list(pycountry.subdivisions):     # iterate trough subdivision list
            if name in subdiv.name:
                code = subdiv.country_code      # code is also alpha_2 code of a country
                country = pycountry.countries.get(alpha_2 = code)
                return country.alpha_3

        return 'XXX'    # if function didn't find nothing, return 'XXX'


def calculate_clicks(impress, CTR):

    '''This function calculate number of clicks from CTR (Click To
     impression Rate) and number of impressions. Also detects errors.

     Example: 916, 0.67% to 6'''

    # detect empty 'impress' parameter.
    if not ''.join(impress).strip():
        sys.stderr.write('STDERR: Error: impressions field is empty.\n'
                         'can not calculate clicks.\n')

        return None

    else:
        try:
            # calculate clicks
            a = float(CTR[:-1])
            b = float(impress)
            clicks = b * (a/100)

            return round(clicks)

        except ValueError as error:
            sys.stderr.write('STDERR: Error calculating clicks, {}\n'.format(error))

            return None