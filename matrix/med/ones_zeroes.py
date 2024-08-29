class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, grid):
        # pass
        numOnesRows = [0] * len(grid)
        numOnesCols = [0] * len(grid[0])
        numZeroesRows = [0] * len(grid)
        numZeroesCols = [0] * len(grid[0])
        
        # lets get the ones and zeroes row-wise first:
        for i in range(len(grid)):
            onesCount = 0
            zeroesCount = 0
            
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    onesCount += 1
                else:
                    zeroesCount += 1
            
            numOnesRows[i] = onesCount
            numZeroesRows[i] = zeroesCount
        
        for j in range(len(grid[0])):
            onesCount = 0
            zeroesCount = 0
            
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    onesCount += 1
                else:
                    zeroesCount += 1
                    
            numOnesCols[j] = onesCount
            numZeroesCols[j] = zeroesCount
        
        # print((numOnesRows, numOnesCols, numZeroesRows, numZeroesCols))
        differenceMatrix = [([0] * len(grid[0])) for _ in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                differenceMatrix[i][j] = numOnesRows[i] + numOnesCols[j] - numZeroesRows[i] - numZeroesCols[j]
        
        return differenceMatrix

def main():
    solver = Solution()

    #solver.solver()
    print(solver.solver(grid = [[0,1,1],[1,0,1],[0,0,1]]))
    """
        0 1 1
        1 0 1
        0 0 1
    """
    
    print(solver.solver(grid = [[1,1,1],[1,1,1]]))
    """
        1 1 1
        1 1 1
    """
    # print(solver.solver())

if __name__ == "__main__":
    main()