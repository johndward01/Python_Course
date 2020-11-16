# A date in Python is not a data type of its own,
# but we can import a module named datetime to work with dates as date objects.

import datetime

now = datetime.datetime.now()
print(now)

# 2020-11-13 14:58:01.175028
# The date contains year, month, day, hour, minute, second, and microsecond.
#
# The datetime module has many methods to return information about the date object.2020-11-13 14:49:42.736274
# The date contains year, month, day, hour, minute, second, and microsecond.
#
# The datetime module has many methods to return information about the date object.

# CREATING DATE OBJECTS
# To create a date, we can use the datetime() class (constructor) of the datetime module.
#
# The datetime() class requires three parameters to create a date: year, month, day.

my_date_object = datetime.datetime(2020, 11, 13)
print(my_date_object)

# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone),
# but they are optional, and has a default value of 0, (None for timezone).

# FORMATTING THE DATETIME OBJECT
# The datetime object has a method for formatting date objects into readable strings.
#
# The method is called strftime(), and takes one parameter, format,
# to specify the format of the returned string:

month_name_full = datetime.datetime(2020, 11, 13)
print(month_name_full.strftime("%B"))
# https://docs.python.org/3/library/datetime.html

