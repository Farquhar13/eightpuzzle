import sys
import copy

class MyClass:
    state = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]

a = MyClass
b = copy.deepcopy(a)
print b.state
b.state[0][2] = '9'
print b.state
print a.state