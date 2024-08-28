class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, n, freqs, p):
        map = {}
        
        for item in freqs:
            if item in map:
                map[item] += 1
            else:
                map[item] = 1
        
        counts = []
        
        for i in range(1, n + 1):
            if i in map:
                counts.append(map[i])
            else:
                counts.append(0)
        
        return counts
            
def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(5, [2, 3, 2, 3, 5], 5))
    print(solver.solver(4, [3, 3, 3, 3], 3))
    print(solver.solver(2, [8, 9], 9))

if __name__ == "__main__":
    main()