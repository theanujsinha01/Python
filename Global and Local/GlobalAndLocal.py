# Global Variables:
# Declared outside all functions.
# Accessible throughout the program, including inside functions (if not redefined).

x = 10  # Global variable

def show_global():
    print("Global x:", x)  # Accessing global variable

show_global()
# Output: Global x: 10


# Local Variables:
# Declared inside a function.
# Only accessible within that function.

def show_local():
    y = 20  # Local variable
    print("Local y:", y)

show_local()
# Output: Local y: 20