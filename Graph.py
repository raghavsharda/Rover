import numpy as np
import math

def astar(graphcongif, initialCoordinate, finalCoordinate):
    
    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(initialCoordinate)

    # Loop until you find the end
    while len(open_list) > 0:
        
        # Get the current node
        current = min(open_list, key=lambda o:o.G + o.H)

        #If it is the item we want, retrace the path and return it
        if current.id == finalCoordinate.id:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]
        
        #Remove the item from the open set
        open_list.remove(current)

        #Add it to the closed set
        closed_list.append(current)

        # Loop through the node's children/neighbour
        for direction,coordinatesOfChildren in current.neighbours.items():
            #If the children is already in the closed set, skip it
            for node in closed_list:
                if (coordinatesOfChildren['xCoordinate'] == node.xCoordinate) and (coordinatesOfChildren['yCoordinate'] == node.yCoordinate):
                    print ("Node has already been visited")
                    continue
            
            for node in open_list:
                continue
                # Check if we beat the G score 
                # new_g = current.G + current.move_cost()
                # if node.G > new_g:
                #     #If so, update the node to have a new parent
                #     node.G = new_g
                #     node.parent = current

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

    def createNeighbours(self,distance,gridSize):
        
        distance = np.floor(distance)
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

def createVertex(listofcoordinates,xdistance,ydistance,gridSize):
    grid_vertex_objects = {}
    vertex_id = 0
    for coordinate in listofcoordinates:
        x = round(coordinate['X'],3)
        y = round(coordinate['Y'],3)
        grid_vertex_objects[vertex_id] = Vertex(x,y,xdistance,ydistance,gridSize)
        vertex_id += 1
    return grid_vertex_objects

def createMatrix(dictOfVertexObjects):
    data = list(dictOfVertexObjects.items()) 
    an_array = np.array(data)
    print(an_array)

def makeFriends(dictOfVertexObjects):
    # iterate over dict of objects
    for node in dictOfVertexObjects.values():
        # check if neighbours are already exsisting nodes
        for x in dictOfVertexObjects.values():
            if node.neighbours['north']['xCoordinate'] == x.xCoordinate and node.neighbours['north']['yCoordinate'] == x.yCoordinate:
                node.egdeList['north'] = x
            if node.neighbours['north-east']['xCoordinate'] == x.xCoordinate and node.neighbours['north-east']['yCoordinate'] == x.yCoordinate:
                node.egdeList['north-east'] = x
            if node.neighbours['east']['xCoordinate'] == x.xCoordinate and node.neighbours['east']['yCoordinate'] == x.yCoordinate:
                node.egdeList['east'] = x
            if node.neighbours['south-east']['xCoordinate'] == x.xCoordinate and node.neighbours['south-east']['yCoordinate'] == x.yCoordinate:
                node.egdeList['south-east'] = x
            if node.neighbours['south']['xCoordinate'] == x.xCoordinate and node.neighbours['south']['yCoordinate'] == x.yCoordinate:
                node.egdeList['south'] = x
            if node.neighbours['west']['xCoordinate'] == x.xCoordinate and node.neighbours['west']['yCoordinate'] == x.yCoordinate:
                node.egdeList['west'] = x
            if node.neighbours['south-west']['xCoordinate'] == x.xCoordinate and node.neighbours['south-west']['yCoordinate'] == x.yCoordinate:
                node.egdeList['south-west'] = x
            if node.neighbours['north-west']['xCoordinate'] == x.xCoordinate and node.neighbours['north-west']['yCoordinate'] == x.yCoordinate:
                node.egdeList['north-west'] = x
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
        # key = str(x)+str(y)
        key = x+y
        # key = key.replace("-", "")
        # key = key.replace(".", "")
        print(key)
        return key

class Edge:
    def __init__(self,node1,node2):
        self.vertex_to = node1
        self.vertex_from = node2
        self.cost = 0
        self.isRed = False
        self.isGreen = False
        self.isDiagonal = False

    def setIsRed(self,decision):
        self.isRed = decision

    def setIsGreen(self,decision):
        self.isGreen = decision

    def setIsDiagonal(self,decision):
        self.isDiagonal = decision

    def setCost(self,cost):
        self.cost = cost

def setHighCrimeAreas(crimeRates,dictOfVertexObjects,gridSize,threshold):
    keysofdict = list(dictOfVertexObjects)
    grid_vertex_edges = {}
    edge_id = None
    l = -1
    for crimes in crimeRates:
        # skip the nth postion
        l = l + 1
        for crime in crimes:
            nodeAtFocus = dictOfVertexObjects[keysofdict[l]]
            print("This is focus node" ,nodeAtFocus.xCoordinate ,nodeAtFocus.yCoordinate)
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
    for edge in grid_vertex_edges.values():
        if edge.isRed is True and edge.isGreen is True and edge.isDiagonal is False:
            edge.setCost(1.3)
        if edge.isRed is False and edge.isGreen is True and edge.isDiagonal is False:
            edge.setCost(1.0)
        if edge.isRed is True and edge.isGreen is False and edge.isDiagonal is True:
            edge.setCost(1.5)

    # Put break here to Debug , and expand and see grid_vertex_edges
    print("Total number of edges ",len(grid_vertex_edges))
    return grid_vertex_edges
