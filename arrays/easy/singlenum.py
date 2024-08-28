class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return nums[0]
        
        counts = dict()
        
        for i in range(len(nums)):
            if nums[i] not in counts:
                counts[nums[i]] = 1
            else:
                counts[nums[i]] += 1
        
        for key in counts:
            if counts[key] == 1:
                return key
        

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [2,2,1]))
    print(solver.solver(nums = [4,1,2,1,2]))
    print(solver.solver(nums = [1]))

if __name__ == "__main__":
    main()