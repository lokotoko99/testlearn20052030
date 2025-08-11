unit_price = 49.95
quantity = 32
sales_tax_rate = 0.065
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax
output = f"""
Subtotal:   ${subtotal:,.2f}
Sales Tax:  ${sales_tax:,.2f}
Total:      ${total:,.2f}
"""

print(output)

### Manipulating Strings####

first_name = "Alan"
middle_init = "C"
last_name = "Simpson"
full_name = first_name + " " + middle_init + " " + last_name
print(full_name)
print(len(full_name))


s = "I love cookies"
print (len(s))
print(s[0:14:2])
print(min(s))
print(max(s))
print(s.index("l"))

"""
TABLE 1-5 Built-In Methods for Python 3 Strings
Method Purpose
s.capitalize() Returns a string with the first letter capitalized and the rest lowercase.
s.count(x[, y[, z]]) Returns the number of times string x appears in string s. Optionally, you can add
y as a starting point and z as an ending point to search a portion of the string.
s.find(x[, y[, z]]) Returns a number indicating the first position at which string x can be found in
string s. Optional y and z parameters allow you to limit the search to a portion
of the string. Returns –1 if none found.
s.index(x[, y[, z]]) Similar to find but raises a “substring not found” error if string x can’t be found
in string y.
s.isalpha() Returns True if s is at least one character long and contains only letters (A–Z or
a–z) and printable Unicode characters.
s.isdecimal() Returns True if s is at least one character long and contains only numeric
characters (0–9).
s.islower() Returns True if s contains letters and all those letters are lowercase.
s.isnumeric() Returns True if s is at least one character long and contains only numeric
characters (0–9).
s.isprintable() Returns True if string s contains only printable characters. Spaces are
considered printable, but newlines and tabs are not.
s.istitle() Returns True if string s contains letters and the first letter of each word is
uppercase followed by lowercase letters.
s.isupper() Returns True if all letters in the string are uppercase.
s.lower() Returns s with all letters converted to lowercase.
s.lstrip() Returns s with any leading whitespace (spaces, tabs, newlines) removed.
s.replace(x, y) Returns a copy of string s with string x replaced by string y.
s.rfind(x[, y[, z]]) Similar to s.find but searches backward from the start of the string. If y and z
are provided, searches backward from position z to position y. Returns –1 if
string x not found.
s.rindex() Same as s.rfind but raises an error if the substring isn’t found.
s.rstrip() Returns string s with any trailing whitespace removed.
s.strip() Returns string s with leading and trailing whitespace removed.
s.swapcase() Returns string s with uppercase letters converted to lowercase and lowercase
letters converted to uppercase.
s.title() Returns string s with the first letter of every word capitalized and all other
letters lowercase.
s.upper() Returns string s with all letters converted to uppercase.
"""



