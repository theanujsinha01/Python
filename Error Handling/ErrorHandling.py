#try-except, else, finally

#try-except
try:
    print(1/1)
except Exception as e:
    print("You can not divide by zero", e)



#else block and finally block 
try:
    a = 2/1
    b = 2*1
except ZeroDivisionError:
    print("you can not divide by zero")
except NameError:
    print("Name occured")
else:
    print(a)
    print(b)
finally:
    print("try-except ")