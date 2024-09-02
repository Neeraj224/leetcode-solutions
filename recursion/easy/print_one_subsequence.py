class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums, k):
        # pass
        n = len(nums)
        
        def backtrack(i, csum, current):
            if i == n:
                if csum == k:
                    print(current)
                    return True
                return False
            
            current.append(nums[i])
            csum = sum(current)
            if backtrack(i + 1, csum, current) == True:
                return True

            current.pop()
            csum = sum(current)
            if backtrack(i + 1, csum, current) == True:
                return True
            
            return False
        
        backtrack(0, 0, [])

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [1, 2, 1], k = 2))
    # print(solver.solver())
    # print(solver.solver())

if __name__ == "__main__":
    main()