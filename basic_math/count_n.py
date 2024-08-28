class Solution:
    def __init__(self) -> None:
        pass
    
    def count_n(self, n):
        str_n = str(n)
        count = 0
        
        for i in range(len(str_n)):
            if str_n[i] == '0':
                continue
            if (n % int(str_n[i])) == 0:
                count += 1
        
        return count
    
def main():
    solver = Solution()
    
    print(solver.count_n(12))
    print(solver.count_n(2446))
    print(solver.count_n(23))

if __name__ == "__main__":
    main()