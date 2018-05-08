import sys
import copy

goal_state = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
boardList = []

class Board():
    def __init__(self, argv_starting_index):
        self.state = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
        self.h = 5

    def copy_mutable_state(self):
        new_state = [[0, 0, 0], [0, 0, 0], [0 , 0, 0]]
        for i in range(3):
            for j in range(3):
                new_state[i][j] = self.state[i][j]
        return new_state

class Child(Board):
    def __init__(self, parent):
        self.state = parent.copy_mutable_state()
        self.h = parent.h



def init_goal_state(argv_index):
    for row in range(3):
        for column in range(3):
            goal_state[row][column] = sys.argv[argv_index]
            argv_index = argv_index + 1

start_state = Board(1)

boardList.append(start_state)

child = Child(start_state)

print "start",  start_state.state
print "child", child.state

child.state[0][0] = 9

print "start",  start_state.state
print "child", child.state

