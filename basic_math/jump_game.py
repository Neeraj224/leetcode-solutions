class Solution:
    def __init__(self) -> None:
        pass
    
    def jumpGame(self, arr, n):
        # pos is the index
        pos = 0
        total_jumps = 0
        
        while True:
            if arr[pos] == 0:
                return -1
            pos = pos + arr[pos]
            total_jumps += 1
            
            if pos >= n - 1:
                return total_jumps
            
            

def main():
    solver = Solution()
    
    print(solver.jumpGame([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 11))
    print(solver.jumpGame([1, 4, 3, 2, 6, 7], 6))
    print(solver.jumpGame([0, 10, 20], 3))

if __name__ == "__main__":
    main()