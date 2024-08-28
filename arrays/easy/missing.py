class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums: list[int]):
        counts = [0] * (len(nums) + 1)
        
        for i in range(len(nums)):
            counts[nums[i]] += 1
        
        for i in range(len(counts)):
            if counts[i] == 0:
                return i

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [3,0,1]))
    print(solver.solver(nums = [0,1]))
    print(solver.solver(nums = [9,6,4,2,3,5,7,0,1]))

if __name__ == "__main__":
    main()