class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, isConnected):
        # pass
        adjList = [[] for _ in range(len(isConnected))]
        # print(adjList)
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                # print((i, j))
                if i == j:
                    # if isConnected[i][j] == 1:
                    #     adjList[i].append(j)
                    continue
                else:
                    if isConnected[i][j] == 1:
                        # print((i, j))
                        adjList[i].append(j)
                    else:
                        continue
        
        
        numProvinces = 0
        provincesVisited = [False] * len(adjList)
        
        for i in range(len(adjList)):
            # print(provincesVisited)
            if provincesVisited[i] == True:
                continue
            else:
                provincesVisited[i] = True
                numProvinces += 1
                
                queue = []
                visited = []
                
                queue.append(i)
                visited.append(i)
                
                while queue:
                    current = queue.pop(0)
                    # print(current)
                    provincesVisited[current] = True
                    
                    if adjList[current] is not None:
                        for neighbor in adjList[current]:
                            if neighbor not in visited:
                                
                                visited.append(neighbor)
                                queue.append(neighbor)
        
        return numProvinces
                
                
            

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(isConnected = [[1,1,0],[1,1,0],[0,0,1]]))
    print(solver.solver(isConnected = [[1,0,0],[0,1,0],[0,0,1]]))
    # print(solver.solver())

if __name__ == "__main__":
    main()