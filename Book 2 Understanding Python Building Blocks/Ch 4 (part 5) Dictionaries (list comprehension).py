#data_dict = {key: value for key, value in zip(keys_list, values_list)}

#Simple lists

keys = [1,2,3,4,5]
values = ["First","Second","Third","Fourth","Fifth"]

# Use list comprehension to create a dictionary from lists
data_dict = {key:value for (key, value) in zip(keys, values)}
print(data_dict)