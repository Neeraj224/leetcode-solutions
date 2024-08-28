import math
class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, freqs):
        map = {}
        
        for item in freqs:
            if item in map:
                map[item] += 1
            else:
                map[item] = 1
        
        print(map)
        tuples = []
        for key, value in map.items():
            tuples.append([key, value])
        
        print(tuples)

        minnest = math.inf
        maxxest = -1
        min_i = 0
        max_i = 0
        
        for i in range(len(tuples)):
            if minnest != min(minnest, tuples[i][1]):
                minnest = min(minnest, tuples[i][1])
                min_i = i
            if maxxest != max(maxxest, tuples[i][1]):
                maxxest = max(maxxest, tuples[i][1])
                max_i = i
        
        return [tuples[min_i], tuples[max_i]]
        
        
            
def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver([10,5,10,15,10,10,5]))
    print(solver.solver([2,2,3,4,4,2]))

if __name__ == "__main__":
    main()