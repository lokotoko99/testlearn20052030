# Create a generic dictionary for products named product.
product = {
'name': '',
'unit_price': 0,
'taxable': True,
'in_stock': 0,
'models': []
}
# Create a dictionary named DWC001 that has the same keys as product.
DWC001 = dict.fromkeys(product.keys())
# Show what's in the new dictionary.
print(DWC001)

DWC001.setdefault('taxable', True)
DWC001.setdefault('models', [])
DWC001.setdefault('reorder_point', 10)

print("Dictionaries after fromkeys() and setdefault()")
print(DWC001)

# Change the taxble field from None to True [default wont capture the True value]
DWC001['taxable'] = True
#print the dictionary after changing taxable to True
print(DWC001)


