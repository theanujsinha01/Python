"""
int() → Converts to an integer
float() → Converts to a float
str() → Converts to a string
list(), tuple(), set(), etc 
"""
a = "190"
a = int(a)
print(a)
print(type(a)) #Output :<class 'int'>

b = 3
b = float(b)
print(b) #Output :3.0
print(type(b)) #Output :<class 'float'>

c = 1,2,3
c = list(c)
print(c) #Output : [1, 2, 3]
print(type(c)) #Output : <class 'list'>

d = 123456
d = str(d)
print(type(d)) #Output : <class 'str'>



