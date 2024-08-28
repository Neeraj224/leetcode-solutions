class Solution:
    def __init__(self) -> None:
        pass
    
    def sumDivisors(self, n):
        def get_divisors_sum(n):
            divisor_sum = 0    
            for i in range(1, n + 1):
                if n % i == 0:
                    divisor_sum += i
            
            return divisor_sum

        total = 0
        for i in range(1, n + 1):
            total += get_divisors_sum(i)
        
        return total

def main():
    solver = Solution()
    
    print(solver.sumDivisors(4))
    print(solver.sumDivisors(5))

if __name__ == "__main__":
    main()