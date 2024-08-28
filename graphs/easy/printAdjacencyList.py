class Solver:
    def printGraph(self, V : int, edges : list[list[int]]) -> list[list[int]]:
        self.totalNodes = V
        self.adjacencyList = [[] for _ in range(0, self.totalNodes)]
        print(self.adjacencyList) 
        
        def addEdge(u, v):
            self.adjacencyList[u].append(v)
            self.adjacencyList[v].append(u)
        
        for i in range(len(edges)):
            addEdge(edges[i][0], edges[i][1])
        
        print(self.adjacencyList)
            
def main():
    solver = Solver()
    edges = [[0,1], [0,4], [4,1], [4,3], [1,3], [1,2], [3,2]]
    solver.printGraph(5, edges)
    
    edges2 = [[0,3], [0,2], [2,1]]
    solver.printGraph(4, edges2)
    
    
if __name__ == "__main__":
    main()