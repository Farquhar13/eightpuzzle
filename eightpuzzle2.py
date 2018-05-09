import sys

boardList = []
duds = []
goal_state = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]

class Board():
    def __init__(self):
        self.state = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
        self.h = -1
        self.g = -1  # cost function
        self.f = -1
        self.moveList = [["start", "start"]]

    def set_start_state(self, argv_starting_index):
        index = argv_starting_index  # 1 is the index for starting state
        state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):  # loops through rows
            for j in range(3):  # loops through columns
                state[i][j] = sys.argv[index]
                index = index + 1
        return state

    def manhattanDistance(self):
        totalDistance = 0
        for i in range(3):
            for j in range(3):
                block = self.state[i][j]  # Goes through block by block
                coordinate = self.goalCoordinates(block)  # finds the coordinate of the same block in the goal state
                blockDistance = abs(i - coordinate[0]) + abs(j - coordinate[1])  # determines how far the block is from the goal state position
                totalDistance += blockDistance  # sums each block's distance from goal position
        if totalDistance == 0:
            self.done()
        return totalDistance

    def goalCoordinates(self, block):
        for i in range(0,3):
            for j in range(0,3):
                if block == goal_state[i][j]:
                    coordinate = i, j
                    return coordinate

    def set_function(self):
        if self.state == [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]:
            print "initialize first"
        self.h = self.manhattanDistance()
        self.g += 1
        self.f = self.h + self.g


    def done(self):
        print "Manhattan distance = 0!"
        for m in self.moveList:
            print m
        sys.exit(0)

    def print_board(self):
        print "state: ", self.state
        print "h: ", self.h
        print "g: ", self.g
        print "f: ", self.f
        print "movelist: ", self.moveList

    # Returns the board with the lowest f and removes it from boardList
    def find_lowest_f(self):
        minimum = sys.maxint
        min_index = 0
        for i in range(len(boardList)):
            if boardList[i].f < minimum:
                minimum = boardList[i].f
                min_index = i
        return boardList.pop(min_index)

    def find_coordinate(self, block):
        for i in range(0,3):
            for j in range(0,3):
                if block == self.state[i][j]:
                    coordinate = i, j
                    return coordinate

    def copy_mutable_state(self):
        new_state = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
        for i in range(3):
            for j in range(3):
                new_state[i][j] = self.state[i][j]
        return new_state

    def copy_board(self):
        nb = Board()
        nb.state = self.copy_mutable_state()
        nb.g = self.g
        nb.moveList = self.moveList
        return nb

    def find_moves(self):
        print "test"
        zeroX, zeroY = self.find_coordinate('0')
        last_move = self.moveList[-1][1]

        if (zeroX + 1) <= 2 and last_move != "down":
            print "test1"

            nb = self.copy_board()

            block = nb.state[zeroX + 1][zeroY]
            nb.state[zeroX + 1][zeroY] = '0'
            nb.state[zeroX][zeroY] = block
            nb.moveList.append([block, "up"])
            nb.check_and_append()
        '''
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
        '''

        duds.append(self.state)

    def no_loops(self):
        for past_state in duds:
            if self.state == past_state:
                return False
        return True

    def check_and_append(self):
        if self.no_loops():
            self.set_function()
            boardList.append(self)

    def do_it(self):
        #self.state = goal_state

        #algorithm
        b = self.find_lowest_f() # find the lowest function value in boardList
        b.print_board()
        b.find_moves() #finds valid moves
        #creates children / child
        #set state that doesn't change the parent
        #set function variables and movelist = parent
        #make the move
        #if the new state does not match any previous state add to boardList
        #add old state to board list
        #repeat until win condition is met





start = Board()
start.state = start.set_start_state(1)
start.set_function()
boardList.append(start)

driver = Board() #going to use this to run
driver.do_it()

print "duds: ", duds
for b in boardList:
    b.print_board()