class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, strings):
        # pass
        result = []
        n = len(strings)
        
        def backtrack(idx, current):
            if idx == n:
                result.append(current[:])
                return

            for letter in strings[idx]:
                backtrack(idx + 1, current + letter)
        
        backtrack(0, "")
        
        return result

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(["abc", "def", "ghi"]))
    # print(solver.solver())
    # print(solver.solver())

if __name__ == "__main__":
    main()