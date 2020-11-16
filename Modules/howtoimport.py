# below we import the module python.py and use the iterator method
from Loops import iterator

x = iterator.MyNums()
my_iterator = iter(x)

for z in my_iterator:
    print(z)
