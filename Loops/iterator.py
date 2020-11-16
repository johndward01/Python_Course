# Making an iterator implemented using a class
# class Count:
#
#     """Iterator that counts upward forever."""
#
#     def __init__(self, start=0):
#         self.num = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         num = self.num
#         self.num += 1
#         return num
#
# # Making an iterator the easy way with generators
# fav_nums = [1, 2, 3, 4, 5, 6]
#
# def square_all(numbers):
#     for n in numbers:
#         yield n**2
# print(square_all(fav_nums))


# EXAMPLE
# def count(start=0):
#     num = start
#     while True:
#         yield num
#         num += 1
#
# for n in count():
#     print(n)
# THIS WILL LOOP FOREVER
# We need something to stop the iteration process

# StopIteration Statement
# The StopIteration statement stops the loop

class MyNums:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

my_object = MyNums()
my_iterator = iter(my_object)

for x in my_iterator:
    print(x)



