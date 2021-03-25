class Node:
	    def __init__(self, data, level, direction):
	        self.data = data
	        self.fscore = 0
	        self.level = level
	        self.direction = direction
	        self.generatedSubPuzzle = []
	

	    def createSides(self):
	

	        locationOfZero = self.findZero(self.data)
	        copyOfData = self.copy(self.data)
	        '''
	        getSides method is gonna return an array of its child nodes
	        [i, j , direction]
	         i represents the row value of the possible next direction
	         j represents the column valud if the possible next directon
	         direction is either up down left and right depends on the current coord of zero
	
	        '''
	        sidesOfZeroNode = self.getSides(copyOfData, locationOfZero)
	        # print(sidesOfZeroNode)
	        for item in sidesOfZeroNode:
	            rowIdx, columnIdx, currentDirection = item
	            newChildPuzzle = self.swap(
	                copyOfData, [rowIdx, columnIdx], locationOfZero)
	            # print(newChildPuzzle)
	            newCreatedPuzzle = Node(
	                newChildPuzzle, self.level + 1, currentDirection)
	            self.generatedSubPuzzle.append(newCreatedPuzzle)
	

	        return self.generatedSubPuzzle
	

	    def swap(self, copyData, childCoord, locationOfZero):
	        newData = self.copy(copyData)
	        childRow, childColum = childCoord
	        mainRow, mainColumn = locationOfZero
	        newData[childRow][childColum], newData[mainRow][mainColumn] = newData[mainRow][mainColumn], newData[childRow][childColum]
	        return newData
	

	    def getSides(self, currentPuzzle, locationOfZero):
	        row = len(currentPuzzle)
	        column = len(currentPuzzle[0])
	        i = locationOfZero[0]
	        j = locationOfZero[1]
	        result = []
	        if i < row - 1:
	            result.append([i + 1, j, 'DOWN'])
	        if i > 0:
	            result.append([i - 1, j, 'UP'])
	        if j < column - 1:
	            result.append([i, j + 1, 'RIGHT'])
	        if j > 0:
	            result.append([i, j - 1, 'LEFT'])
	        return result
	

	    def findZero(self, data):
	        row = 0
	        column = 0
	        for i in range(len(data)):
	            for j in range(len(data[0])):
	                item = data[i][j]
	                if item == '0':
	                    row = i
	                    column = j
	                    break
	        return [row, column]
	

	    def copy(self, data):
	        return [[val for val in item] for item in data]

class Main:
	    def __init__(self):
	        self.open = []
	        self.goal = self.getGoal()
	        self.start = self.getStart()
	        self.counter = 0
	

	    def getGoal(self):
	        return [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '0']
        ]
	

	    def getStart(self):
	        array = []
	        with open('mlp1input.txt', 'r') as reader:
	            for line in reader.readlines():
	                oneline = line.split(' ')
	                newl = list(map(lambda x: x.rstrip('\n'), oneline))
	                array.append(newl)
	        return array
	

	    def getFScore(self, inital, goal):
	        hScore = self.getHScore(inital.data, goal)
	        goalScore = inital.level
	        return hScore + goalScore
	

	    def getHScore(self, startData, goal):
	        count = 0
	        for i in range(len(startData)):
	            for j in range(len(startData[0])):
	                current = startData[i][j]
	                other = goal[i][j]
	                if current != other and current != '0':
	                    count += 1
	        return count
	

	    def pintPuzzle(self, puzzle):
	        for i in puzzle.data:
	            for j in i:
	                print(j, end=" ")
	            print("")
	

	    def applyAStar(self):
	        print(
	            'Machine Learning \n MLP1: A* Algoritm for Sliding Puzzle \nSEMESTER: [Spring 2021]\nNAME: [Sai Kumar Vurukonda]')
	        print('**********')
	        inital = Node(self.start, 0, None)
	        inital.fscore = self.getFScore(inital, self.goal)
	        self.open.append(inital)
	        while True:
	            puzzle = self.open[0]
	            print(f"MOVE : {puzzle.direction}")
	            self.pintPuzzle(puzzle)
	            print('**********')
	            if self.getHScore(puzzle.data, self.goal) == 0:
	                break
	            neighborPuzzles = puzzle.createSides()
	            for sub in neighborPuzzles:
	                self.counter += 1
	                sub.fscore = self.getFScore(sub, self.goal)
	                self.open.append(sub)
	            del self.open[0]
	            self.open.sort(key=lambda x: x.fscore)
	        print(f"number of states visited {self.counter - 2}")
	

	

main = Main()
main.applyAStar()

