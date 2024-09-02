class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums, k):
        # pass
        n = len(nums)
        count = 0
        
        def backtrack(i, csum, current):
            nonlocal count
            if i == n:
                if csum == k:
                    count += 1
                    return
                return
            if csum > k:
                return
            
            # first check the first branch - TAKE
            current.append(nums[i])
            csum += nums[i]
            backtrack(i + 1, csum, current)
            
            # next, do not TAKE:
            current.pop()
            csum -= nums[i]
            backtrack(i + 1, csum, current)
            
        backtrack(0, 0, [])
        
        return count
            

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [1, 2, 1], k = 2))
    # print(solver.solver())
    # print(solver.solver())

if __name__ == "__main__":
    main()