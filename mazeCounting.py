import itertools

# class Node():
# 	def __init__(self, xVal, yVal):
# 		self.xVal = xVal
# 		self.yVal = yVal

# 	def addConnection(self, newConnection):
# 		self.connections += [newConnection]

# 	def __str__(self):
# 		return str(self.xVal) + " " + str(self.yVal)

# 	def __repr__(self):
# 		return str(self.xVal) + " " + str(self.yVal)


# def createGraph(width, height):
# 	myGraph = []
# 	for j in range(0, height):
# 		myGraph += [list()]
# 		for i in range(0, width):
# 			newNode = Node(i,j)
# 			myGraph[j] += [newNode]

# 	for j in range(0, height):
# 		for i in range(0, width):
# 			if i > 0:
# 				myGraph[j][i].addConnection(myGraph[j][i-1]) #Add link to the one to the left
# 			if j > 0:
# 				myGraph[j][i].addConnection(myGraph[j-1][i]) #Add link to the one above
# 			if i < width - 1:
# 				myGraph[j][i].addConnection(myGraph[j][i+1]) #Add link to the one to the right
# 			if j < height - 1:
# 				myGraph[j][i].addConnection(myGraph[j+1][j]) #Add link to the one below
# 			print myGraph[j][i]
# def createGraph(width, height):
# 	myGraph = []
# 	myEdges = []
# 	for j in range(0, height):
# 		myGraph += [list()]
# 		for i in range(0, width):
# 			myGraph[j] += [(j,i)]
# 			if j < height - 1:
# 				myEdges += [[j,i],[j+1, i]]
# 			if i < width - 1:
# 				myEdges += [[j,i],[j,i+1]]
# 	print myGraph
# 	print myEdges

# def printMaze(myGraph):
# 	for i in range(0, len(myGraph)):
# 		print myGraph[i]

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def __str__(self):
    	return self.id

    def __repr__(self):
    	return str(self.id)

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def printGraph(self):
    	for aVert in self.vertList:
    		print aVert, str(self.vertList[aVert].connectedTo.keys())

def createGraph(bdSize, myEdges):
    myGraph = Graph()
    for row in range(bdSize):
       for col in range(bdSize):
           nodeId = posToNodeId(row,col,bdSize)
           newPositions = genLegalMoves(row,col,bdSize)
           for e in newPositions:
               nid = posToNodeId(e[0],e[1],bdSize)
               myGraph.addEdge(nodeId,nid)
               if set([nodeId, nid]) not in myEdges:
                   myEdges += [set([nodeId, nid])]
    # myGraph.printGraph()
    return myGraph

def checkGraph(aGraph, edges):
	print len(edges)


def posToNodeId(row,col,bdSize):
	return (row*bdSize) + col

def genLegalMoves(x,y,bdSize):
    newMoves = []
    moveOffsets = [(-1,0),(0,-1),(1,0),(0,1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX,bdSize) and \
                        legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    return newMoves

def legalCoord(x,bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False

# (set([0, 3]), set([0, 1]), set([1, 4]), set([1, 2]), set([2, 5]), set([3, 6]), set([3, 4]), set([4, 7]))
def checkIfValidState(bdSize, edges):
	allVertices = set()
	for anEdge in edges:
		allVertices.add(list(anEdge)[0])
		allVertices.add(list(anEdge)[1])
	return len(allVertices) == bdSize * bdSize

# 4, 292, 453620
def main():
    bdSize = 3
    myEdges = []
    myGraph = createGraph(bdSize, myEdges)
    print "mark1"
    possibleValidStates = list(itertools.combinations(myEdges, bdSize*bdSize-1))
    validCount = 0
    for aPossibleValidState in possibleValidStates:
        if checkIfValidState(bdSize, aPossibleValidState):
            print aPossibleValidState
            
            validCount += 1
    print validCount

    # for aPossibleState  in possibleValidStates:
        

    # print myEdges
    # print "check Time"
    # checkGraph(myGraph, myEdges)

if __name__ == '__main__':
	main()