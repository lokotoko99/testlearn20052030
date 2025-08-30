# Unmasking Anonymous Functions

"""Python supports anonymous functions, also called lambda functions"""

names = ['Adams', 'Ma', 'diMeola','Zandusky']
namestest = ['Adams', 'Ma', 'diMeola','Zandusky']
numbers = [50,100,200]
names.sort()
print(names)

def lowercaseof(anystring):
    """Converts string to all lowercase"""
    return [x.lower() for x in anystring]

print(lowercaseof(names))


def LOWERCASE(anystring):
    return anystring.lower()

#print(lowercaseof('JAPAN'))

print(LOWERCASE('JAPAN'))

names.sort(key = LOWERCASE)
print(names)


namestest.sort(key = lambda s: s.lower())
print(namestest)

currency = lambda n: f"${n:,.2f}"
percent = lambda n: f"{n:.2%}"

print(currency((99)))


# Show number in currency format.
def currency2 (n, w = 15):
    """Show in currency format, width = 15 or width of your choosing"""
    s = f"${n:,.2f}"
    # Pad left of output with spaces to width of w.
    return s.rjust(w)

# Show number in percent format.
def percent2(n, w = 15):
    """ Show in percent format, width = 15 or width of your choosing"""
    # Show number in percent fomrat.
    s = f"{n:.1%}"
    # Pad left of output with spaces to width of w.
    return s.rjust(w)

print(currency2(99))
print(percent2(99))


"""
So there you have it: the ability to create your own custom functions in Python. In
real life, any time you find that you need access to the same chunk of code — the
same bit of logic — over and over again in your app, don’t simply copy and paste
that chunk of code over and over. Instead, put the code in a function that you can
call by name. That way, if you decide to change the code, you don’t have to go digging
through your app to find all the places that need changing. Just change it in
the function where it’s all defined in one place.
"""





