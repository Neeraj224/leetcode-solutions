class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, grid):
        max_rows = [0] * len(grid)
        max_cols = [0] * len(grid[0])

        for i in range(len(grid)):
            max_rows[i] = max(grid[i])
        
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                max_cols[j] = max(grid[i][j], max_cols[j])
        
        total_sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                    total_sum += min(max_rows[i], max_cols[j]) - grid[i][j]
        
        # print(grid)
        return total_sum

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))
    print(solver.solver(grid = [[0,0,0],[0,0,0],[0,0,0]]))
    print(solver.solver([[34,77,85,90],[50,78,1,34],[77,1,14,58],[60,2,48,3]]))

if __name__ == "__main__":
    main()
