class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, arr, n, k):
        longest = 0
        current = 0
        agg = 0
        i = 0
        j = i
        
        while i < n and j < n:
            if agg < k:
                agg += arr[j]
                current += 1
                j += 1
            elif agg == k:
                longest = max(longest, current)
                current = 0
                agg = 0
                i += 1
                j = i
            else:
                agg = 0
                current = 0
                i += 1
                j = i
                    
        return longest

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver([10, 5, 2, 7, 1, 9], 6, 15))
    print(solver.solver([-1, 2, 3], 3, 6))
    print(solver.solver([-1,4,3,3,5,5], 6, 7))

if __name__ == "__main__":
    main()