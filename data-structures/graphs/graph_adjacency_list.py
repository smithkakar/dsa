#!/usr/local/bin/env python3
class Vertex:

    def __init__(self, key):
        self.id = key
        # adjacency list in the form of dictionary
        self.connections = {}

    # adds a connection from this vertex to another
    def addNeighbor(self, nbr, weight=0):
        self.connections[nbr] = weight

    def __str__(self):
        return str(self.id) + ' is connected to: ' + str([x.id for x in self.connections])

    # all the vertices in the adjacency list
    def getConnections(self):
        return self.connections.keys()

    def getId(self):
        return self.id

    #  weight of the edge from this vertex to the vertex passed as a parameter
    def getWeight(self, nbr):
        return self.connections[nbr]


'''
graph as an adjacency list
'''


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        self.numVertices += 1

    def addEdge(self, fromVert, toVert, weight=0):
        if fromVert not in self.vertList:
            newVert = self.addVertex(fromVert)
        if toVert not in self.vertList:
            newVert = self.addVertex(toVert)

        self.vertList[fromVert].addNeighbor(self.vertList[toVert], weight)

    def getVertex(self, vertKey):
        if vertKey in self.vertList:
            return self.vertList[vertKey]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


g = Graph()
for i in range(6):
    g.addVertex(i)

g.addEdge(0, 1, 2)

for vertex in g:
    print(f'vertex: {vertex}')
    print(f'vertex connections: {vertex.getConnections()}')
    print('\n')
