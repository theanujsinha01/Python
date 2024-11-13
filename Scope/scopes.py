num = 100 #global variable

def changeNum():
    num = 200 #local variable this can not be used outside function
  

changeNum()
print(num)



def number():
    global num  # Declare x as global to modify it within the function
    num = 1000
  

number()
print(num)
