class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, mat):
        primary = 0
        secondary = 0

        for i in range(len(mat)):
            primary += mat[i][i]
        

        i = 0
        j = len(mat[0]) - 1

        while i < len(mat) and j >= 0:
            if i == j:
                i += 1
                j -= 1
                continue
            
            secondary += mat[i][j]
            
            i += 1
            j -= 1
          
        return primary + secondary

def main():
    solver = Solution()
    
    #solver.solver()
    mat1 =  [[1,2,3],
              [4,5,6],
              [7,8,9]]
    
    mat2 = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
    
    mat3 = [[5]]
    
    print(solver.solver(mat1))
    print(solver.solver(mat2))
    print(solver.solver(mat3))

if __name__ == "__main__":
    main()