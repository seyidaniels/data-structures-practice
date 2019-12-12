class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbours = list()
        self.distance = 9999
        self.color = 'black'

    def addNeighbour(self, neighbourName):
        if neighbourName not in self.neighbours:
            self.neighbours.append(neighbourName)
            self.neighbours.sort()


class Graph:
    vertices = {}

    def addVertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def addEdge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for name, vertex in self.vertices.items():
                if name == u:
                    vertex.addNeighbour(v)
                if name == v:
                    vertex.addNeighbour(u)

    def printGraph(self):
        for key in sorted(list(self.vertices)):
            print(
                key + str(self.vertices[key].neighbours) + str(self.vertices[key].distance))

    def breathFirstSearch(self, vertice):
        q = list()
        vertice.distance = 0
        vertice.color = 'red'

        for v in vertice.neighbours:
            self.vertices[v].distance = vertice.distance + 1
            q.append(v)

        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.color = 'red'

            for visiting in node_u.neighbours:
                node_v = self.vertices[visiting]
                if node_v.color == 'black':
                    q.append(visiting)

                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1


graph = Graph()

a = Vertex('A')

graph.addVertex(a)

graph.addVertex(Vertex('A'))

for i in range(ord('A'), ord('K')):
    graph.addVertex(Vertex(chr(i)))


edges = [
    'AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI'
]

for edge in edges:
    graph.addEdge(edge[:1], edge[1:])


graph.breathFirstSearch(a)

graph.printGraph()
