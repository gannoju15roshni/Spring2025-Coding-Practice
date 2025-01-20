# Decorators are powerful and flexible way to modify or extend the behavior of functions or methods, without changing their actual code.

# A decorator is essentially a fucntion that taskes another function as an argumnet and returns a new function with enhanced fucntionality.

# Decorators are often used in scenariors such as logging, authentication and memorization, allowing us to and additional fucntionality to existing functions or methods in a clean, reusable way.

# Simple Decorator Function:

# def decorator(func):
  
#     def wrapper():
#         print("Before calling the function.")
#         func()
#         print("After calling the function.")
#     return wrapper

# # Applying the decorator to a function
# @decorator

# def greet():

#     print("Hello, World!")

# greet()


# Example

# A higher-order function that takes another function as an argument
def fun(f, x):
    return f(x)

# A simple function to pass
def square(x):
    return x * x

# Using apply_function to apply the square function
res = fun(square, 5)
print(res)



# def decorator_name(func):
#     def wrapper(*args, **kwargs):
#         # Add functionality before the original function call
#         result = func(*args, **kwargs)
#         # Add functionality after the original function call
#         return result
#     return wrapper


# @decorator_name
# def function_to_decorate():
#     # Original function code
#     pass

# 1. decorator_name(func):
# decorator_name: This is the name of the decorator function.
# func: This parameter represents the function being decorated. When you use a decorator, the decorated function is passed to this parameter.
# 2. wrapper(*args, **kwargs):

# wrapper: This is a nested function inside the decorator. It wraps the original function, adding additional functionality.
# *args: This collects any positional arguments passed to the decorated function into a tuple.
# **kwargs: This collects any keyword arguments passed to the decorated function into a dictionary.
# The wrapper function allows the decorator to handle functions with any number and types of arguments.
# 3. @decorator_name:

# This syntax applies the decorator to the function_to_decorate function. It is equivalent to writing function_to_decorate = decorator_name(function_to_decorate).

