# Using list comprehension


# List comprehension is really just an alternative syntax for working with lists. It's mainly used to create a new list from an existing list.
#basically making a new list from an existing list

# new_list =[expression for item in iterable if condition]

simple_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]
same_numbers = [number for number in simple_numbers]
print(same_numbers)

# Even numbers only in this list
even_numbers = [number for number in simple_numbers if number % 2 == 0]
print(even_numbers)

#Odd numbers only in this list:
odd_numbers =[number for number in simple_numbers if number % 2 != 0]
print(odd_numbers)

# All numbers squared:
squared_numbers = [number**2 for number in simple_numbers]
print(squared_numbers)



