#Set : It is store multiple items in single variable 
# Unchangeable : we can't changed the value of set, but can add or remove items
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