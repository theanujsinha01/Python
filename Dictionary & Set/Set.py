
# set is a collection of unordered, unique elements
# sets are mutable and can be changed
# sets are defined using curly braces {}
# elements are separated by commas
# sets do not have duplicates
# sets can have elements of different data types


nums = {1, 2, 3, 4, 5}
print(nums)  # Output: {1, 2, 3, 4, 5}

null_set = set()
print(null_set)  # Output: set()

# set methods

# add() - Adds an element to the set.
# remove() - Removes the specified element from the set.
# discard() - Removes the specified element from the set.
# pop() - Removes an arbitrary element from the set.
# clear() - Removes all elements from the set.
# union() - Returns a set containing the union of sets.
# intersection() - Returns a set containing the intersection of sets.
# difference() - Returns a set containing the difference of sets.

nums.add(6)
print(nums)  # Output: {1, 2, 3, 4, 5, 6}

nums.remove(6)
print(nums)  # Output: {1, 2, 3, 4, 5}


nums.pop()
print(nums)  # Output: {2, 3, 4, 5}

nums.clear()
print(nums)  # Output: set()

# set operations

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

print(set1.union(set2)) # Output: {1, 2, 3, 4, 5, 6, 7}
print(set1.intersection(set2))  # Output: {4, 5}

print(set1.difference(set2)) # Output: {1, 2, 3}
print(set2.difference(set1)) # Output: {6, 7}

