import copy
import sys

list = [None]

class MyClass:
    def __init__(self):
        self.one = 1
        self.list = [1, 2, 3]

a = MyClass()
b = copy.deepcopy(a)

print b.list
b.list[2] = 0
print b.list
print a.list

count = 0
while True:
    count = count + 1
    print count
    if count == 10:
        sys.exit()
