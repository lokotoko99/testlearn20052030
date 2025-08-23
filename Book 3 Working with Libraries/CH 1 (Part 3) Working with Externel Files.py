with open('quotes.txt') as f:
    filecontents= f.read()
    print(filecontents)

# Returns as a list

with open('quotes.txt') as f:
    filecontents = f.readlines()
    print(filecontents)


# Returns as a string
with open('quotes.txt') as f:
    filecontents = f.readline()
    print(filecontents)    