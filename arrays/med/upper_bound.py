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
        
        if low >= n:
            return -1
        
        return low

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver([5, 6, 8, 9, 6, 5, 5, 6], 8, 7))
    print(solver.solver([5, 6, 8, 8, 6, 5, 5, 6], 8, 10))
    #print(solver.solver())

if __name__ == "__main__":
    main()