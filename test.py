
list = [None]

class MyClass:
    def __init__(self):
        self.one = 1
        print "printing from class"

class LowerClass(MyClass):
    def __init__(self, parent):
        self.one = parent.one

higher = MyClass()
lower = LowerClass(higher)
print "higher", higher.one
print "lower:", lower.one
lower.one = 2
print "higher", higher.one
print "lower:", lower.one

min = None



