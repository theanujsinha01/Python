
# Tuples are immutable. This means that you cannot change the values in a tuple.
# A tuple is defined using parentheses () and elements are separated by commas.

tup = (1, 2, 3, 4, 5)
print(tup)  # Output: (1, 2, 3, 4, 5)

# A tuple can have elements of different data types.
tup = (1, 'a', 2.5, 'hello') # Output: (1, 'a', 2.5, 'hello')

print(tup[0])  # Output: 1
print(tup[1])  # Output: a


# Tuple methods
# count() - Returns the number of times a specified value occurs in a tuple.
# index() - Searches the tuple for a specified value and returns the position of where it was found.

tup = (1, 2, 3, 4, 5, 1, 1)
print(tup.count(1))  # Output: 3
print(tup.index(5))  # Output: 4


