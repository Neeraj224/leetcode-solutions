class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums: list[int], target: int):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
            
                

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [2,7,11,15], target = 9))
    print(solver.solver(nums = [3,2,4], target = 6))
    print(solver.solver(nums = [3,3], target = 6))
    print(solver.solver(nums = [0,4,3,0], target = 0))

if __name__ == "__main__":
    main()