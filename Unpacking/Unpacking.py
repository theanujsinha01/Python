#Unpacking means taking items from a group (like a list or dictionary) and putting each one into its own separate box (variable) easily.

data = (1, 2, 3)
a, b, c = data  # Unpacking the tuple into three variables
print(a, b, c)  # Output: 1 2 3


info = {'name': 'rohit', 'age': 21}
for key, value in info.items():  # Unpacking dictionary items into key and value
    print(key)
    print(value)
