class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums: list[int], k: int):
        windowSize = k
        i = 0
        maxsum = float('-inf')
        windowSum = 0
        
        while i < windowSize:
            windowSum += nums[i]
            i += 1
        
        maxsum = max(windowSum, maxsum)
        
        i = 1
        
        while i + windowSize - 1 < len(nums):
            
            windowSum -= nums[i - 1]
            windowSum += nums[i + windowSize - 1]
            
            maxsum = max(windowSum, maxsum)
            
            i += 1
        
        return maxsum / windowSize


def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [1,12,-5,-6,50,3], k = 4))
    print(solver.solver(nums = [5], k = 1))
    # print(solver.solver())

if __name__ == "__main__":
    main()