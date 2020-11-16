# FUNCTIONS
# In Python a function is defined using the def keyword:

# Creating the function
# def greeting(first_name, last_name):
#     print(f"Hello, {first_name} {last_name}!")

# Calling the function
# greeting("John", "Ward")


# If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
# def add(*args):
#     result = 0
#     for x in args:
#         result += x
#     print(result)
# add(1,2,3,4,56)

# KEYWORD ARGUMENTS -> **kwargs

# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
# def print_coordinates(x,y):
#     print(f"({x},{y})")
#
# print_coordinates(y = 2, x = 4)

# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#
# This way the function will receive a dictionary of arguments,
# and can access the items accordingly:

# def my_function(**kwargs):
#     print("arg1 is: " + kwargs["arg1"])
#
# my_function(arg2 = "second argument", arg1 = "first argument")

# Default Parameter Value
# If no arguments are given then the default parameter will be used
# def my_function(country = "The United States"):
#     print("I am from " + country)
# my_function()
# my_function("Germany")
# my_function("Some random place")

