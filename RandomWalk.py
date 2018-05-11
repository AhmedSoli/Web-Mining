import random
# 1. Choose a node at random
# 2. Choose an edge at random from this node
# 3.  
# 3.1 20%: stop the walk.
# 3.2 80%: go over the chosen edge to a new node. The Repeat from 2
# 4. Repeat 100

def getNodeWithIndex(G,index):
    iteration = 0
    for node in G.nodes():
        if iteration == index:
            return node
        iteration += 1
        
        
def getRandomEdge(G,Node):
    # Choose a random number x between 0 and the number of edges for the chosen Node
    randomEdgeIndex = random.randint(0,len(G.edges(Node)))
    iteration = 0
    for edge in G.edges(Node):
        if iteration == randomEdgeIndex:
            return edge
        iteration += 1
    return False

def randomWalk(G,Repeat):
    resultMatrix = [0] * len(G.nodes)
    for i in range(0,Repeat):
        # Choosing the starting node randomly 
        nodesLength = len(G.nodes())
        randomNodeIndex = random.randint(0,nodesLength - 1)
        chosenNode = getNodeWithID(G,randomNodeIndex)
        # Setting up param for the Walk
        continueWalk = True
        while(continueWalk != False):
            resultMatrix[int(chosenNode)] += 1
            # Choosen a random edge from the chosenNode
            randomEdge = getRandomEdge(G,chosenNode)
            # If edge found: continue. Otherwise: END THE WALK  
            if randomEdge != False:
                # 20% : END THE WALK || 80%: CONTINUE THE WALK
                print(randomEdge)
                continueWalk = random.randint(0,5)
                chosenNode = randomEdge[1]
            else:
                continueWalk = False
    return resultMatrix

randomWalk(G,10000)