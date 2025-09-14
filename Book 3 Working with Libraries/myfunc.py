

"""
to_date(any_str): Pass in any string(any_str) date in mm/dd/yy or mm/dd/yyy format, and the function sends back a Python datetime.date that
you can use for date calculations.

>> mdy(any_date): Pass in any Python date or datetime, and the function returns a string date formatted in mm/dd/yyyy format for display on the screen.

>>to_cuur(any_num, len): Pass in any Python float or integer number and the function returns a string with a leading dollar sign, commas in thousands places,
and two digits for the pennies. len is an optional number for length. If provided, the return value will be padded on the left with spaces to match the legnth specified.


"""

# Contains custom functions for dates and curency values.

import datetime as dt

def to_date(any_str):
    """Convert mm/dd/yy or mm/dd/yyyy string to datetime.date, or None if invalid date."""
    try:
        if len(any_str) == 10:
            the_date = dt.datetime.strptime(any_str,'%m/%d/%Y').date()
        else:
            the_date = dt.datetime.strptime(any_str,'%m/%d/%y').date()
    except (ValueError, TypeError):
        the_date = None
    return the_date

def mdy(any_date):
    """ Returns a string date in mm/dd/yyyy format. Pass in Python date or string date in mm/dd/yyyy format """
    if type(any_date) == str:
        any_date = to_date(any_date)
    # Make sure a datetime is being forwarded
    if isinstance(any_date,dt.date):
        s_date = f"{any_date:'%m/%d/%Y'}"
    else:
        s_date = "Invalid date"
    return s_date

def to_curr(anynum, len=0):
    """ Returns a number as a string with $ and commas. Length is optional"""
    s = "Invalid amount"
    try:
        x = float(anynum)
    except ValueError:
        x = None
    if isinstance(x,float):
        s = '$' + f"{x:,.2f}"
        if len > 0: 
            s = s.rjust(len)
    return s


