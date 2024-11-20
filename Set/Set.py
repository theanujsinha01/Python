#  sets in Python are mutable. You can add or remove items from a set after creating it. But the items inside a set must be immutable, like numbers, strings, or tuples
# unique : does not contain duplicates

myset = {'apple', 56, 3.4, True}
print(myset) #unordered 

# add item in set
myset.add('mango')
print(myset)

# remove item in set
myset.remove('apple')
print(myset)

#length of set
print(len(myset))

# clear the set
myset.clear()
print(myset)