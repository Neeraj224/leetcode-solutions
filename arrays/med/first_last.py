class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums: list[int], target: int):
        if len(nums) == 0:
            return [-1, -1]

        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if target < nums[mid]:
                high = mid - 1
            
            if target > nums[mid]:
                low = mid + 1
            
            if target == nums[mid] and low == mid - 1 and nums[low] == target:
                return [mid - 1, mid]
            
            if target == nums[mid] and high == mid + 1 and nums[high] == target:
                return [mid, mid + 1]
            
            if target == nums[mid]:
                return [mid, mid]
        
        if low > high:
            return [-1, -1]

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [5,7,7,8,8,10], target = 8))
    print(solver.solver(nums = [5,7,7,8,8,10], target = 6))
    print(solver.solver(nums = [], target = 0))
    print(solver.solver(nums = [2, 2], target = 2))
    print(solver.solver(nums = [1, 3], target = 1))

if __name__ == "__main__":
    main()