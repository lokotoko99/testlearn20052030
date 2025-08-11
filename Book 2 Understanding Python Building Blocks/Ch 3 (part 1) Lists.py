students = ["Joey","Vince","Michelle"]
print(students)
#print(students[1])

for x in students:
    if x == "Vince":
        print("Has Vince")


has_vince = "Vince" in students
print(has_vince)

print(len(students))

students.append("Goober")
print(students)

# lil code to add to list but if already there won't add it

new_student = "Goober"
# add student_name but only if not already int he list.
if new_student in students:
    print(new_student + " Already in List")
else:
    students.append(new_student)
    print(new_student + " added to the list")

print(students)

#Positional Inserting an item into a list

students.insert(0,"Ali")
print(students)

#Changing an item ina  list
students[2]="Vincent"
print(students)

boxers = ["Manny","Floyd"]

students.extend(boxers)

print(students)

#Removing from a list of strings
letters = ["Z","A","B","C","D","E","F","Z","Z"]
letters.remove("Z")
print(letters)

letters2 = ["A","A","A","B","C"]

while "A" in letters2:
    letters2.remove("A")
print(letters2)

#Using .pop()
letters3 =["Z","O","O","M","E","R"]
#Remove the first item.
first_removed = letters3.pop(0)
last_removed = letters3.pop()

print(letters3)

print(first_removed + " and " + last_removed + " were removed")


# del letters :deletes the entire list
# letters.clear()  :clears the list.

o_count = letters3.count("O")
print(o_count)


"""
When trying to combine numbers and strings to form a message, you have to convert
the numbers to strings using the str() function. Otherwise, you get an error
that reads something like can only concatenate str (not "int") to str. In
that message, int is short for integer and str is short for string.

"""

school_grades = ["A","B","B","B","D","F","F","C","C","C","C"]

look_for = "C"

if look_for in school_grades:
    print(look_for + " is in index " + str(school_grades.index(look_for)))
else:
    print(look_for + " is not in index")


dbz_chars =  ["Goku","Bulma","Vegeta","Krillin","Yamcha","Master Roshi"]
numbers = [100,2,5,7,5,200,0]
dbz_chars.sort()    
numbers.sort()

print(dbz_chars)
print(numbers)

"""
If your list contains strings with a mixture of uppercase and lowercase
letters, and if the results of the sort don’t look right, try replacing .sort() with
.sort(key=lambda s: s.lower()) and then running the code again. See Book 2,
Chapter 5 if you’re curious about the details.

"""

import datetime as dt

datelist = []
datelist.append(dt.date(2025,1,31))
datelist.append(dt.date(2027,5,31))
datelist.append(dt.date(2023,12,31))
datelist.append(dt.date(2022,12,31))

#sorting

datelist.sort()

#reversing

print(datelist)
datelist.sort(reverse = True)

for x in datelist:
    print(x)

for x in datelist:
    print(f"{x:%m/%d/%Y}")

#names.reverse() just reverses the list

# .copy() just copies the list



