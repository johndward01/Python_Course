# print(10 == 10)
# #true
# print(1 > 2)
# #false
# print(0 < 100)
# #true


# the bool() function allows you to evaluate any value, and give you True and False in return

# print(bool("Hello World!"))

# print(bool(10))

# Almost all values are true like javascript only a few are "falsy"
# The following will return False:
# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool(()))
# print(bool([]))
# print(bool({}))
#
# class myclass():
#     def __len__(self):
#         return 0
#
# myobj = myclass()
# print("Fringe example")
# print(bool(myobj))

# Functions can return a boolean too

# def myFunction():
#     return True
#
# if myFunction():
#     print("yes")
# else:
#     print("no")

# Identity operators are used to compare the objects, # not if they are equal,
# but if they are actually the same object, with the same memory location:

# x = ["apple", "banana", "orange"]
# y = ["apple", "banana", "orange"]
# z = x
# print(x is z)
# print(x is y)
# print(x == y)

# Membership operators are used to test if a sequence is presented in an object:
# x = ["apple", "banana", "orange"]
# print("banana" in x)
# print("grape" not in x)

