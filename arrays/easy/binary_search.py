class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums, target):
        # pass
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        
        return -1
        
def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [-1,0,3,5,9,12], target = 9))
    print(solver.solver(nums = [-1,0,3,5,9,12], target = 2))
    # print(solver.solver())

if __name__ == "__main__":
    main()