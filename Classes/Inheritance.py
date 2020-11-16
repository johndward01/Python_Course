# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
class Base_Class:
    is_base_class = True

    def base_or_derived_method(self):
        print("base_class method")


class Derived_Class(Base_Class):
    def derived_method(self):
        print("child_class method")


# BASE CLASS OBJECT
base_class_object = Base_Class()

# CALL THE METHODS
base_class_object.base_or_derived_method()

print() # empty line for clarity

# CHILD CLASS OBJECT
derived_class_object = Derived_Class()

# CALL THE METHODS
derived_class_object.base_or_derived_method()
derived_class_object.derived_method()


# PASS
class Another_Class(Derived_Class):
    pass
x = Another_Class()
x.base_or_derived_method()
x.derived_method()
# using the PASS keyword we can just copy the contents and not add anything additional

# THE __init__() FUNCTION     (also called the constructor)
# if you want to create your own constructor in the derived class,
# then you will have to add a reference to the base class constructor; Otherwise,
# you will break the inheritance hierarchy
# THE self KEYWORD represents the instance of the class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def print_name(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self,fname, lname):
        Person.__init__(self, fname, lname) #base class constructor


s1 = Student(Person)
s1.print_name()
# When we call the printname method we pass s1 as the "self" argument

# SUPER()
# Forces derived class to inherit all methods and properties of base class
class Student02(Person):
    def __init__(self, fname, lname, id):
        super().__init__(fname,lname)

