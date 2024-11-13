#try-except, else, finally


try:
    print(1/0)
except Exception as e:
    print("You can not divide by zero", e)
