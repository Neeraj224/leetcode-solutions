class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums):
        nums.sort()
        
        return nums[len(nums) // 2]
        
def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [3,2,3]))
    print(solver.solver(nums = [2,2,1,1,1,2,2]))

if __name__ == "__main__":
    main()