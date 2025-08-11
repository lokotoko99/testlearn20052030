# A Tuple is basically an immutable list and has round brackets in it (Tuple)

# i.e prices =(29.95, 9.98, 4.95, 79.98, 2.95)

prices = (29.95, 9.98, 4.95, 79.98, 2.95)
#prices.append(200)

print(prices)


# A Set has no set order and none of the items get index numbers and they use {} curly brackets {Curly}
# A set can't contain more than one instance of a value

sample_set = {10,20,30}

sample_set.add(40)
sample_set.add(30)
sample_set.update([100,200])
print(sample_set)

# we can do .copy() on sets too

"""
Lists and tuples are two of the most commonly used Python data structures. Sets
don’t seem to get as much play as the other two, but it’s good to know about them.
A fourth — and widely used — Python data structure is the dictionary, which you
learn about in the next chapter.
"""