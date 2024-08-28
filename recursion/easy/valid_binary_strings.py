class Solution:
    def __init__(self) -> None:
        pass
    
    def generate_binary_strings(self, n):
        result = []
        
        def backtrack(current_string):
            if len(current_string) == n:
                result.append(current_string)
                return
            else:
                backtrack(current_string + '0')
                backtrack(current_string + '1')
                return
            
        backtrack("")
        return result
    
    def solver(self, n):
        binary_strings = self.generate_binary_strings(n)
        valid_strings = []
        valid = True
        
        for s in binary_strings:
            for i in range(0, len(s) - 1):
                dual_sub = s[i] + s[i + 1]
                if dual_sub.count('1') == 0:
                    valid = False
                    break
            if not valid:
                valid = True
            else:
                valid_strings.append(s)
        
        return valid_strings

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(n = 3))
    print(solver.solver(n = 2))
    print(solver.solver(n = 1))

if __name__ == "__main__":
    main()