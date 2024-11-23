#Unpacking means taking items from a group (like a list or dictionary) and putting each one into its own separate box (variable) easily.

data = (1, 2, 3)
a, b, c = data  # Unpacking the tuple into three variables
print(a, b, c)  # Output: 1 2 3


info = {'name': 'rohit', 'age': 21}
for key, value in info.items():  # Unpacking dictionary items into key and value
    print(key)
    print(value)

print("...........................................")
sequence = ['rohit', 1, 2, 3, 4]

# Unpacking the sequence. 'name' gets the first item, and 'marks' gets the rest.
name, *marks = sequence
print(name)  # Output: rohit

# 'marks' holds the remaining elements of the list (the numbers 1, 2, 3, 4) as a list.
print(marks)  # Output: [1, 2, 3, 4]


print("...........................................")

# items(), keys(), values()
student ={'name':'Anuj','age':22,'grade':'A'}
print(student.items())

for key , value in student.items():
    print(key, value)

print("...........................................")
name, age, grade = student.values()
print(name)
print(age)
print(grade)