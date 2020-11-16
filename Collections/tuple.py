# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# essentially.. tuples are list that cannot change

coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# This line is called UNPACKING and is shorthand for the above code
x, y, z = coordinates

#

# Once a tuple has been created it CANNOT be changed
# However, we can change the tuple to a list, then convert it back to a tuple
# x = (1,2,3)
# y = list(x)
# y[1] = "apple"
# x = tuple(y)
# print(x)

# To create a tuple with only one item,
# you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
# correct_tuple = (1,)
# incorrect_tuple = (1)

# print(type(correct_tuple))
# print(type(incorrect_tuple))

# DELETE TUPLE
# my_tuple = (1,2,3)
# del my_tuple
# print(my_tuple) # this will cause an error bc we deleted the tuple

# Join 2 Tuples
# tuple1 = (1,2,3)
# tuple2 = (4,5,6)
# tuple3 = tuple1 + tuple2
# print(tuple3)

# using the tuple Constructor
# my_list = [1,2,3]
# my_tuple = tuple(my_list)
# print(type(my_tuple))

# you need double parentheses when using the tuple constructor => tuple()
# #my_tuple = tuple(1,2,3) # THIS WILL CAUSE AN ERROR!!!
# my_tuple = tuple((1,2,3)) # THIS IS CORRECT
# print(type(my_tuple))





