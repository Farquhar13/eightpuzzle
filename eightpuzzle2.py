import sys

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
        if self.h == 0:
            pass  # win condition
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
        zeroX, zeroY = self.goalCoordinates('0')

        # Checks if a block can be moved up
        if 0 <= zeroX + 1 <=2:
            boardList.append(Board())
            boardList[-1].state = self.state
            boardList[-1].f = self.f  # function = g + h
            boardList[-1].g = self.g  # cost function
            boardList[-1].h = self.h  # hueristic = Manhattan distance
            boardList[-1].moveList = self.moveList
            boardList[-1].expanded = False

            print "pre self.state", self.state
            block = boardList[-1].state[zeroX + 1][zeroY]
            boardList[-1].state[zeroX + 1][zeroY] = '0'
            boardList[-1].state[zeroX][zeroY] = block
            print "post self.state", self.state
            if boardList[-1].uniqueState():
                print "check 2"  # BUG! does not print
                boardList[-1].moveList.append(block, "up")
                boardList[-1].g = boardList[-1].g + 1
                boardList[-1].manhattanDistance()
                boardList.append(boardList[-1])


        '''# Checks if a block can be moved down
        if 0 <= zeroX - 1 <=2:
            newState = self
            block = self.state[zeroX - 1][zeroY]
            newState.state[zeroX][zeroY] = block
            newState.state[zeroX - 1][zeroY] = '0'

            if self.uniqueState:
                newState.moveList.append([block, "down"])
                boardList.append(newState)
                newState.g = self.g + 1
                self.manhattanDistance()

        # Checks if a block can be moved left
        if 0 <= zeroY + 1 <=2:
            newState = self
            block = self.state[zeroX][zeroY + 1]
            newState.state[zeroX][zeroY] = block
            newState.state[zeroX][zeroY + 1] = '0'

            if self.uniqueState:
                newState.moveList.append([block, "left"])
                boardList.append(newState)
                newState.g = self.g + 1
                self.manhattanDistance()

        # Checks if a block can be moved right
        if 0 <= zeroY - 1 <=2:
            newState = self
            block = self.state[zeroX][zeroY - 1]
            newState.state[zeroX][zeroY] = block
            newState.state[zeroX][zeroY - 1] = '0'

            if self.uniqueState:
                newState.moveList.append([block, "right"])
                boardList.append(newState)
                newState.g = self.g + 1
                self.manhattanDistance()'''


    # Checks if an expanded state is already in boardList
    def uniqueState(self):
        for board in boardList:
            if self.state == board.state:
                return False
            else:
                return True

    # Finds the board with the lowest f that hasn't been expanded
    def lowestF(self):
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


class Successor(Board):
    def __init__(self, parent, direction):
        self.state = parent.state
        self.f = parent.f  # function = g + h
        self.g = parent.g  # cost function
        self.h = parent.h  # hueristic = Manhattan distance
        self.moveList = parent.moveList
        self.expanded = False

        if direction == "up":
            print "pre parent.state", parent.state
            zeroX, zeroY = self.goalCoordinates('0')
            block = self.state[zeroX + 1][zeroY]
            self.state[zeroX + 1][zeroY] = '0'
            self.state[zeroX][zeroY] = block
            print "post parent.state:", parent.state  # BUG! changes parent.state
            if self.uniqueState():
                print "check 2"  # BUG! does not print
                self.moveList.append(block, "up")
                self.g = self.g + 1
                self.manhattanDistance()
                boardList.append(self)



startState = Board()
startState.setState(1)
boardList.append(startState)
print "Start State:"
startState.printPuzzle()

goalState = Board()
goalState.setState(10)
print "Goal State:"
goalState.printPuzzle()

startState.manhattanDistance()
print "Starting Manhattan distance:", startState.h

print "Function total:", startState.f

print
print "boardList before:"
for b in boardList:
    print b.state

startState.lowestF()

print
print "boardList after:"
for b in boardList:
    print b.state