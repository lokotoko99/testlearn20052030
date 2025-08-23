# var = open(filename.ext[mode])

f = open('quotes.txt')
filecontents = f.read()
print(filecontents)

f.close()

# ________________ Contextual Syntax
with open('quotes.txt') as f:
    filecontents = f.read()
    print(filecontents)

# The unindented line below is outside the with. . .  block;
print('File is closed: ', f.closed)

with open('happy_pickle.jpg','rb') as f:
    filecontents = f.read()
    print(filecontents)

with open('names.txt','r',encoding = 'utf-8') as f:
    filecontents = f.read()
    print(filecontents)

"""
»»  For a plain-text file (ASCII), you can use r or nothing as the mode.
»»  For a binary file, you must specify b in the mode.
»»  For a text file with fancy characters, you most likely need to open it as a text
    file with encoding set to utf-8 in the open() statement.
"""