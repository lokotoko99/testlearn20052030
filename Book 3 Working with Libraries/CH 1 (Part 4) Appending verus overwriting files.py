# New name to add with \n to mark end of line.
##new_name = 'Jose Calderón\n'
# Open names.txt in append mode with encoding.
#with open('names.txt', 'a', encoding = 'utf-8') as f:
    #f.write(new_name) 

with open('names.txt', encoding = 'utf-8') as f:
    print(f.read())

# Using tell() to determine the pointer location

with open('names.txt', encoding ='utf-8') as f:
    # Read first line to get started.
    print(f.tell())
    one_line = f.readline()
    # Keep reading one line at a time until there are no more.
    while one_line:
        print(one_line[:-1], f.tell()) # the -1 is to remove the \n lines
        one_line = f.readline()

with open('names.txt', encoding ='utf-8') as f:
    # Read first line to get started.
    print(f.tell())
    # Keep reading one line at a time until there are no more.
    for one_line in f.readlines():
        print(one_line[:-1], f.tell())

# Moving the pointer with seek()   
# file.seek(position[,whence])