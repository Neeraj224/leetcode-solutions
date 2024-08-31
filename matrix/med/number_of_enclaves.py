class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, grid):
        # pass
        edgeboard = [([0] * len(grid[0])) for _ in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1) and grid[i][j] == 1:
                    edgeboard[i][j] = 'E'
                else:
                    edgeboard[i][j] = grid[i][j]
        
        queue = []
        
        def dfs(row, col):
            if edgeboard[row][col] == 'V' or edgeboard[row][col] == 0:
                return
            
            elif edgeboard[row][col] == 1 or edgeboard[row][col] == 'E':
                queue.append((row, col))
                edgeboard[row][col] = 'V'
            
            if row - 1 >= 0:
                # up
                dfs(row - 1, col)
            if col + 1 < len(edgeboard[0]):
                # right
                dfs(row, col + 1)
            if row + 1 < len(edgeboard):
                # down
                dfs(row + 1, col)
            if col - 1 >= 0:
                # left
                dfs(row, col - 1)
            
        for i in range(len(edgeboard)):
            for j in range(len(edgeboard[0])):
                if edgeboard[i][j] == 'E':
                    dfs(i, j)
        
        count = 0
        for i in range(len(edgeboard)):
            for j in range(len(edgeboard[0])):
                if edgeboard[i][j] == 1:
                    count += 1
        
        return count

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))
    print(solver.solver(grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))
    # print(solver.solver())

if __name__ == "__main__":
    main()