#module : single file with .py and this contains all the code like functions, classes and variables

#package : collections of modules , contain sub-package

# built-in module

import math
sqrt = math.sqrt(16)
print(sqrt)

pi = math.pi
print(pi)

import datetime
now = datetime.datetime.now()
print(now)




#create own module and package
from myPackage import calc
ans = calc.mul(3,5)
print(ans)