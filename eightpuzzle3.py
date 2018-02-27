import sys
import copy

boardList = []

class Board:
    def __init__(self):
        self.state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.f = -1  # function = g + h
        self.g = 0  # cost function
        self.h = -1  # hueristic = Manhattan distance
        self.moveList = []
        self.expanded = False

    # Initializes the board state
    def setState(self, argvStartIndex):
        index = argvStartIndex
        for i in range(0, 3):  # loops through rows
            for j in range(0, 3):  # loops through columns
                self.state[i][j] = sys.argv[index]
                index = index + 1

    # Prints the state of a puzzle
    def printPuzzle(self):
        for row in self.state:
            for block in row:
                print block,
            print "\n"

    # Calculates h and calls method to update f
    def manhattanDistance(self):
        totalDistance = 0
        for i in range(0,3):
            for j in range(0,3):
                block = self.state[i][j]  # Goes through block by block
                coordinate = goalState.goalCoordinates(block)  # finds the coordinate of the same block in the goal state
                blockDistance = abs(i - coordinate[0]) + abs(j - coordinate[1])  # determines how far the block is from the goal state position
                totalDistance = totalDistance + blockDistance  # sums each block's distance from goal position
        self.h = totalDistance

        # Win condition
        if self.h == 0:
            print "Manhattan distance = 0!"
            for m in self.moveList:
                print m
                sys.exit()
        self.updateF()

    # Finds the coordinate of a block, given as an argument
    def goalCoordinates(self, block):
        for i in range(0,3):
            for j in range(0,3):
                if block == self.state[i][j]:
                    coordinate = i, j
                    return coordinate

    # Updates our function f
    def updateF(self):
        self.f = self.h + self.g

    # Expands new possible states
    def expand(self):
        global boardList
        zeroX, zeroY = self.goalCoordinates('0')

        # Checks if a block can be moved up
        if 0 <= zeroX + 1 <=2:
            boardList.append(copy.deepcopy(self))

            block = boardList[-1].state[zeroX + 1][zeroY]
            boardList[-1].state[zeroX + 1][zeroY] = '0'
            boardList[-1].state[zeroX][zeroY] = block

            if boardList[-1].uniqueState():
                boardList[-1].moveList.append([block, "up"])
                boardList[-1].g = boardList[-1].g + 1
                boardList[-1].manhattanDistance()
            else:
                del boardList[-1]

        # Checks if a block can be moved down
        if 0 <= zeroX - 1 <=2:
            boardList.append(copy.deepcopy(self))

            block = boardList[-1].state[zeroX - 1][zeroY]
            boardList[-1].state[zeroX - 1][zeroY] = '0'
            boardList[-1].state[zeroX][zeroY] = block

            if boardList[-1].uniqueState():
                boardList[-1].moveList.append([block, "down"])
                boardList[-1].g = boardList[-1].g + 1
                boardList[-1].manhattanDistance()
            else:
                del boardList[-1]

        # Checks if a block can be moved left
        if 0 <= zeroY + 1 <=2:
            boardList.append(copy.deepcopy(self))

            block = boardList[-1].state[zeroX][zeroY + 1]
            boardList[-1].state[zeroX][zeroY + 1] = '0'
            boardList[-1].state[zeroX][zeroY] = block

            if boardList[-1].uniqueState():
                boardList[-1].moveList.append([block, "left"])
                boardList[-1].g = boardList[-1].g + 1
                boardList[-1].manhattanDistance()
            else:
                del boardList[-1]

        # Checks if a block can be moved right
        if 0 <= zeroY - 1 <=2:
            boardList.append(copy.deepcopy(self))

            block = boardList[-1].state[zeroX][zeroY - 1]
            boardList[-1].state[zeroX][zeroY - 1] = '0'
            boardList[-1].state[zeroX][zeroY] = block

            if boardList[-1].uniqueState():
                boardList[-1].moveList.append([block, "right"])
                boardList[-1].g = boardList[-1].g + 1
                boardList[-1].manhattanDistance()
            else:
                del boardList[-1]


    # Checks if an expanded state is already in boardList
    def uniqueState(self):
        for board in boardList:
            if self.state == board.state:
                return False
            else:
                return True

    # Finds the board with the lowest f that hasn't been expanded
    def lowestF(self):
        while True:
            min = None  # very high initialization value
            for i in range(len(boardList)):
                if boardList[i].expanded == False and min == None:
                    min = boardList[i].f
                    minIndex = i
                if boardList[i].expanded == False and boardList[i].f < min:
                    min = boardList[i].f
                    minIndex = i

        boardList[minIndex].expanded = True
        boardList[minIndex].expand()  # selects lowest board with lowest f to expand in moveBlock


startState = Board()
startState.setState(1)
boardList.append(startState)
print "Start State:"
startState.printPuzzle()

goalState = Board()
goalState.setState(10)
print "Goal State:"
goalState.printPuzzle()

print
print "boardList before:"
for b in boardList:
    print b.state


startState.lowestF()

print "boardList after:"
for b in boardList:
    print b.state
