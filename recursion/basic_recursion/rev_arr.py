class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, idx, arr, rev):
        if idx == -1:
            return rev
        else:
            rev.append(arr[idx])
            return self.solver(idx - 1, arr, rev)

def main():
    solver = Solution()
    
    #solver.solver()
    arr = [1, 2, 3, 4, 5]
    print(solver.solver(len(arr) - 1, arr, []))

if __name__ == "__main__":
    main()