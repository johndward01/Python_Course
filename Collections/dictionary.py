# DICTIONARIES
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# essentially.. it's a list with key value pairs

# customer = {
#     "name": "John",
#     "age": 30,
#     "is_verified": True
# }
# print(customer["name"])

# add a key:value pair to a dictionary
# employee = {
#     "first_name": "Michael",
#     "last_name": "Smith",
#     "date_of_birth": "Jan 10 1990"
# }
# employee["id"] = 10344565
#
# print(employee)

# Asks for your phone number and turns the digits into written words
numbers = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
# list = []
# phone_number = input("Enter your phone number: ")
# for digit in phone_number:
#     list.append(numbers[digit])
# print(list)

# get() method is safer to use than bracket notation numbers[x]
# list = []
# for x in numbers:
#     list.append(numbers.get(x))
# print(list)