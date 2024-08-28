class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums, target):
        # pass
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if target == nums[mid]:
                return mid
            
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [4,5,6,7,0,1,2], target = 0))
    print(solver.solver(nums = [4,5,6,7,0,1,2], target = 3))
    print(solver.solver(nums = [1], target = 0))

if __name__ == "__main__":
    main()