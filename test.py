a = [[1,2,3], [4,5,6], [7,8,9]]
b = [[1,2,3], [4,5,6], [7,8,9]]

if a == b:
    print "a and b are equal"


class MyClass:
    def __init__(self):
        self.a = 'a'




my_object = MyClass()
print my_object.a
another_object = my_object
print another_object.a
another_object.a = 'b'
print another_object.a
print my_object.a
