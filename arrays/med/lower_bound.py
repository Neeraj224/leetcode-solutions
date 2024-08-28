class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, arr, n, x):
        low = 0
        high = n - 1
        res = n
        
        while low <= high:
            mid = (low + high) // 2
            
            if x <= arr[mid]:
                high = mid - 1
            if x > arr[mid]:
                low = mid + 1
            if x == arr[mid]:
                return mid
        
        return high

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver([1,2,8,10,11,12,19], 7, 0))
    print(solver.solver([1,2,8,10,11,12,19], 7, 5))
    #print(solver.solver())

if __name__ == "__main__":
    main()