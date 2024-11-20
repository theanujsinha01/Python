job = "software Engineer"
print(job)

#charactor in string at index
print(job[0]) # first char
print(job[1])
print(job[2])
print(job[-1]) #last char

#multiline strings
str = """We are learning Python
Python is most powerful program"""
print(str)


# f-strings
# provide a concise and readable way to embed expressions inside string literals. It’s prefixed with the letter f and can contain variables or expressions inside curly braces {}.

name = "Alice"
age = 30

# Using an f-string to format the string
info = f"My name is {name} and I am {age} years old."
print(info)  
# Output: My name is Alice and I am 30 years old.



# A docstring is used to describe the purpose of a function, class, or module. It should be placed immediately after the function definition.

def multiply(a, b):
    """
    This function takes two numbers as input,
    multiplies them, and returns the result.
    """
    return a * b

# Calling the function
result = multiply(4, 5)
print(result)  # Output: 20

# Accessing the docstring
print(multiply.__doc__)  
# Output: This function takes two numbers as input, multiplies them, and returns the result.