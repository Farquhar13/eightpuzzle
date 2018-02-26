import sys

boardList = []

class Board:
    def __init__(self):
        self.state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.f = -1 #function = g + h
        self.g = 0 #cost function
        self.h = -1 #hueristic = Manhattan distance
        self.moveList = []
        self.expanded = False

    #Initializes the board state
    def setState(self, argvStartIndex):
        index = argvStartIndex
        for i in range(0, 3):  # loops through rows
            for j in range(0, 3):  # loops through columns
                self.state[i][j] = sys.argv[index]
                index = index + 1

    #Prints the state of a puzzle
    def printPuzzle(self):
        for row in self.state:
            for block in row:
                print block,
            print "\n"

    #Calculates h and calls method to update f
    def manhattanDistance(self):
        totalDistance = 0
        for i in range(0,3):
            for j in range(0,3):
                block = self.state[i][j] #Goes through block by block
                coordinate = goalState.goalCoordinates(block) #finds the coordinate of the same block in the goal state
                blockDistance = abs(i - coordinate[0]) + abs(j - coordinate[1]) #determines how far the block is from the goal state position
                totalDistance = totalDistance + blockDistance #sums each block's distance from goal position
        self.h = totalDistance
        self.updateF()

    #Finds the coordinate of a block, given as an argument
    def goalCoordinates(self, block):
        for i in range(0,3):
            for j in range(0,3):
                if block == self.state[i][j]:
                    coordinate = i, j
                    return coordinate

    #updates our function f
    def updateF(self):
        self.f = self.h + self.g

    #Checks for available moves
    def moveBlock(self):
        zeroX, zeroY = self.goalCoordinates('0')
        print "zeroX:", zeroX
        print "zeroY:", zeroY

        if 0 <= zeroX + 1 <=2:
            newState = self
            block = self.state[zeroX + 1][zeroY]
            newState.state[zeroX][zeroY] = block
            newState.state[zeroX + 1][zeroY] = '0'
            #check if state matches any from boardList
            if self.uniqueState == True:
                newState.moveList.append([block, "left"])
                boardList.append(newState)
                newState.g = self.g + 1

        if 0 <= zeroX - 1 <=2:
            print "right"
        if 0 <= zeroY + 1 <=2:
            print "up"
        if 0 <= zeroY - 1 <=2:
            print "down"

    def uniqueState(self):
        for board in boardList:
            if self.state == board.state:
                return False
            else:
                return True

    def lowestF(self):
        min = 1000000
        for i in range len(boardList):
            if boardList[i].expanded == False and boardList[i].f < min:
                min = boardList[i].f
                minIndex = i





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

startState.moveBlock()


goalState.moveBlock()