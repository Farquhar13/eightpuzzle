import sys
import copy

boardList = []
goal_state = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
duds = []

class Board():
    def __init__(self, argv_starting_index):
        self.state = self.setState(argv_starting_index)
        self.h = self.manhattanDistance()
        self.g = 0  # cost function
        self.f = self.update_f()
        self.moveList = [["start", "start"]]

    # Initializes the starting board state
    def setState(self, argv_starting_index):
        index = argv_starting_index  # 1 is the index for starting state
        state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):  # loops through rows
            for j in range(3):  # loops through columns
                state[i][j] = sys.argv[index]
                index = index + 1
        return state

    # Calculates h and calls method to update f
    def manhattanDistance(self):
        totalDistance = 0
        for i in range(3):
            for j in range(3):
                block = self.state[i][j]  # Goes through block by block
                coordinate = self.goalCoordinates(block)  # finds the coordinate of the same block in the goal state
                blockDistance = abs(i - coordinate[0]) + abs(j - coordinate[1])  # determines how far the block is from the goal state position
                totalDistance += blockDistance  # sums each block's distance from goal position
        return totalDistance

    # Finds the coordinate of a block, given as an argument
    def goalCoordinates(self, block):
        for i in range(0,3):
            for j in range(0,3):
                if block == goal_state[i][j]:
                    coordinate = i, j
                    return coordinate

    def find_coordinate(self, block):
        for i in range(0,3):
            for j in range(0,3):
                if block == self.state[i][j]:
                    coordinate = i, j
                    return coordinate


    # Updates our function f
    def update_f(self):
        self.win_condition()
        return self.h + self.g

    def win_condition(self):
        if self.h == 0:
            print "Manhattan distance = 0!"
            for m in self.moveList:
                print m
            sys.exit(0)

    # Returns the board with the lowest f and removes it from boardList
    def get_lowest_f(self):
            minimum = sys.maxint
            min_index = 0
            for i in range(len(boardList)):
                if boardList[i].f < minimum:
                    minimum = boardList[i].f
                    min_index = i
            the_chosen_one = boardList.pop(min_index)
            duds.append(the_chosen_one.state)
            return the_chosen_one

    def find_moves(self):
        zeroX, zeroY = self.find_coordinate('0')
        last_move = self.moveList[-1][1]

        if 0 <= (zeroX + 1) and (zeroX + 1) <= 2:
            nb = Child(self)
            block = nb.state[zeroX + 1][zeroY]
            nb.state[zeroX + 1][zeroY] = '0'
            nb.state[zeroX][zeroY] = block
            nb.update_and_append(block, "up")

        if 0 <= (zeroX - 1) and (zeroX - 1) <= 2:
            nb = Child(self)
            block = nb.state[zeroX - 1][zeroY]
            nb.state[zeroX - 1][zeroY] = '0'
            nb.state[zeroX][zeroY] = block
            nb.update_and_append(block, "down")

        if 0 <= (zeroY + 1) and (zeroY + 1) <=2:
            nb = Child(self)
            block = nb.state[zeroX][zeroY + 1]
            nb.state[zeroX][zeroY + 1] = '0'
            nb.state[zeroX][zeroY] = block
            nb.update_and_append(block, "left")

        if 0 <= (zeroY - 1) and (zeroY - 1) <= 2:
            nb = Child(self)
            block = nb.state[zeroX][zeroY - 1]
            nb.state[zeroX][zeroY - 1] = '0'
            nb.state[zeroX][zeroY] = block
            nb.update_and_append(block, "right")

        #print "self.state", self.state

    def update_and_append(self, block, direction):
        repeat = self.no_loops()
        if repeat == True:
            self.g = self.g + 1
            self.h = self.manhattanDistance()
            self.f = self.update_f()
            self.moveList.append([block, direction])
            boardList.append(self)

    # Prints the state of a puzzle
    def printPuzzle(self):
        for row in self.state:
            for block in row:
                print block,
            print "\n"

    def no_loops(self):
        for past_state in duds:
            if self.state == past_state:
                return False
            else:
                return True

    def copy_mutable_state(self):
        new_state = [['0', '0', '0'], ['0', '0', '0'], ['0' , '0', '0']]
        for i in range(3):
            for j in range(3):
                new_state[i][j] = self.state[i][j]
        return new_state

    def loop(self):
        c = 0
        while True:
            board = self.get_lowest_f()
            board.find_moves()

            c += 1
            if c == 20000:
                board = self.get_lowest_f()
                print board.h
                sys.exit(0)



class Child(Board):
    def __init__(self, parent):
        self.state = parent.copy_mutable_state()
        self.h = parent.h
        self.g = parent.g
        self.f = parent.f
        self.moveList = parent.moveList



def init_goal_state(argv_index):
    for row in range(3):
        for column in range(3):
            goal_state[row][column] = sys.argv[argv_index]
            argv_index = argv_index + 1

init_goal_state(10)
start_state = Board(1)

boardList.append(start_state)
print "Start State:"
start_state.printPuzzle()

start_state.loop()

'''print "boardList after:"
for b in boardList:
    print b.state'''

'''c = 0
while True:
    board = boardList[-1].get_lowest_f()
    board.find_moves()

    c += 1
    if c == 30000:
        board = boardList[-1].get_lowest_f()
        print board.h
        sys.exit(0)'''
