class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, grid):
        # pass
        resultMatrix = [([0] * (len(grid) - 2)) for _ in range(len(grid) - 2)]
        localMaxes = []
        
        def print3x3SubMatrix(grid, windowSize):
            for i in range(0, len(grid) - (windowSize - 1)):
                for j in range(0, len(grid[i]) - (windowSize - 1)):
                    maxLocal = float("-inf")
                    for k in range(i, i + windowSize):
                        for l in range(j, j + windowSize):
                            maxLocal = max(maxLocal, grid[k][l])

                    if maxLocal >= grid[k][l]:
                        localMaxes.append(maxLocal)
        
        print3x3SubMatrix(grid, 3)
        lmi = 0
        
        for i in range(len(resultMatrix)):
            for j in range(len(resultMatrix[i])):
                resultMatrix[i][j] = localMaxes[lmi]
                lmi += 1
        
        return resultMatrix

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))
    print(solver.solver(grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))
    # print(solver.solver())

if __name__ == "__main__":
    main()