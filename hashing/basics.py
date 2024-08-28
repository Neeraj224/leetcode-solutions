class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, array, queries):
        map = {}
        
        for i in range(len(array)):
            if array[i] in map:
                map[array[i]] += 1
            else:
                map[array[i]] = 1
        
        counts = []
        for element in queries:
            if element in map:
                counts.append(map[element])
            else:
                counts.append(0)

        return counts
        
def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver([1, 2, 1, 3, 2], [1, 3, 4, 2, 10]))

if __name__ == "__main__":
    main()