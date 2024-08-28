class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, s: str):
        words = []
        current = ""
        
        for i in range(len(s)):
            if s[i] == " ":
                if current != "":
                    words.append(current)
                    current = ""
                continue
            else:
                current += s[i]
        if current != "":
            words.append(current)
        
        res = ""
        
        for i in range(len(words) - 1, -1, -1):
            res += words[i]
            res += " "
        
        return res[:len(res) - 1]

                

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(s = "the sky is blue"))
    print(solver.solver(s = "  hello world  "))
    print(solver.solver(s = "a good   example"))

if __name__ == "__main__":
    main()