import sys

class Board:
    def __init__(self):
        self.state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.f = -1
        self.g = -1
        self.h = -1
        self.move_list = []

    def setState(self, argvStartIndex):
        index = argvStartIndex
        for i in range(0, 3):  # loops through rows
            for j in range(0, 3):  # loops through columns
                self.state[i][j] = sys.argv[index]
                index = index + 1

    def printPuzzle(self):
        for row in self.state:
            for block in row:
                print block,
            print "\n"

    def manhattanDistance(self):
        totalDistance = 0
        for i in range(0,3):
            for j in range(0,3):
                block = self.state[i][j]
                coordinate = goalState.goalCoordinates(block)
                blockDistance = abs(i - coordinate[0]) + abs(j - coordinate[1])
                totalDistance = totalDistance + blockDistance
        self.h = totalDistance


    def goalCoordinates(self, block):
        for i in range(0,3):
            for j in range(0,3):
                if block == self.state[i][j]:
                    coordinate = i, j
                    return coordinate

startState = Board()
startState.setState(1)
print "Start State:"
startState.printPuzzle()

goalState = Board()
goalState.setState(10)
print "Goal State:"
goalState.printPuzzle()

startState.manhattanDistance()
print startState.h