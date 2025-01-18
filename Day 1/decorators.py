# Decorators are powerful and flexible way to modify or extend the behavior of functions or methods, without changing their actual code.

# A decorator is essentially a fucntion that taskes another function as an argumnetb and returns a new function with enhanced fucntionality.

# Decorators are often used in scenariors such as logging, authentication and memorization, allowing us to and additional fucntionality to existing functions or methods in a clean, reusable way.

# Simple Decorator Function:
def decorator(func):
  
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

# Applying the decorator to a function
@decorator

def greet():
    print("Hello, World!")

greet()