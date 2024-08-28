class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums):
        curr = 0
        max1 = -1
        i = 0
        
        while i < len(nums):
            if nums[i] == 1:
                curr += 1
                max1 = max(max1, curr)
            elif nums[i] == 0:
                curr = 0
            i += 1
            
        if max1 == -1:
            return 0
        
        return max1
        

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [1,1,0,1,1,1]))
    print(solver.solver(nums = [1,0,1,1,0,1]))

if __name__ == "__main__":
    main()