import math

class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums: list[int]):
        # O(n):
        def verify_sort(arr):
            if len(arr) == 0 or len(arr) == 1:
                return True
            
            for i in range(1, len(arr)):
                if arr[i - 1] > arr[i]:
                    return False
            
            return True

        # O(n):
        def get_min_index(arr):
            minimum = math.inf
            
            for i in range(len(arr)):
                minimum = min(minimum, arr[i])
            
            return arr.index(minimum)
        
        def rotate_arr(arr, start):
            return arr[start:] + arr[:start]

        return verify_sort(rotate_arr(nums, get_min_index(nums)))

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [3,4,5,1,2]))
    print(solver.solver(nums = [2,1,3,4]))

if __name__ == "__main__":
    main()