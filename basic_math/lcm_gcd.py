import math

class Solution:
    def __init__(self) -> None:
        pass
    
    def lcm_gcd(self, a, b):
        arr = [0] * 2
        
        gcd = math.gcd(a, b)
        lcm = (a * b) // gcd
        
        arr[0], arr[1] = lcm, gcd
        
        return arr

def main():
    solver = Solution()
    
    print(solver.lcm_gcd(5, 10))
    print(solver.lcm_gcd(14, 8))

if __name__ == "__main__":
    main()