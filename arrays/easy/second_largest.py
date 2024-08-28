import math

class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, arr):
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return arr[0]
        
        maximum = -1
        
        for element in arr:
            maximum = max(maximum, element)
        
        diffs = []
        
        for i in range(len(arr)):
            diffs.append(maximum - arr[i])
        
        next_min = math.inf
        for element in diffs:
            if element == 0:
                pass
            else:
                next_min = min(next_min, element)
                
        if next_min == math.inf:
            return -1
        
        return arr[diffs.index(next_min)]
            

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver([12, 35, 1, 10, 34, 1]))
    print(solver.solver([10, 10]))

if __name__ == "__main__":
    main()