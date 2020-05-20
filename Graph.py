import numpy as np

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
    def __init__(self,X,Y): 

        self.parent = None
        self.xCoordinate = X
        self.yCoordinate = Y
        self.H = 0
        self.G = 0
        self.F = 0
        self.neighbours = {'north':{},'north-east':{},'east':{},'south-east':{},'south':{},'south-west':{},'west':{},'north-west':{}}
        self.egdeList = []
        self.createNeighbours()

    def setEgdeList(self ,node):
        self.egdeList.append(node)

    def __str__(self):
        return str(self.xCoordinate),str(self.yCoordinate)

    def getId(self,X,Y):
        return self

    def createNeighbours(self):
        
        # To-Do make this section more dynamic
        distance = 0.04
        gridsize = 2
        # gridsize = 20
        northNeighbour=self.yCoordinate+(distance/gridsize)
        eastNeighbour=self.xCoordinate+(distance/gridsize)
        southNeighbour=self.yCoordinate-(distance/gridsize)
        westNeighbour=self.xCoordinate-(distance/gridsize)

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

def createVertex(listofcoordinates):
    grid_vertex_objects = {}
    vertex_id = 0
    for coordinate in listofcoordinates:
        vertex_id += 1
        grid_vertex_objects[vertex_id] = Vertex(coordinate['X'],coordinate['Y'])
        # grid_vertex_objects[vertex_id].update()Vertex(coordinate['X'],coordinate['Y'])
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
                node.egdeList.append(x)
            if node.neighbours['north-east']['xCoordinate'] == x.xCoordinate and node.neighbours['north-east']['yCoordinate'] == x.yCoordinate:
                node.egdeList.append(x)
            if node.neighbours['east']['xCoordinate'] == x.xCoordinate and node.neighbours['east']['yCoordinate'] == x.yCoordinate:
                node.setEgdeList(x)
            if node.neighbours['south-east']['xCoordinate'] == x.xCoordinate and node.neighbours['south-east']['yCoordinate'] == x.yCoordinate:
                node.setEgdeList(x)
            if node.neighbours['south']['xCoordinate'] == x.xCoordinate and node.neighbours['south']['yCoordinate'] == x.yCoordinate:
                node.setEgdeList(x)
            if node.neighbours['west']['xCoordinate'] == x.xCoordinate and node.neighbours['west']['yCoordinate'] == x.yCoordinate:
                node.setEgdeList(x)
            if node.neighbours['south-west']['xCoordinate'] == x.xCoordinate and node.neighbours['south-west']['yCoordinate'] == x.yCoordinate:
                node.setEgdeList(x)
            if node.neighbours['north-west']['xCoordinate'] == x.xCoordinate and node.neighbours['north-west']['yCoordinate'] == x.yCoordinate:
                node.egdeList.append(x)
            else:
                pass

# class Graph:
#     def __init__(self):
#         self.num_vertices = 0
#         self.vert_dict = {}

#     def add_vertex(self,vertex):
#         self.num_vertices = self.num_vertices + 1
#         self.vert_dict[vertex] = vertex
#         # return new_vertex
    
#     def get_vertices(self):
#         return self.vert_dict.keys()