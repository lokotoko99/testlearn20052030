#Nesting dictionaries [ create a generic products dictionary to contain multiple product dictionaries.and]

products = {
    'RB00111': {'name' : 'Ray-Ban Sunglasses', 'price': 1122.98, 'models' : ['black', 'tortoise']},
    'DWC0317': {'name' : 'Drone with Camera', 'price': 72.95, 'models' : ['white', 'black']},
    'MTS0540': {'name' : 'T-Shirt', 'price': 2.95, 'models' : ['small', 'medium', 'large']},
    'ECD2989': {'name' : 'Echo Dot', 'price': 29.99, 'models' : []}
                
}
#making a header
print(f"{'ID':<9}{'Name':<17}{'Price':>8}{' Models'}")
print("-" * 60)

#Loop through each dictionary in the products dictionary
for x in products.keys():
    # Get the id of one product.
    id = x
    #Get the name of one product.
    name = products[x]['name']
    #Get the unit price of one product and format with $
    unit_price = "$" +f"{products[x]['price']:.2f}"
    # Create and empty string variable named models
    models = ''
    #Loop through the models list and tack onto models
    # one item from the list followed by a comma and a space
    for y in products[x]['models']:
        models += y + ' ,'
    #if the models variable is more than two character sin legnth, peel off the last 2 character (last comma and space)   
    if len(models)>2:
        models = models[:-2]
    else:
    #Otherwise, if no models, show ,none
        models = "<None>"
    #print all the variables with a neat f-string
    print(f"{id:<6} {name:<17} {unit_price:>8} {models}")