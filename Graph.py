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
        # self.id = id
        self.parent = None
        self.xCoordinate = X
        self.yCoordinate = Y
        self.H = 0
        self.G = 0
        self.F = 0
        self.neighbours = {'north' :{},'east':{},'south':{},'west':{}}
        self.createNeighbours()
        
    # def getId(self,xCoordinate,yCoordinate):
        # return self.id

    def __str__(self):
        return str(self.xCoordinate),str(self.yCoordinate)

    def createNeighbours(self):
        gridSize = 2
        eastNeighbour=self.xCoordinate+(gridSize*(1/100))
        westNeighbour=self.xCoordinate-(gridSize*(1/100))
        northNeighbour=self.yCoordinate+(gridSize*(1/100))
        southNeighbour=self.yCoordinate-(gridSize*(1/100))

        self.neighbours["north"]["xCoordinate"] = self.xCoordinate
        self.neighbours['north']['yCoordinate'] = northNeighbour

        self.neighbours['east']['xCoordinate'] = eastNeighbour
        self.neighbours['east']['yCoordinate'] = self.yCoordinate

        self.neighbours['south']['xCoordinate'] = self.xCoordinate
        self.neighbours['south']['yCoordinate'] = southNeighbour

        self.neighbours['west']['xCoordinate'] = westNeighbour
        self.neighbours['west']['yCoordinate'] = self.yCoordinate

        # self.neighbours["north"] = self.xCoordinate,northNeighbour
        # self.neighbours['east'] = eastNeighbour,self.yCoordinate
        # self.neighbours['south'] = self.xCoordinate,southNeighbour
        # self.neighbours['west'] = westNeighbour,self.yCoordinate

        # print("East"   ,eastNeighbour,self.yCoordinate)
        # print("West"    ,westNeighbour,self.yCoordinate)
        # print("North"   ,self.xCoordinate,northNeighbour)
        # print("South"   ,self.xCoordinate,southNeighbour)

    def get_Neighbours(self):
        return self.neighbours.values()

class Graph:
    def __init__(self):
        self.num_vertices = 0
        self.vert_dict = {}

    def add_vertex(self,vertex):
        self.num_vertices = self.num_vertices + 1
        self.vert_dict[vertex] = vertex
        # return new_vertex
    
    def get_vertices(self):
        return self.vert_dict.keys()

def createVertexes(listofcoordinates):
    grid_vertex_objects = {}
    vertex_id = 0
    for coordinate in listofcoordinates:
        vertex_id += 1
        grid_vertex_objects[vertex_id] = Vertex(coordinate['X'],coordinate['Y'])



# if __name__ == '__main__':
    
#     g = Graph()
#     v1 = Vertex(1,-73.59,45.49)
#     v2 = Vertex(2,-73.59,45.51)
#     # v3 = Vertex(3,-73.59,45.53)
#     # v4 = Vertex(4,-73.57,45.49)

#     g.add_vertex(v1)
#     g.add_vertex(v2)
#     # g.add_vertex(v3)
#     # g.add_vertex(v4)

#     a = astar(g,v1,v2)
#     print(a)
#     # print("Number of current Vertices " , g.num_vertices)
#     # print("\n") 
#     # # print("Which is/are " , g.get_vertices()) 
#     # print("\n") 
#     # print("Its Neighbours are " , v1.get_Neighbours()) 
#     # print("\n") 


















#   for grapg class
    # def add_neighbor(self, neighbor, weight=0):
    #     self.adjacent[neighbor] = weight

    # def get_connections(self):
    #     return self.adjacent.keys()  

    # def get_id(self):
    #     return self.id

    # def get_weight(self, neighbor):
    #     return self.adjacent[neighbor]






    # g.add_edge('a', 'b', 7)  
    # g.add_edge('a', 'c', 9)
    # g.add_edge('a', 'f', 14)
    # g.add_edge('b', 'c', 10)
    # g.add_edge('b', 'd', 15)
    # g.add_edge('c', 'd', 11)
    # g.add_edge('c', 'f', 2)
    # g.add_edge('d', 'e', 6)
    # g.add_edge('e', 'f', 9)

    # for v in g:
    #     for w in v.get_connections():
    #         vid = v.get_id()
    #         wid = w.get_id()
    #         print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))

    # for v in g:
    #     print 'g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()])