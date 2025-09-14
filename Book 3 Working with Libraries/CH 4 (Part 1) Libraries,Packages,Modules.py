import csv 

x = 3
print(type(x))

x = 'howdy'
print(type(x))

y = 3.14
print(type(y))

d = True
print(type(d))

print(dir(str)) # gives like a breakdown of what is involved in the class itself if one wants to dig deeper.

print(type(x),x.isalpha(),x.upper(),x.capitalize())

help(str.upper)
help(csv.reader)
help(csv.writer)


import csv
import io

# Use a fake file in memory so we don't have to write a real file
fake_file = io.StringIO()
writer = csv.writer(fake_file)

# Now this works:
help(writer.writerows)
help(str.upper)

from math import pi
print(pi)