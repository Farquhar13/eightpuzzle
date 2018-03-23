import copy
import sys

class myClass:
    def __init__(self, q = 'q'):
        print "1"
        self.q = q

a = myClass('a')
print a.q

