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


def visualizeGraph(bdSize, edges):
	visualGraph = Graph()
	for edge in edges:
		edgeList = list(edge)
		visualGraph.addEdge(edgeList[0], edgeList[1])
		visualGraph.addEdge(list(edge)[1], list(edge)[0])
	# visualGraph.printGraph()
	for i in range(bdSize):
		toPrintLine = ""
		for j in range(bdSize):
			if j != bdSize - 1:
				if set([(bdSize*i)+j, (bdSize*i)+j+1]) in edges:
					toPrintLine += "*--"
				else:
					toPrintLine += "*  "
		toPrintLine += "*"
		print toPrintLine

		toPrintLine = ""
		for j in range(bdSize):
			if set([(bdSize*i)+j, (bdSize*i)+j+bdSize]) in edges:
				toPrintLine += "|  "
			else:
				toPrintLine += "   "

		print toPrintLine

	for edge in edges:
		edgeList = list(edge)

	


def checkIfValidState(bdSize, edges):
	checkGraph = Graph()
	for edge in edges:
		checkGraph.addEdge(list(edge)[0], list(edge)[1])
		checkGraph.addEdge(list(edge)[1], list(edge)[0])
	
	vertsSeen = [checkGraph.getVertex(0)]
	frontier = [checkGraph.getVertex(0)]
	while frontier:
		checkVert = frontier.pop(0)
		if not checkVert: return False
		for aConnection in checkVert.getConnections():
			if aConnection not in vertsSeen:
				frontier += [aConnection]
				vertsSeen += [aConnection]
		# print frontier
	# print vertsSeen
	return len(vertsSeen) == (bdSize*bdSize)

# 4, 192, 100352
def main():
    bdSize = 4
    myEdges = []	
    myGraph = createGraph(bdSize, myEdges)
    possibleValidStates = list(itertools.combinations(myEdges, bdSize*bdSize-1))
    validCount = 0
    numPossible = len(possibleValidStates)
    counter = 0
    print "start check"
    for aPossibleValidState in possibleValidStates:
    	counter += 1
        if checkIfValidState(bdSize, aPossibleValidState):
            visualizeGraph(bdSize, aPossibleValidState)
            validCount += 1
    	if(counter % 10000 == 0):
    		print counter, " / ", numPossible, " : ", validCount
    print validCount





    # print validEdgeCounts

    # for aPossibleState  in possibleValidStates:
        

    # print myEdges
    # print "check Time"
    # checkGraph(myGraph, myEdges)

if __name__ == '__main__':
	main()