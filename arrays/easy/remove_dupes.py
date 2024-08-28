class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums: list[int]):
        PLACEHOLDER = 999
        
        if len(nums) == 0 or len(nums) == 1:
            return nums
        
        i = 0
        j = i + 1
        count_k = 0
        
        while i < len(nums) or j < len(nums):
            if nums[i] == nums[j]:
                nums[j] = PLACEHOLDER
                count_k += 1
                if j == len(nums) - 1:
                    break
                j += 1
            elif nums[i] != nums[j]:
                i = j
                if i == len(nums) - 1:
                    break
                else:
                    j = i + 1
        
        nums.sort()
        return nums

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [1,1,2]))
    print(solver.solver(nums = [1,1,1]))
    print(solver.solver(nums = [0,0,1,1,1,2,2,3,3,4]))
    #print(solver.solver())

if __name__ == "__main__":
    main()