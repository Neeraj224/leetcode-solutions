class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, matrix: list[list[int]], target: int):
        # pass
        row = -1
        
        for i in range(len(matrix)):
            if target > matrix[i][0] and target <= matrix[i][-1]:
                row = i
                break
            elif target == matrix[i][0]:
                return True
        
        if row == -1:
            return False
        
        # print(row)
        left = 0
        right = len(matrix[row]) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
            elif target == matrix[row][mid]:
                return True

        return False
        
def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
    print(solver.solver(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
    print(solver.solver(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 30))
    print(solver.solver(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 11))


if __name__ == "__main__":
    main()