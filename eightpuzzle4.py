import sys
import copy

boardList = []
goal_state = [['0','1','2'], ['3','4','5'], ['6','7','8']]

class Board:
    def __init__(self, argv_starting_index):
        self.state = self.setState(argv_starting_index)
        self.h = self.manhattanDistance()
        self.g = 0  # cost function
        self.f = self.updateF()
        self.moveList = []

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
                totalDistance = totalDistance + blockDistance  # sums each block's distance from goal position
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
    def updateF(self):
        return self.h + self.g

    def win_condition(self):
        # Win condition
        if self.h == 0:
            print
            "Manhattan distance = 0!"
            for m in self.moveList:
                print
                m
                sys.exit()

    # Expands new possible states
    def expand(self):
        global boardList
        zeroX, zeroY = self.find_coordinate('0')

        # Checks if a block can be moved up
        if 0 <= zeroX + 1 <=2:
            #print "up"
            boardList.append(copy.deepcopy(self))

            block = boardList[-1].state[zeroX + 1][zeroY]
            boardList[-1].state[zeroX + 1][zeroY] = '0'
            boardList[-1].state[zeroX][zeroY] = block
            #print boardList[-1].state

            if boardList[-1].uniqueState():
                boardList[-1].moveList.append([block, "up"])
                boardList[-1].g = boardList[-1].g + 1
                boardList[-1].manhattanDistance()
                boardList[-1].expanded = False
            else:
                #print "delete 1"
                del boardList[-1]

        # Checks if a block can be moved down
        if 0 <= zeroX - 1 <=2:
            #print "down"
            boardList.append(copy.deepcopy(self))

            block = boardList[-1].state[zeroX - 1][zeroY]
            boardList[-1].state[zeroX - 1][zeroY] = '0'
            boardList[-1].state[zeroX][zeroY] = block
            #print boardList[-1].state

            if boardList[-1].uniqueState():
                boardList[-1].moveList.append([block, "down"])
                boardList[-1].g = boardList[-1].g + 1
                boardList[-1].manhattanDistance()
                boardList[-1].expanded = False
            else:
                #print "delete 2"
                del boardList[-1]

        # Checks if a block can be moved left
        if 0 <= zeroY + 1 <=2:
            #print "left"
            boardList.append(copy.deepcopy(self))

            block = boardList[-1].state[zeroX][zeroY + 1]
            boardList[-1].state[zeroX][zeroY + 1] = '0'
            boardList[-1].state[zeroX][zeroY] = block
            #print boardList[-1].state

            if boardList[-1].uniqueState():
                boardList[-1].moveList.append([block, "left"])
                boardList[-1].g = boardList[-1].g + 1
                boardList[-1].manhattanDistance()
                boardList[-1].expanded = False
            else:
                #print "delete 3"
                #print boardList[-1].state
                #print "len before", len(boardList)
                del boardList[-1]
                #print "len after", len(boardList)


        # Checks if a block can be moved right
        if 0 <= zeroY - 1 <=2:
            #print "right"
            boardList.append(copy.deepcopy(self))

            block = boardList[-1].state[zeroX][zeroY - 1]
            boardList[-1].state[zeroX][zeroY - 1] = '0'
            boardList[-1].state[zeroX][zeroY] = block
            #print boardList[-1].state

            if boardList[-1].uniqueState():
                boardList[-1].moveList.append([block, "right"])
                boardList[-1].g = boardList[-1].g + 1
                boardList[-1].manhattanDistance()
                boardList[-1].expanded = False
            else:
                #print "delete 4"
                #print boardList[-1].state
                #print "len before", len(boardList)
                del boardList[-1]
                #print "len after", len(boardList)

    # Returns the board with the lowest f and removes it from boardList
    def get_lowest_f(self):
            minimum = sys.maxint
            min_index = 0
            for i in range(len(boardList)):
                boardList[i].win_condition
                if boardList[i].f < minimum:
                    minimum = boardList[i].f
                    min_index = i
            return boardList.pop(min_index)

    # Prints the state of a puzzle
    def printPuzzle(self):
        for row in self.state:
            for block in row:
                print block,
            print "\n"


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

x = start_state.get_lowest_f()
print x.state

'''print "boardList after:"
for b in boardList:
    print b.state'''