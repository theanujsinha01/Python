# reading from a file
f = open(r"C:\Users\thean\OneDrive\Desktop\Skills\Python\File Input Output\test.txt", "r")

data = f.read()
print(data)
print(type(data))
f.close()


# writing to a file
f = open(r"C:\Users\thean\OneDrive\Desktop\Skills\Python\File Input Output\test.txt", "w")

f.write("Hello World")
f.close()


# appending to a file
f = open(r"C:\Users\thean\OneDrive\Desktop\Skills\Python\File Input Output\test.txt", "a")

f.write("\nMachine Learning")
f.close()


# deleting a file
import os
os.remove(r"C:\Users\thean\OneDrive\Desktop\Skills\Python\File Input Output\test.txt")




