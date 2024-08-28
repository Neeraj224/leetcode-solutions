class Graph:
    def __init__(self, numNodes, edges):
        self.numNodes = numNodes
        self.edges = edges
        self.adjacencyList = [[] for _ in range(0, self.numNodes)]
        self.adjacencyMatrix = [([0] * self.numNodes) for _ in range(0, self.numNodes)]
        # the visited map is used mainly forrrrrrr DFS!
        self.visited = {}
    
    def addEdge(self, u, v, bidirectional = False):
        self.adjacencyList[u].append(v)
        
        if bidirectional:
            self.adjacencyList[v].append(u)
    
    def buildAdjacencyMatrix(self, edges, bidirectional = False):
        for i, j in edges:
            self.adjacencyMatrix[i][j] = 1
            if bidirectional:
                self.adjacencyMatrix[j][i] = 1
        
        for row in self.adjacencyMatrix:
            print(row)
    
    # def bfs(self, node):
    #     self.visited = {}
    #     queue = []
        
    def printGraph(self):
        for node in range(len(self.adjacencyList)):
            print(node, end = ": ")
            print(self.adjacencyList[node])
    
    def getNumNeighbors(self, node):
        return len(self.adjacencyList[node])
    

def main():
    edges = [[0, 1], [0, 2], [1, 3], [2, 3], [4, 2], [4, 5]]
    graph1 = Graph(6, edges)
    
    for edge in edges:
        graph1.addEdge(edge[0], edge[1], bidirectional=True)
    
    graph1.printGraph()
    
    popped = []
    def dfs(node):
        if node in graph1.visited:
            return node
        
        graph1.visited[node] = 1
        popped.append(node)

        if graph1.adjacencyList[node] is not None:
            for neighbor in graph1.adjacencyList[node]:
                dfs(neighbor)
        
        return node
    
    dfs(1)
    print(popped)
    
    print(graph1.getNumNeighbors(2))
    
    sumOfDegrees = 0
    
    for node in popped:
        sumOfDegrees += graph1.getNumNeighbors(node)
    
    if sumOfDegrees == 2 * len(edges):
        print("correct!")
        
    graph1.buildAdjacencyMatrix(edges, True)

if __name__ == "__main__":
    main()