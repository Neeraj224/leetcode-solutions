class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, arr1, arr2, n, m):
        def solution1(arr1, arr2, n, m):
            i, j = 0, 0
            res = []
            
            while i < n and j < m:
                if arr1[i] <= arr2[j]:
                    if len(res) == 0 or res[-1] != arr1[i]:
                        res.append(arr1[i])
                    i += 1
                else:
                    if len(res) == 0 or res[-1] != arr2[j]:
                        res.append(arr2[j])
                    j += 1
            
            while i < n:
                if res[-1] != arr1[i]:
                    res.append(arr1[i])
                i += 1

            while j < n:
                if res[-1] != arr2[j]:
                    res.append(arr2[j])
                j += 1
            
            return res
        
        def solution2(arr1, arr2, n, m):
            return sorted(list(set(arr1 + arr2)))
    
        return solution1(arr1, arr2, n, m)
            
def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver([1, 2, 3, 4, 5], [1, 2, 3, 6, 7], 5, 4))
    print(solver.solver([2, 2, 3, 4, 5], [1, 1, 2, 3, 4], 5, 5))
    print(solver.solver([1, 1, 1, 1, 1], [2, 2, 2, 2, 2], 5, 5))

if __name__ == "__main__":
    main()