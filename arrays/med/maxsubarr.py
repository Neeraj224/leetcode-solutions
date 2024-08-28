class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums):
        maximum = float("-inf")
        total = 0
        
        for i in range(len(nums)):
            total += nums[i]
            
            if total > maximum:
                maximum = total
            
            if total < 0:
                total = 0
                
        return maximum
        
def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [-2,1,-3,4,-1,2,1,-5,4]))
    print(solver.solver(nums = [1]))
    print(solver.solver(nums = [5,4,-1,7,8]))

if __name__ == "__main__":
    main()