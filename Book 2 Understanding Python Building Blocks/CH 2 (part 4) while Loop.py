"""
while condition:
    do this...
    do this...
do this when the loop is done
"""
import random

counter = 1
while counter < 91:
    print(str(counter) + "=" + chr(counter))
    counter += 1
print("all done")

import random
print("Odd numbers")
counter = 0
while counter < 10:
    # Get a random number
    number = random.randint(1,999)
    if int(number / 2) == number /2:
        # If its an even number, dont print it.
        continue
    #otherwise, if its an odd, print it and increment the counter.
    print(number)
    counter += 1
print("Loop is compelte")


counter = 0
while counter < 10:
    # Get a random number
    number = random.randint(1,999)
    if int(number / 2) == number /2:
        # If its an even number, dont print it.
        continue
    #otherwise, if its an odd, print it and increment the counter.
    print(number)
    counter += 1
print("Loop is compelte")


print("Numbers that aren't evenly divisible by 5")

counter = 0
while counter < 10:
# Get a random number
    number = random.randint(1,999)
    if int(number / 5) == number / 5:
# If it's evenly divisible by 5, bail out.
        break
# Otherwise, print it and keep going for a while.
    print(number)
# Increment the loop counter.
    counter += 1
print("Loop is done")