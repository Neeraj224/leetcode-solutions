class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, target: int, nums: list[int]):
        count = float("inf")
        
        for i in range(len(nums)):
            if nums[i] >= target:
                return 1
            else:
                subarrsum = nums[i]
                current_count = 1
                j = i + 1

                while subarrsum < target and j < len(nums):
                    subarrsum += nums[j]
                    current_count += 1
                    j += 1
                
                if subarrsum == target:
                    count = min(current_count, count)
                    current_count = 0
                elif subarrsum > target:
                    count = min(current_count, count)
                    current_count = 0
        
        if count == float("inf"):
            return 0
        
        return count
        
def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(target = 7, nums = [2,3,1,2,4,3]))
    print(solver.solver(target = 4, nums = [1,4,4]))
    print(solver.solver(target = 11, nums = [1,1,1,1,1,1,1,1]))
    print(solver.solver(target = 80, nums = [10,5,13,4,8,4,5,11,14,9,16,10,20,8]))

if __name__ == "__main__":
    main()