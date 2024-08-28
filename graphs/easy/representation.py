"""
    For now this is gonna be a very basic representation of Graphs
"""
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(0, self.num_vertices)]
        self.visited = {}
        self.dfsTraversal = []
        # print(self.adj_list)
    
    def add_edge(self, u, v, bidirectional = False):
        """
            Adds an edge from u to v, and if bidirectional is True,
            also adds from v to u:
        """
        self.adj_list[u].append(v)
        
        if bidirectional:
            self.adj_list[v].append(u)
    
    def get_neighbors(self, u):
        """
            returns the neighbors of the vertex u
        """
        return self.adj_list[u]

    def display(self):
        for i in range(0, self.num_vertices):
            print(f"Vertex {i}: {self.adj_list[i]}")
    
    def searchNodes(self, node):
        if node in self.visited:
            return node
        
        self.visited[node] = 1
        self.dfsTraversal.append(node)
        
        for neighbor in self.get_neighbors(node):
            print(neighbor)
            self.searchNodes(neighbor)
        
        return node
        
    
def main():
    adjList = [[2,3],[1,3],[2,3],[1,3]]
    graph1 = Graph(len(adjList))
    
    for i in range(0, len(adjList)):
        for j in range(0, len(adjList[i])):
            # print([i + 1, adjList[i][j]])
            graph1.add_edge(i, adjList[i][j])
    
    # graph1.display()
    graph1.searchNodes(0)
    print(graph1.dfsTraversal)
    
if __name__ == "__main__":
    main()