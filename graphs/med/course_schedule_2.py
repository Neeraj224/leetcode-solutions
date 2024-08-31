class Graph:
    def __init__(self, numNodes, edges):
        self.numNodes = numNodes
        self.edges = edges
        self.adjacencyList = {}
        self.visited = set()
        self.traversed = []
        self.indegrees = {}
        self.order = []
    
    def buildGraph(self):
        for edge in self.edges:
            if edge[1] not in self.adjacencyList:
                self.adjacencyList[edge[1]] = []
            self.adjacencyList[edge[1]].append(edge[0])
    
    def initialiseIndegrees(self):
        for i in range(self.numNodes):
            self.indegrees[i] = 0
    
    def printGraph(self):
        print(self.adjacencyList)
        
    def dfs(self, node):
        if node in self.visited:
            self.indegrees[node] += 1
            return node
        
        self.visited.add(node)
        self.traversed.append(node)
        
        if node not in self.adjacencyList:
            return node
        
        if self.adjacencyList[node] is not None:
            for neighbor in self.adjacencyList[node]:
                self.dfs(neighbor)
        
        return node
    
class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, numCourses, prerequisites):
        # # pass
        # graph = Graph(numCourses, prerequisites)
        # graph.buildGraph()
        # # graph.printGraph()
        # graph.initialiseIndegrees()
        # graph.dfs(0)
        
        # sorted_order = list(sorted(graph.indegrees, key = lambda k: graph.indegrees[k]))
        # return sorted_order
        # build the adjacency list of the graph first:
        adj_list = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        # states:
        #       0   -> unvisited
        #       -1  -> on path
        #       1   -> visited
        visited = [0] * numCourses
        # for the topological sort order
        sorted_order = []

        def dfs(course):
            # if the one we are visiting is on the current path
            # that means we found a cylce, so we need to return False
            if visited[course] == -1:
                return False
            # if we already explored this course node, and its not on the path
            # that means no cycle exists
            if visited[course] == 1:
                return True
            
            # else we mark it as on the path:
            visited[course] = -1

            # now we visit all the prerequisites:
            for prereq in adj_list[course]:
                # if any of them is on the path, and hence cant be completed,
                # we return false
                if dfs(prereq) == False:
                    return False
                
            # mark the course as visited once all the 
            # neighbors (prerequisites) have been explored:
            visited[course] = 1
            # add the course to the order:
            sorted_order.append(course)

            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return []
        
        return sorted_order

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(numCourses = 2, prerequisites = [[1,0]]))
    print(solver.solver(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))
    print(solver.solver(numCourses = 1, prerequisites = []))

if __name__ == "__main__":
    main()