# To make a copy = newdictionaryname = dictionaryname.copy()

# deleting dictionary items
# Define a dictionary named people.
people = {
'htanaka': 'Haru Tanaka',
'zmin': 'Zhang Min',
'afarooqi': 'Ayesha Farooqi',
'akhan' : 'Ali Khan'
}

#show original people dictionary.
print(people)
#remove zmin from the dictionary
del people['zmin']
#show whats in people now
print(people)
minus = people.pop('akhan')
print(people)
print(minus)


product = {
    'name' : 'Ray-Ban Wayfarer Sunglasses',
    'unit_price' : 112.99,
    'taxable' : True,
    'in_stock' : 10,
    'models' : ['Black','Tortoise'],
}

print('Name: ', product['name'])
print('Price: ', product['unit_price'])
print('Taxable: ', product['taxable'])
print('in_stock: ', product['in_stock'])
print('Models:')
for x in product['models']:
    print(" "* 10 + x)





