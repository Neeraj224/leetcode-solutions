class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums: list[int]):
        # pass
        nums = list(set(nums))
        nums.sort()
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        # print(nums)
        maxcount = float("-inf")
        count = 0
        i = 0
        
        while i <= len(nums) - 2:
            if nums[i] + 1 == nums[i + 1]:
                count += 1
            else:
                count = 0
            maxcount = max(count, maxcount)
            i += 1
        
        return maxcount + 1
            

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [100,4,200,1,3,2]))
    print(solver.solver(nums = [0,3,7,2,5,8,4,6,0,1]))
    # print(solver.solver())

if __name__ == "__main__":
    main()