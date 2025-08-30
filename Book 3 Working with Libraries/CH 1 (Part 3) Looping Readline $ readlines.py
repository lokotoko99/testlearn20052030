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
            print('>' + one_line[1])

with open('quotes.txt') as f:
    for tup in enumerate(f.readlines()):
        print(tup)


"""The while loop continues as long as one_line contains something (i.e., it's not an empty string '').
As long as there are more lines in the file, one_line will contain those lines, and the loop will run."""

with open('quotes.txt') as f:
    one_line = f.readline()
    while one_line:
        print(one_line, end ='') # with end = '' print doesn't add a new line
        one_line = f.readline()

# Store a number to use as a loop counter.
counter = 1
# Open the file.
with open('quotes.txt') as f:
    # Read one line from the file.
    one_line = f.readline()
    # as long as there are lines to read. . .
    while one_line:
        # If the counter is an even number, print a couple spaces.
        if counter % 2 == 0:
            print(' ' + one_line)
        # Otherwise print with no newline at the end.
        else:
            print(one_line, end ='')
        # Increment the counter
        counter += 1
        # Read the next line.
        one_line = f.readline()
