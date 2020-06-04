# -------------------------------------------------------
# Assignment 1
# Written by Raghav Sharda 40017344
# For COMP 472 Section ABJX – Summer 2020
# --------------------------------------------------------

import numpy as np
import math

def astar(dictOfVertexObjects,grid_vertex_edges,initialNodeRef,finalNodeRef):
    
    # Initialize both open and closed list
    open_list = []
    closed_list = []
    touch = []
    fcost  = 0
    # Add the start node
    open_list.append(initialNodeRef)

    # Loop until you find the end
    while len(open_list) > 0:
        
        # Get the current node
        currentNode = min(open_list, key=lambda o:o.G)

        #If it is the item we want, retrace the path and return it
        if currentNode.isEquals(finalNodeRef):
            path = []
            while currentNode.parent:
                path.append(currentNode)
                currentNode = currentNode.parent
                fcost = fcost + currentNode.G
            path.append(currentNode)
            print ("Cost of Path ",fcost)
            # print(path)
            return path[::-1],touch
        
        #Remove the item from the open set
        open_list.remove(currentNode)

        #Add it to the closed set
        closed_list.append(currentNode)

        # Loop through the node's children/neighbour
        for direction,neighbourNodeRef in currentNode.egdeList.items():
            # To check if node's children/neighbour are not empty
            # as boundry nodes will not have children in all direction
            if bool(currentNode.egdeList[direction]):
                # Now check if that edge in this direction is accessible 
                if getEdgeAccessibility(currentNode,currentNode.egdeList[direction],dictOfVertexObjects,grid_vertex_edges) == False:
                   
                    #If the children is already in the closed set, skip it
                    if neighbourNodeRef in closed_list:
                        # print ("Node has already been visited")
                        continue
                    
                    if neighbourNodeRef in open_list:
                        # Check if we beat the G score 
                        new_g = currentNode.G + move_cost(currentNode,neighbourNodeRef,dictOfVertexObjects,grid_vertex_edges)
                        if neighbourNodeRef.G > new_g:
                            #If so, update the node to have a new parent
                            neighbourNodeRef.G = new_g
                            neighbourNodeRef.parent = currentNode
                    if neighbourNodeRef not in open_list and neighbourNodeRef not in closed_list:
                        # If it isn't in the open set, calculate the G and H score for the node
                        neighbourNodeRef.G = currentNode.G + move_cost(currentNode,neighbourNodeRef,dictOfVertexObjects,grid_vertex_edges)
                        neighbourNodeRef.H = diagonalDistance(neighbourNodeRef, finalNodeRef)
                        neighbourNodeRef.F = neighbourNodeRef.G + neighbourNodeRef.H
                        #Set the parent to our current item
                        neighbourNodeRef.parent = currentNode
                        #Add it to the list
                        open_list.append(neighbourNodeRef)
            else:
                continue
    raise ValueError('No Path Found')

def manhattan(Vertex1,Vertex2):
    return abs(Vertex1.xCoordinate - Vertex2.xCoordinate) + abs(Vertex1.yCoordinate - Vertex2.yCoordinate)              

def euclidean(Vertex1, Vertex2):
    return math.sqrt(Vertex1.xCoordinate * Vertex2.xCoordinate + Vertex1.yCoordinate * Vertex2.yCoordinate)

def diagonalDistance(Vertex1,Vertex2):
    D = 1.0
    D2 = 1.5
    dx = abs(Vertex1.xCoordinate - Vertex2.xCoordinate)
    dy = abs(Vertex1.yCoordinate - Vertex2.yCoordinate)
    return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

def createVertex(listofcoordinates,xdistance,ydistance,gridSize):
    grid_vertex_objects = {}
    vertex_id = 0
    for coordinate in listofcoordinates:
        x = round(coordinate['X'],3)
        y = round(coordinate['Y'],3)
        grid_vertex_objects[vertex_id] = Vertex(x,y,xdistance,ydistance,gridSize)
        vertex_id += 1
    return grid_vertex_objects

# Not being used right now
def createMatrix(dictOfVertexObjects):
    data = list(dictOfVertexObjects.items()) 
    an_array = np.array(data)
    print(an_array)

def makeFriends(dictOfVertexObjects):
    # iterate over dict of objects
    for node in dictOfVertexObjects.values():
        # check if neighbours are already exsisting nodes
        for x in dictOfVertexObjects.values():
            if not (node.isEquals(x)):
                if node.neighbours['north']['xCoordinate'] == x.xCoordinate and node.neighbours['north']['yCoordinate'] == x.yCoordinate:
                    node.egdeList['north'] = x
                    continue
                if node.neighbours['north-east']['xCoordinate'] == x.xCoordinate and node.neighbours['north-east']['yCoordinate'] == x.yCoordinate:
                    node.egdeList['north-east'] = x
                    continue
                if node.neighbours['east']['xCoordinate'] == x.xCoordinate and node.neighbours['east']['yCoordinate'] == x.yCoordinate:
                    node.egdeList['east'] = x
                    continue
                if node.neighbours['south-east']['xCoordinate'] == x.xCoordinate and node.neighbours['south-east']['yCoordinate'] == x.yCoordinate:
                    node.egdeList['south-east'] = x
                    continue
                if node.neighbours['south']['xCoordinate'] == x.xCoordinate and node.neighbours['south']['yCoordinate'] == x.yCoordinate:
                    node.egdeList['south'] = x
                    continue
                if node.neighbours['west']['xCoordinate'] == x.xCoordinate and node.neighbours['west']['yCoordinate'] == x.yCoordinate:
                    node.egdeList['west'] = x
                    continue
                if node.neighbours['south-west']['xCoordinate'] == x.xCoordinate and node.neighbours['south-west']['yCoordinate'] == x.yCoordinate:
                    node.egdeList['south-west'] = x
                    continue
                if node.neighbours['north-west']['xCoordinate'] == x.xCoordinate and node.neighbours['north-west']['yCoordinate'] == x.yCoordinate:
                    node.egdeList['north-west'] = x
                    continue
                else:
                    pass

# Not being used right now
def getKeyforVertex(X,Y):
        key = str(X)+str(Y)
        key = key.replace("-", "")
        key = key.replace(".", "")
        return key

# Not being used right now
def getKeyforEdge(focus,neighbour):
        x = str(focus.xCoordinate) + str(neighbour.xCoordinate)
        y = str(focus.yCoordinate) + str(neighbour.yCoordinate)
        key = x+y
        return key

def setHighCrimeAreas(crimeRates,dictOfVertexObjects,gridSize,threshold):
    keysofdict = list(dictOfVertexObjects)
    grid_vertex_edges = {}
    x1b = dictOfVertexObjects[0].xCoordinate
    x2b = dictOfVertexObjects[keysofdict[-1]].xCoordinate
    y1b = dictOfVertexObjects[0].yCoordinate
    y2b = dictOfVertexObjects[keysofdict[-1]].yCoordinate
    edge_id = None
    l = -1
    for crimes in crimeRates:
        # skip the nth postion
        l = l + 1
        for crime in crimes:
            nodeAtFocus = dictOfVertexObjects[keysofdict[l]]
            # print("This is focus node" ,nodeAtFocus.xCoordinate ,nodeAtFocus.yCoordinate)
            northNode = nodeAtFocus.egdeList['north']
            northEastNode = nodeAtFocus.egdeList['north-east']
            eastNode = nodeAtFocus.egdeList['east']

            if bool(northNode):
                edge_id = str(l)+ str(l+1)
                if edge_id in grid_vertex_edges.keys():
                    if crime >= threshold:
                        grid_vertex_edges[edge_id].setIsRed(True)
                    else:
                        grid_vertex_edges[edge_id].setIsGreen(True)   
                else:
                    grid_vertex_edges[edge_id] = Edge(nodeAtFocus,northNode)
                    if crime >= threshold:
                        grid_vertex_edges[edge_id].setIsRed(True)
                    else:
                        grid_vertex_edges[edge_id].setIsGreen(True) 
            
            #Init diagonal edge number 1
            if bool(northEastNode):
                edge_id = str(l)+ str(l+gridSize+2)
                if edge_id in grid_vertex_edges.keys():
                    if crime >= threshold:
                        grid_vertex_edges[edge_id].setIsRed(True)
                    else:
                        grid_vertex_edges[edge_id].setIsGreen(True)   
                else:
                    grid_vertex_edges[edge_id] = Edge(nodeAtFocus,northEastNode)
                    grid_vertex_edges[edge_id].setIsDiagonal(True)

                    if crime >= threshold:
                        grid_vertex_edges[edge_id].setIsRed(True)
                    else:
                        grid_vertex_edges[edge_id].setIsGreen(True)       
           
            if bool(eastNode):
                edge_id = str(l)+ str(l+gridSize+1)
                if edge_id in grid_vertex_edges.keys():
                    if crime >= threshold:
                        grid_vertex_edges[edge_id].setIsRed(True)
                    else:
                        grid_vertex_edges[edge_id].setIsGreen(True)   
                else:
                    grid_vertex_edges[edge_id] = Edge(nodeAtFocus,eastNode)
                    if crime >= threshold:
                        grid_vertex_edges[edge_id].setIsRed(True)
                    else:
                        grid_vertex_edges[edge_id].setIsGreen(True) 

            if bool(northNode) and bool(northEastNode):
                edge_id = str(l+1)+ str(l+gridSize+2)
                if edge_id in grid_vertex_edges.keys():
                    if crime >= threshold:
                        grid_vertex_edges[edge_id].setIsRed(True)
                    else:
                        grid_vertex_edges[edge_id].setIsGreen(True)   
                else:
                    grid_vertex_edges[edge_id] = Edge(northNode,northEastNode)
                    if crime >= threshold:
                        grid_vertex_edges[edge_id].setIsRed(True)
                    else:
                        grid_vertex_edges[edge_id].setIsGreen(True) 

            if bool(eastNode) and bool(northEastNode):
                edge_id = str(l+gridSize+1)+ str(l+gridSize+2)
                if edge_id in grid_vertex_edges.keys():
                    if crime >= threshold:
                        grid_vertex_edges[edge_id].setIsRed(True)
                    else:
                        grid_vertex_edges[edge_id].setIsGreen(True)   
                else:
                    grid_vertex_edges[edge_id] = Edge(eastNode,northEastNode)
                    if crime >= threshold:
                        grid_vertex_edges[edge_id].setIsRed(True)
                    else:
                        grid_vertex_edges[edge_id].setIsGreen(True) 
           
            #Init diagonal edge number 2
            if bool(eastNode) and bool(northNode):
                edge_id = str(l+gridSize+1)+ str(l+1)
                if edge_id in grid_vertex_edges.keys():
                    if crime >= threshold:
                        grid_vertex_edges[edge_id].setIsRed(True)
                    else:
                        grid_vertex_edges[edge_id].setIsGreen(True)   
                else:
                    grid_vertex_edges[edge_id] = Edge(eastNode,northNode)
                    grid_vertex_edges[edge_id].setIsDiagonal(True)
                    if crime >= threshold:
                        grid_vertex_edges[edge_id].setIsRed(True)
                    else:
                        grid_vertex_edges[edge_id].setIsGreen(True) 
            
            l = l + 1

    # set cost for each type of edge
    for edgekey,edge in grid_vertex_edges.items():
        if edge.isRed is True and edge.isGreen is True and edge.isDiagonal is False:
            edge.setCost(1.3)
            # print("For edge" , edgekey , "Cost = " , edge.cost)
        elif edge.isRed is True and edge.isGreen is False and edge.isDiagonal is False:
            edge.setCost(1.3)
            # print("For edge" , edgekey , "Cost = " , edge.cost)
        elif edge.isRed is False and edge.isGreen is True and edge.isDiagonal is False:
            edge.setCost(1.0)
            # print("For edge" , edgekey , "Cost = " , edge.cost)
        elif edge.isRed is True and edge.isGreen is False and edge.isDiagonal is True:
            edge.setCost(1.5)
            # print("For edge" , edgekey , "Cost = " , edge.cost)
        elif edge.isRed is False and edge.isGreen is True and edge.isDiagonal is True:
            edge.setCost(1.5)
            # print("For edge" , edgekey , "Cost = " , edge.cost)
        else:
            print("No cost assigned to " , edgekey)

    for edgekey,edgeRef in grid_vertex_edges.items():
        if (edgeRef.isRed == True and edgeRef.isGreen == False) or (edgeRef.vertex_to.xCoordinate == x1b and edgeRef.vertex_from.xCoordinate == x1b) or (edgeRef.vertex_to.xCoordinate == x2b and edgeRef.vertex_from.xCoordinate == x2b)or (edgeRef.vertex_to.yCoordinate == y1b and edgeRef.vertex_from.yCoordinate == y1b)or (edgeRef.vertex_to.yCoordinate == y2b and edgeRef.vertex_from.yCoordinate == y2b):
            edgeRef.setIsDisabled(True)
    
    return grid_vertex_edges

def searchVertexKeys(startingPoint,finalPoint,dictOfVertexObjects):
    startingPoint = startingPoint.split(",")
    finalPoint = finalPoint.split(",")
    x1=startingPoint[0]
    y1=startingPoint[1]
    x2=finalPoint[0]
    y2=finalPoint[1]
    vertexKey1 = None
    vertexRef1 = None
    vertexKey2 = None
    vertexRef2 = None
    for key,vertex in dictOfVertexObjects.items():
        if vertex.xCoordinate == float(x1) and vertex.yCoordinate == float(y1):
            vertexKey1 = key
            vertexRef1 = vertex

        if vertex.xCoordinate == float(x2) and vertex.yCoordinate == float(y2):
            vertexKey2 = key
            vertexRef2 = vertex
    
    return vertexKey1,vertexRef1, vertexKey2,vertexRef2
    
def move_cost(currentNode,neighbourNodeRef,dictOfVertexObjects,grid_vertex_edges):
    currentNodeKey= None
    neighbourNodeKey = None
    cost=0
    edgekey=None
    for key,vertexRef in dictOfVertexObjects.items():
        if currentNode.isEquals(vertexRef):
            currentNodeKey = key
        if neighbourNodeRef.isEquals(vertexRef):
            neighbourNodeKey = key
    
    type1 = str(currentNodeKey)+str(neighbourNodeKey)
    type2 = str(neighbourNodeKey)+str(currentNodeKey)
    for edgekey,edgeRef in grid_vertex_edges.items():
        if type1 == edgekey or type2 == edgekey:
            cost = edgeRef.cost
            
    return cost

def getEdgeAccessibility(currentNode,neighbour,dictOfVertexObjects,grid_vertex_edges):
    currentKey=None
    neighbourKey=None
    for key, ref in dictOfVertexObjects.items():
        if ref.isEquals(currentNode):
            currentKey = key 
        if ref.isEquals(neighbour):
            neighbourKey = key

    type1 = str(currentKey)+str(neighbourKey)
    type2 = str(neighbourKey)+str(currentKey)
    edgeKey = None
    for key, ref in grid_vertex_edges.items():
        if key == type1 or key == type2:
            edgeKey = key
            break
    
    return grid_vertex_edges[edgeKey].isDisabled

def findVertexForInputs(startingPoint,finalPoint,dictOfVertexObjects):
    
    startingPoint = str(startingPoint)
    startingPoint = startingPoint.split(",")
    finalPoint = str(finalPoint)
    finalPoint = finalPoint.split(",")
    startingPoint[0] = float(startingPoint[0])
    startingPoint[1] = float(startingPoint[1])
    finalPoint[0] = float(finalPoint[0])
    finalPoint[1] = float(finalPoint[1])

    minx = None
    miny = None
    for key, ref in dictOfVertexObjects.items():
        if (startingPoint[0] >= ref.xCoordinate and startingPoint[1] >= ref.yCoordinate):
            minx =  ref
        if (finalPoint[0] >= ref.xCoordinate and finalPoint[1] >= ref.yCoordinate):
            miny =  ref
    return minx,miny

class Edge:
    def __init__(self,node1,node2):
        self.vertex_to = node1
        self.vertex_from = node2
        self.cost = 0
        self.isRed = False
        self.isGreen = False
        self.isDiagonal = False
        self.isDisabled = False

    def setIsRed(self,decision):
        self.isRed = decision

    def setIsGreen(self,decision):
        self.isGreen = decision

    def setIsDiagonal(self,decision):
        self.isDiagonal = decision

    def setCost(self,cost):
        self.cost = cost

    def setIsDisabled(self,decision):
        self.isDisabled = decision

class Vertex:
    def __init__(self,X,Y,xdistance,ydistance,gridSize): 

        self.parent = None
        self.xCoordinate = X
        self.yCoordinate = Y
        self.H = 0
        self.G = 0
        self.F = 0
        self.neighbours = {'north':{},'north-east':{},'east':{},'south-east':{},'south':{},'south-west':{},'west':{},'north-west':{}}
        self.egdeList = {'north':{},'north-east':{},'east':{},'south-east':{},'south':{},'south-west':{},'west':{},'north-west':{}}
        self.createNeighbours(xdistance,gridSize)

    def __str__(self):
        return str(self.xCoordinate),str(self.yCoordinate)

    def getId(self,X,Y):
        return self

    def isEquals(self,otherNode):
        if(self.xCoordinate == otherNode.xCoordinate and self.yCoordinate == otherNode.yCoordinate):
            return True
        else:
            return False

    def createNeighbours(self,distance,gridSize):
        
        distance = round(distance,2)
        northNeighbour=self.yCoordinate+(distance/gridSize)
        eastNeighbour=self.xCoordinate+(distance/gridSize)
        southNeighbour=self.yCoordinate-(distance/gridSize)
        westNeighbour=self.xCoordinate-(distance/gridSize)

        self.neighbours["north"]["xCoordinate"] = round(self.xCoordinate,3)
        self.neighbours['north']['yCoordinate'] = round(northNeighbour,3)

        self.neighbours["north-east"]["xCoordinate"] = round(eastNeighbour,3)
        self.neighbours['north-east']['yCoordinate'] = round(northNeighbour,3)

        self.neighbours['east']['xCoordinate'] = round(eastNeighbour,3)
        self.neighbours['east']['yCoordinate'] = round(self.yCoordinate,3)

        self.neighbours['south-east']['xCoordinate'] = round(eastNeighbour,3)
        self.neighbours['south-east']['yCoordinate'] = round(southNeighbour,3)

        self.neighbours['south']['xCoordinate'] = round(self.xCoordinate,3)
        self.neighbours['south']['yCoordinate'] = round(southNeighbour,3)

        self.neighbours['south-west']['xCoordinate'] = round(westNeighbour,3)
        self.neighbours['south-west']['yCoordinate'] = round(southNeighbour,3)

        self.neighbours['west']['xCoordinate'] = round(westNeighbour,3)
        self.neighbours['west']['yCoordinate'] = round(self.yCoordinate,3)

        self.neighbours["north-west"]["xCoordinate"] = round(westNeighbour,3)
        self.neighbours['north-west']['yCoordinate'] = round(northNeighbour,3)