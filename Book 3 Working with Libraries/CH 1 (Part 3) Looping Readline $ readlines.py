with open('quotes.txt') as f:
    filecontents= f.read()
    print(filecontents)

# Returns as a list

with open('quotes.txt') as f:
    filecontents = f.readlines()
    print(filecontents)

# Returns as a stringg
with open('quotes.txt') as f:
    filecontents = f.readline()
    print(filecontents)    

with open('quotes.txt') as f:
    # Reads in all lines first, then loops through
    for one_line in f.readlines():
        print(one_line,end="")

with open('quotes.txt') as f:
    # Reads in all lines first, then loops through.
    # Count each line starting at zero.
    for one_line in enumerate(f.readlines()):
        # If counter is even number, print with no extra newline
        if one_line[0] % 2 == 0:
            print(one_line[1], end='')
        # Otherwise print a couple spaces and an extra newline.
        else:
            print(' ' + one_line[1])