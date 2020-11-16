# Set is a collection which is unordered and unindexed. No duplicate members.
# Python will automatically order this set below when you print it out
# my_set = {1, 3, 2, 5, 4}
# for x in my_set:
#     print(x)

# run this code multiple times to see how a set is unordered
# my_other_set = {"j", "a", "c", "k"}
# for letter in my_other_set:
#     print(letter)

# check if an element is within the set
# my_set = {"1", "2", "3"}
# x = input("Type the element and I will check if it's inside the set: ")
# if x in my_set:
#     print(f"{x} is in {my_set}")

# You cannot access items is a set by referring to an index or key
# my_set = {"a", "b", "c"}
# print(my_set[1]) # this will cause an error

# To add items to a set use the add() method (it will not be in order)
# my_set = {"abc", "def"}
# my_set.add("ghi")
# print(my_set)

# To add many items to a set use the update() method
# my_set = {"a", "b", "c"}
# my_set.update("ddd", "eee", "fff")
# print(my_set)

# Remove an item from a set use the remove() method
# x = {1, 2, 3, "str"}
# x.remove("str")
# print(x)

# OR use the discard() method (the remove method will raise an error if the item doesn't exist)
# x = {"3", "2", "1", "4"}
# x.discard("5")
# print(x)

# use clear() to empty the set
# my_set = {1,2,3}
# my_set.clear()
# print(my_set)

