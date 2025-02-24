# List is a built in data type that stores set of values  and changeable(mutable). Allows duplicate members. It can store different data types.
# In Python lists are written with square brackets.
marks =[88,97,99,85,90]
print(marks) # [88, 97, 99, 85, 90]
print(type(marks)) # <class 'list'>
print(marks[0]) # 88
print(marks[1]) # 97
print(len(marks)) # 5

students = ['John',85,78.9,True]
print(students) # ['John', 85, 78.9, True]
print(students[-1]) # True 

# List Methods
# append() - Adds an element at the end of the list
marks.append(100)
print(marks) # [88, 97, 99, 85, 90, 100]

# insert() - Adds an element at the specified position
marks.insert(1,95)
print(marks) # [88, 95, 97, 99, 85, 90, 100]

# remove() - Removes the first item with the specified value
marks.remove(95)
print(marks) # [88, 97, 99, 85, 90, 100]

# pop() - Removes the element at the specified position
marks.pop(1)
print(marks) # [88, 99, 85, 90, 100]

# clear() - Removes all the elements from the list
marks.clear()
print(marks) # []

# copy() - Returns a copy of the list
marks =[88,97,99,85,90]
marks_copy = marks.copy()
print(marks_copy) # [88, 97, 99, 85, 90]

# count() - Returns the number of elements with the specified value
print(marks.count(99)) # 1

# index() - Returns the index of the first element with the specified value
print(marks.index(99)) # 2

# reverse() - Reverses the order of the list
marks.reverse()
print(marks) # [90, 85, 99, 97, 88]

# sort() - Sorts the list
marks.sort()
print(marks) # [85, 88, 90, 97, 99]


