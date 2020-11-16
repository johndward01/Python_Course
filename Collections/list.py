# LISTS
# A list is a collection which is ordered and changeable. Allows duplicate members.

# different ways to manipulate a list
# names = ['John', 'Jay', 'Jack', 'Joe', 'Jeff']
# print(names)
# print(names[0])
# print(names[2:])
# print(names[2:4])


# code that will choose the greatest number in a list
# prices = [10, 20, 30]
# i = 0
# x = 0
# for item in prices:
#     if prices[i] > x:
#         x = prices[i]
#         i += 1
# print(x)

# add something to the list at the end
# names.append('Test')
#
# add something to the list at the beginning
# names.insert('Test')
#
# print(names[len(names) - 1]) #print out the last name of the list
# # similar to Console.WriteLine(names[names.Length - 1])
#
# # deleting an element inside the list at index 5
# del names[5]
# print(names)

# you can concatenate lists in python
# print([1,2,3] + [4,5,6])

# and you are not limited by type
# list_1 = ['a','b','c']
# list_2 = [1,2,3]
# print(list_1 + list_2)

# You can repeat lists like strings
# list = [1,2,3]
# list_3 = list * 3
# print(list_3)

# you can evaluate if something is inside the list or not
# list = [10, 20, 30]
# print(20 in list)

# you can do the same operations as strings
# print(list[2])
# print(list[-2])
# print(list[1:])
#print(len(list))

# Print the unique numbers not the duplicates in a list
# list = [1,2,2,3,5,7,2,3,1]
# distinct = []
# for x in list:
#     if x not in distinct:
#         distinct.append(x)
# print(distinct)

# POPULAR LIST METHODS
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


# 2D LISTS

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix)
# print(matrix[0])
# print(matrix[1][2])

