
# Dictionary are used to store key-value pairs.
# A dictionary is defined using curly braces {}. Each key-value pair is separated by a colon : and the pairs are separated by commas.
# The key in a dictionary must be unique. However, the values can be repeated.
# The values in a dictionary can be of any data type.
# they are mutable and can be changed. don't have duplicates.

dict = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(dict)  # Output: {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# Accessing elements in a dictionary
print(dict['name'])  # Output: John
print(dict.get('age'))  # Output: 25

null_dict = {}
print(null_dict)  # Output: {}

# Adding elements to a dictionary
dict['phone'] = '555-5555'
print(dict)  # Output: {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}


# Updating elements in a dictionary
dict['name'] = 'Jane'
print(dict)  # Output: {'name': 'Jane', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}

# Deleting elements in a dictionary
del dict['phone']
print(dict)  # Output: {'name': 'Jane', 'age': 25, 'courses': ['Math', 'CompSci']}

dict.pop('age')
print(dict)  # Output: {'name': 'Jane', 'courses': ['Math', 'CompSci']}

print(len(dict))  # Output: 2

dict.clear()
print(dict)  # Output: {}




# Dictionary methods

# keys() - Returns a list of all keys in the dictionary.
# values() - Returns a list of all values in the dictionary.
# items() - Returns a list of key-value pairs in the dictionary.

dict = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(dict.keys())  # Output: dict_keys(['name', 'age', 'courses'])

print(dict.values())  # Output: dict_values(['John', 25, ['Math', 'CompSci']])
print(dict.items())  # Output: dict_items([('name', 'John'), ('age', 25), ('courses', ['Math', 'CompSci'])])

# Looping through a dictionary
for key in dict:
    print(key)  # Output: name, age, courses

for key, value in dict.items():
    print(key, value)  # Output: name John, age 25, courses ['Math', 'CompSci'] 

# Check if a key exists in a dictionary
print('name' in dict)  # Output: True
print('phone' in dict)  # Output: False

# update() - Updates the dictionary with the specified key-value pairs.
dict2 = {'phone': '555-5555', 'city': 'New York'}
dict.update(dict2)
print(dict)  # Output: {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '555-5555', 'city': 'New York'}

