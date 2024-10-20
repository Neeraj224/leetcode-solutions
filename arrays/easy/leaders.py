class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, arr):
        current_max = arr[-1]
        leaders = []
        
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] >= current_max:
                leaders.append(arr[i])
                current_max = arr[i]
        
        return leaders[::-1]

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(arr = [16, 17, 4, 3, 5, 2]))
    print(solver.solver(arr = [10, 4, 2, 4, 1]))
    print(solver.solver(arr = [5, 10, 20, 40]))
    print(solver.solver(arr = [30, 10, 10, 5]))

if __name__ == "__main__":
    main()