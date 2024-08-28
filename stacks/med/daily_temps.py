class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, temperatures):
        # pass
        answers = [0] * len(temperatures)
        
        # print(list(enumerate(temperatures)))
        
        for i in range(len(temperatures)):
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    answers[i] = j - i
                    break
        
        return answers

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(temperatures = [73,74,75,71,69,72,76,73]))
    print(solver.solver(temperatures = [30,40,50,60]))
    print(solver.solver(temperatures = [30,60,90]))

if __name__ == "__main__":
    main()