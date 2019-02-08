# countries.py

import pycountry


def get_country_code(name):

    # this function is searching for aplha_3 country code (DEU, POL, GIN)
    # by using name of subdivision as a parameter
    for subdiv in list(pycountry.subdivisions):
        if name in subdiv.name:
            code = subdiv.country_code
            country = pycountry.countries.get(alpha_2 = code)
            return country.alpha_3

    return 'XXX'