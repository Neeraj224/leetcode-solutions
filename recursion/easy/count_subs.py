class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums, k):
        # pass
        n = len(nums)
        
        def backtrack(i, csum, current):
            if i == n:
                if csum == k:
                    return 1
                return 0
            
            # first check the first branch - TAKE
            # so in the left branches, if we take those,
            # it will se how many counts are present, and it will
            # return those to the left
            current.append(nums[i])
            csum += nums[i]
            left = backtrack(i + 1, csum, current)
            
            # next, do not TAKE:
            # it will do the same for the right branches, i.e. when we DO
            # NOT TAKE those, then it will count how many of them sum up to the k
            # given, and it will return that count
            current.pop()
            csum -= nums[i]
            right = backtrack(i + 1, csum, current)
            
            return left + right
            
        return backtrack(0, 0, [])
            

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [1, 2, 1], k = 2))
    # print(solver.solver())
    # print(solver.solver())

if __name__ == "__main__":
    main()