import csv

# Open CSV file with UTF-8 encoding, don't read in new line characters.
with open('namedata.csv', encoding = 'utf-8', newline ='') as f:
    # reader = csv.reader(f)
    # Create a CVS row counter and row reader.
    reader = enumerate(csv.reader(f)) #reader() function, which returns an object that can iterate through rows.
    # Loop through one row at a time, i is counter, row is entire row.
    for i,row in reader:
        print(i,row)
        #print(row[0]) #helps get the column selection
print('Done!')

# Converting Strings

# Open CSV file with UTF-8 encoding, don't read in new line characters.
with open('namedata.csv', encoding = 'utf-8', newline ='') as f:
    # reader = csv.reader(f)
    # Create a CVS row counter and row reader.
    reader = enumerate(csv.reader(f)) #reader() function, which returns an object that can iterate through rows.
    # Loop through one row at a time, i is counter, row is entire row.
    for i,row in reader:
        if i > 0:
            try:
                # Whole name split into two at comma
                full_name = row[0].split(',')
                last_name = full_name[0].strip()
                first_name = full_name[1].strip()
                print(first_name, last_name)
            except IndexError:
                full_name = last_name = first_name = ""
            print(first_name, last_name)
print('Done!')

# Converting to integers

with open('namedata.csv', encoding = 'utf-8', newline ='') as f:
    # reader = csv.reader(f)
    # Create a CVS row counter and row reader.
    reader = enumerate(csv.reader(f)) #reader() function, which returns an object that can iterate through rows.
    # Loop through one row at a time, i is counter, row is entire row.
    for i,row in reader:
        if i > 0:
            try:
                # Whole name split into two at comma
                birth_year = int(row[1] or 0)
            except IndexError:
                birth_year = ""
            print(birth_year)
print('Done!')

# Converting to date

#----------------------------------------------------------------------------------------------------------------------------

import datetime as dt

with open('namedata.csv', encoding = 'utf-8', newline ='') as f:
    # reader = csv.reader(f)
    # Create a CVS row counter and row reader.
    reader = enumerate(csv.reader(f)) #reader() function, which returns an object that can iterate through rows.
    # Loop through one row at a time, i is counter, row is entire row.
    for i,row in reader:
        if i > 0:
            try:
                # Whole name split into two at comma
                full_name = row[0].split(',')
                last_name = full_name[0].strip()
                first_name = full_name[1].strip()
            except IndexError:
                full_name = last_name = first_name = ""
            
            # Birth year integer, zero for empty string.
            birth_year = int(row[1] or 0)

            # Date_joined is a date.
            try:
                date_joined = dt.datetime.strptime(row[2], "%m/%d/%Y").date()
            except ValueError:
                date_joined = None # None is python's word for an empty object.


            #if row[3] == 'TRUE':
                #is_active = True
            #else:
                #is_active = False

            # is_active is a Boolean. Convert TRUE to True, anything else to False    
            is_active = True if row[3] == "TRUE" else False
            
            # Balance is a float, zero for empty string.
            str_balance = row[4].replace("$", "").replace(",","").strip()
            balance = float(str_balance or 0)

            print(first_name, last_name,birth_year,date_joined,is_active,balance)            
print('Done!')


""""
USING REGULAR EXPRESSIONS IN PYTHON
Although we assume that you’re not familiar with other programming languages, some
readers will be and may be wondering why we didn’t use a regular expression instead
of the replace() method to remove the dollar sign and comma from balance. Well,
regular expressions aren’t built into Python. So if you want to use them, you need to
put from re import sub near the top of your code. The re module provides support
for regular expressions. The sub() function from that module lets you do that actual
substitution.
from re import sub
Later in the code, you can replace
str_balance = (row[4].replace('$', '').replace(',', '')).strip()
with
str_balance = (sub(r'[\s\$,]', '', row[4])).strip()
This line does the same thing as the original line. It removes the dollar sign, commas,
and any leading and trailing spaces from the fifth column value.

"""