class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums, k):
        # pass
        subsequences_k = []
        n = len(nums)
        # print(sum(nums))
        def backtrack(index, csum, current):
            if csum == k:
                subsequences_k.append(current.copy())
                return
            if csum > k:
                return
            if index == n:
                return
            
            current.append(nums[index])
            csum = sum(current)
            backtrack(index + 1, csum, current)
            
            current.pop()
            csum = sum(current)
            backtrack(index + 1, csum, current)
        
        backtrack(0, 0, [])
        
        return subsequences_k
        

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [1, 2, 1], k = 2))
    print(solver.solver([5, 2, 3, 10, 6, 8], 10))
    print(solver.solver([2, 5, 1, 4, 3], 10))

if __name__ == "__main__":
    main()