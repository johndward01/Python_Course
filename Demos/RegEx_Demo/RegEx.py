import re

# Character	Description	Example	Try it
# []	A set of characters	"[a-m]"
# \	Signals a special sequence (can also be used to escape special characters)	"\d"
# .	Any character (except newline character)	"he..o"
# ^	Starts with	"^hello"
# $	Ends with	"world$"
# *	Zero or more occurrences	"aix*"
# +	One or more occurrences	"aix+"
# {}	Exactly the specified number of occurrences	"al{2}"
# |	Either or	"falls|stays"
# ()	Capture and group

# Sets
# A set is a set of characters inside a pair of square brackets [] with a special meaning:
#
# Set	Description	Try it
# [arn]	Returns a match where one of the specified characters (a, r, or n) are present
# [a-n]	Returns a match for any lower case character, alphabetically between a and n
# [^arn]	Returns a match for any character EXCEPT a, r, and n
# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
# [0-9]	Returns a match for any digit between 0 and 9
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
# [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

text = f'Lorem ipsum dolor sit amet, ' \
       f'consectetur adipiscing elit, ' \
       f'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.' \
       f'Ut enim ad minim veniam, ' \
       f'quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ' \
       f'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. ' \
       f'Excepteur sint occaecat cupidatat non proident, ' \
       f'sunt in culpa qui officia deserunt mollit anim id est laborum.'

# RegEx Functions
# The re module offers a set of functions that allows us to search a string for a match:
#
# Function	Description
# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string

# The findall() function returns a list containing all matches.
# x = re.findall("or", text)
# print(x)
#
# # The search() function searches the string for a match, and returns a Match object if there is a match.
# #
# # If there is more than one match, only the first occurrence of the match will be returned:
# x = re.search(" ", text)
# print("The first white-space character is located in position:", x.start())
#
# # The split() function returns a list where the string has been split at each match:
# print(re.split(" ", text))
# print(re.split(" ", text, 1))
#
# # The sub() function replaces the matches with the text of your choice:
# #
# print(re.sub(" ", "__", text))
# # control the number of replacements with the count parameter
# print(re.sub(" ", "__", text, 2))

# MATCH OBJECT
# The search result is a match object in Python.
# The Match object has properties and methods used to retrieve information about the search, and the result:
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match
x = re.search(r"\bD\w+", text)
print(x.span())
print(x.string)
print(x.group())