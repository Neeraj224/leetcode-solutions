class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return nums
        
        zero_count = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            
        def float_zero(nums):
            for i in range(len(nums) - 1):
                if nums[i] == 0:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
        
        for i in range(zero_count):
            float_zero(nums)
        
        return nums

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [0,1,0,3,12]))
    print(solver.solver(nums = [0]))

if __name__ == "__main__":
    main()