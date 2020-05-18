class Vertex:
    def __init__(self,id,X,Y):

        self.id = id
        self.xCoordinate = X
        self.yCoordinate = Y
        self.adjacent = {}
        self.createNeighbours()

    def __str__(self):
        return str(self.xCoordinate),str(self.yCoordinate)

    def createNeighbours(self):

        gridSize = 2
        eastNeighbour=self.xCoordinate+gridSize*(1/100)
        westNeighbour=self.xCoordinate-(gridSize*(1/100))
        northNeighbour=self.yCoordinate+(gridSize*(1/100))
        southNeighbour=self.yCoordinate+(gridSize*(1/100))
       
        self.adjacent['east'] = eastNeighbour,self.yCoordinate
        self.adjacent['west'] = westNeighbour,self.yCoordinate
        self.adjacent['north'] = self.xCoordinate,northNeighbour
        self.adjacent['south'] = self.xCoordinate,southNeighbour

        # print("East"   ,eastNeighbour,self.yCoordinate)
        # print("West"    ,westNeighbour,self.yCoordinate)
        # print("North"   ,self.xCoordinate,northNeighbour)
        # print("South"   ,self.xCoordinate,southNeighbour)

    def get_Neighbours(self):
        return self.adjacent.keys()


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


if __name__ == '__main__':
    
    g = Graph()
    v = Vertex(1,-73.59,45.49)
    g.add_vertex(v)
    # g.add_vertex(2,-73.59,45.51)
    # g.add_vertex(3,-73.59,45.53)
    # g.add_vertex(4,-73.57,45.49)

    print("Number of current Vertices " , g.num_vertices)
    print("\n") 
    print("Which is/are " , g.get_vertices()) 
    print("\n") 
    print("Its Neighbours are " , g.get_Neighbours()) 
    print("\n") 


















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