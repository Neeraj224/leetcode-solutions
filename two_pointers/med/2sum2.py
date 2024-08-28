class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums, target):
        # pass
        hashnums = list(set(nums))
        hashnums.sort()
        print(hashnums)
        
        indices = []
        
        for i in range(0, len(nums) - 1):
            diff = target - nums[i]
            if diff in hashnums:
                indices.append(i + 1)
                indices.append(nums.index(diff) + 1)
                return indices
        
        return indices

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [2,7,11,15], target = 9))
    print(solver.solver(nums = [2,3,4], target = 6))
    print(solver.solver(nums = [-1,0], target = -1))

if __name__ == "__main__":
    main()