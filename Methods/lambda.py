# LAMBDA
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments but can only have one expression.
# An anonymous function is a function without a name

# Syntax
# lambda arguments : expression
# The expression is executed and the result is returned:

# SYNTAX 1
# my_lambda = lambda x: x + 4
# print(my_lambda(0))
#
# # SYNTAX 2
# print((lambda x: x + 4)(0))

# Example
# Add 10 to argument a, and return the result:
# x = lambda a: a + 10
# print(x(5))


# Lambda functions can take any number of arguments:

# Example
# Multiply argument a with argument b and return the result:
#
# x = lambda a, b: a * b
# print(x(5, 6))

# WHY USE LAMBDA FUNCTIONS?

# The power of lambda is better shown when you use them as
# an anonymous function inside another function.

# Say you have a function definition that takes one argument,
# and that argument will be multiplied with an unknown number:
#
# def myfunc(n):
#   return lambda a : a * n
# Use that function definition to make a function that always doubles the number you send in:
#
# Example
# def myfunction(n):
#     return lambda a: a * n
#
#
# mydoubler = myfunction(2)
#
# print(mydoubler(11))

# This Lambda takes 2 arguments and returns a formatted string
# print_name = lambda first_name, last_name: print(f"Name: {first_name} {last_name}")
# print_name("John", "Ward")

