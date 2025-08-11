# Dictionaries  are also called associative arrays in some languages
# They are kind of like Lists, But each item in the list is identified not by position in the list but by a key.

people = {
    'htanaka': 'Haru Tanaka',
    'ppatel': 'Priya Patel',
    'bagarcia': 'Benjamin Alberto Garcia',
    'zmin': 'Zhang Min',
    'afarooqi': 'Ayesha Farooqi',
    'hajackson': 'Hanna Jackson',
    'papatel': 'Pratyush Aarav Patel',
    'hrjackson': 'Henry Jackson'
}

print(people)
print(people['htanaka'])

print(len(people))
print('htanaka' in people)

#another way to look for something is get()
# dictionaryname.get(key)
print(people.get('htanaka',"Not Found"))
print(people['hajackson'])

# dictionaryname[key] = newvalue
people['hajackson'] = "Hanna Jackson-Smith"
print(people['hajackson'])

"""
In real life, the data in a dictionary would probably be stored also in some kind of
external file so that it’s permanent. Additional code would be required to save the
dictionary changes to that external file. But you need to learn these basics before
you get into all of that, so we’ll just forge ahead with dictionaries for now.

"""
peoplex = {
    'Wolverine':'Sharp claws',
    'Storm':'Manipulates weather elements'
}

# dictionaryname.update({key, value})
print(peoplex)

peoplex.update({'Wolverine':'Sharp Claws and super-human strength'})
peoplex.update({"Cyclops":"Laser beam out of eyes"})
print(peoplex)

for x in peoplex.keys():
    print(x + " = " + peoplex[x])

# Looping through dictionary
for x in peoplex:
    print(x)

for x in peoplex:
    print(peoplex[x])

for x in peoplex.keys():
    print(x)

for x in peoplex.values():
    print(x)

for x,y in peoplex.items():
    print(x,y)


"""

Dictionary Methods
Method : What It Does
clear() : Empties the dictionary by removing all keys and values.
copy() : Returns a copy of the dictionary.
fromkeys() : Returns a new copy of the dictionary but with only specified keys and values.
get() : Returns the value of the specified key, or None if it doesn’t exist.
items() : Returns a list of items as a tuple for each key:value pair.
keys() : Returns a list of all the keys in a dictionary.
pop() : Removes the item specified by the key from the dictionary, and returns its value.
popitem() : Removes the last key:value pair.
setdefault() : Returns the value of the specified key. If the key doesn’t exist, inserts the key with the specified value and returns it.
update() : Updates the value of an existing key, or adds a new key:value pair if the specified key isn’t already in the dictionary.
values() : Returns a list of all the values in the dictionary.

"""

