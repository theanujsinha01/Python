# The map() function in Python is used to apply a given function to every item in an iterable (e.g., list, tuple) and returns a map object (which can be converted into a list, tuple, etc.).

# map(function, iterable)
# function: A function to apply to each element.
# iterable: An iterable like a list, tuple, etc.

def square(num):
    return num * num

numbers = [1, 2, 3, 4, 5]
result = map(square, numbers)

print(list(result))  # Output: [1, 4, 9, 16, 25]