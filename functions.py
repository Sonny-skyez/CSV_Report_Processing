# file with functions used in Main.py


def date_change(date):

    # this function will create a new date in expected output format;
    # example: 01/21/2019 to 2019-01-21
    new_date = date.split('/')
    new_date.insert(0, new_date.pop(-1))    # change position of the year to 0 position in list
    new_date = '-'.join(new_date)   # create 2019-01-21 format

    return new_date


def calculate_clicks(impress, CTR):

    # this function will calculate number of clicks
    # from CTR (Click To impression Rate)
    a = float(CTR[:-1])
    b = float(impress)
    clicks = b * (a/100)

    return round(clicks, 2)