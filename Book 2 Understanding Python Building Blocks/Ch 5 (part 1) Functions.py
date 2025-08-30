
# If you want to use some (but not all) optional parameters with multiple parameters,
# make sure the optional ones are the last ones entered.

# Below is writing a function so that passing a  parameter is optional.
# def functioname(parametername=defaultvalue):


def hello(fname, lname, datestring): #Practice function
    """ A docstring describing the function"""
    print("Hello! " + fname + ' ' + lname)
    print('The date is ' + datestring)

hello('Alan','Simpson','12/31/2024')


# Remember what ever parameter you want options has to be last in the function
def hello2(fname, lname, datestring=''):
    """ Hello first name and last name"""
    msg = 'Hello ' + fname + ' ' +lname
    if len(datestring) > 0:
        msg += ' The date is ' + datestring
    print(msg)

hello2('mike','joey','10/23/2025')


#Using Key word arguments (Kwargs)

#Pass in literal kwargs (identify each by parameter name)

hello2(datestring='12/31/2024', lname='Simpson', fname ='Alan')

# Pass in Kwargs from variables (identify each by parameter name)
appt_date = '12/30/2019'
last_name = 'Janda'
first_name = 'Kylie'
hello2(datestring=appt_date, lname =last_name, fname=first_name)





