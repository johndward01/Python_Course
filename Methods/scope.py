# Scope of Variables
# All variables in a program may not be accessible at all locations in that program. This depends on where you have declared a variable.
#
# The scope of a variable determines the portion of the program where you can access a particular identifier. There are two basic scopes of variables in Python −
#
# Global variables
# Local variables
# Global vs. Local variables
# Variables that are defined inside a function body have a local scope, and those defined outside have a global scope.
#
# This means that local variables can be accessed only inside the function in which they are declared,
# whereas global variables can be accessed throughout the program body by all functions.
# When you call a function, the variables declared inside it are brought into scope.

# Example
# total = 0
#
#
# def sum(arg1, arg2):
#     total = arg1 + arg2
#     print("Inside the function local total : ", total)
#     return total
#
#
# #TODO: What is the output of this code?
# sum(10, 20)
# print("Outside the function global total : ", total)
#
# global_variable = 1
#
# def my_function():
#     local_variable = 10
#     def my_nested_function(x):
#         nested_function_variable = local_variable
#         if nested_function_variable is local_variable:
#             print(f"I have access to the local_variable {local_variable}")
#             print(f"Ihave access to the global_variable {global_variable}")

# However I do not have access to the local variables from the global scope only in the function scope
# print(global_variable + local_variable) THROWS AN ERROR

