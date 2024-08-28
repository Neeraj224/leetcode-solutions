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
        
        return maximum
        

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver([1, 8, 7, 56, 90]))
    print(solver.solver([5, 5, 5, 5]))
    print(solver.solver([10]))

if __name__ == "__main__":
    main()