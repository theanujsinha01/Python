
def calc_sum(a, b):
    print("Sum of a and b is: ", a + b)
    

def calc_diff(a, b):
    print("Difference of a and b is: ", a - b)


calc_sum(10, 5) # Output: 15
calc_diff(10, 5) # Output: 5


def greet():
    print("Namste! Welcome to Python Functions")

greet() # Output: Namste! Welcome to Python Functions


# recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
ans = factorial(5) # Output: 120
print("Factorial of 5 is: ", ans)

