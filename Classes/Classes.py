# CLASSES

# Create a class
# class MyClass:
#     first_name = "First Name"

# Create an object
# obj_01 = MyClass()
#
# print(obj_01.first_name)

# THE __init__() FUNCTION
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties,
# or other operations that are necessary to do when the object is being created:
#
# Example
# CREATE A CLASS CALLED PERSON
# use the __init__() function to assign values for name and age:
#
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# p1 = Person("John", 36)
#
# print(p1.name)
# print(p1.age)

# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.
#
# Let us create a method in the Person class:
#
# Example
# Insert a function that prints a greeting, and execute it on the p1 object:
#
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is " + self.name)
#
# p1 = Person("John", 36)
# p1.myfunc()

# EXAMPLE
class TrueCoder:
    def __init__(self, name, age, is_night_class):
        self.name = name
        self.age = age
        self.night_class = True
        self.day_class = not self.night_class

    def status(self, name):
        if name is self.name and self.night_class is True:
            print(f"{self.name} is in the night class")
        else:
            print(f"{self.name} is in the day class")
true_coder01 = TrueCoder("John", 30, True)
true_coder01.status(true_coder01.name)

# SELF
# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.
#
# It does not have to be named self, you can call it whatever you like,
# but it has to be the first parameter of any function in the class:

# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age
#
#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
#
# p1 = Person("John", 36)
# p1.myfunc()

