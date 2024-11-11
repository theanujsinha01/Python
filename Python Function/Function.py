#function
def greet():# define function
    print('Good Morning')

greet()#call the function
greet()#call the function

# parameter and arguments
def add(x,y):
    print(x+y)

add(4,6)

# return value
def sum(x,y):
    return x+y

ans = sum(2,9)
print(ans)

# Aribitrary function
def Print(*args):
    for i in args:
        print(i)

    
Print(1,2,3,5)

#lambda function , small and one line expression
total = lambda a,b : a+b
print(total(52,54))

# default parameters
def welcome(name='friend'):
    print('welcome',name)

welcome()
welcome('Anuj')

# recursive function : it is concept when function call itself to solve a smaller part of bigger problem
#base case: this is condition that stops the recursion.

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

factorial = fact(4)
print(factorial)

