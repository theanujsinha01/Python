#Logical operators : Used to combine two or more conditional statement

# and operator
x = 10
print(x<50 and x>1)

# or operator
y = 23
print(y>20 or y<0)

# not operator
z = 10
print(not z>100) # give always oposite

print("...........................................")
#The in and not in operators in Python are used to check for the presence or absence of an element in a sequence (like a string, list, tuple, or dictionary). They return True or False.

fruits = ['apple', 'banana', 'cherry']
print('apple' in fruits)  # Output: True
print('grape' in fruits)  # Output: False

text = "hello world"
print('hello' in text)  # Output: True
print('bye' in text)    # Output: False

info = {'name': 'Anuj', 'age': 21}
print('name' in info)  # Output: True
print('Anuj' in info)  # Output: False (because it checks only keys, not values)


print("...........................................")

# is: Checks if two variables point to the same object.
#is not: Checks if two variables point to different objects. 

# Example with `is`
x = [1, 2, 3]
y = x  # Both point to the same object
print(x is y)  # Output: True

# Example with `is not`
a = [1, 2, 3]
b = [1, 2, 3]  # Different objects with the same value
print(a is not b)  # Output: True
