import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "Birmingham"
}
print(x)

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# Format the Result
# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
#
# The json.dumps() method has parameters to make it easier to read the result:

x_formatted = json.dumps(x, indent=4)
print(x_formatted)

# Order the Result
# The json.dumps() method has parameters to order the keys in the result:
#
# Example
# Use the sort_keys parameter to specify if the result should be sorted or not:
#
print(json.dumps(x, indent=4, sort_keys=True))