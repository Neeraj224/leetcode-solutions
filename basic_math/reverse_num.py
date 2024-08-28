class Solution:
    def __init__(self) -> None:
        pass
    
    def reverse(self, x: int) -> int:
        limit = 2 ** 31

        num_s = str(x)
        negative_flag = False
        
        if num_s[0] == '-':
            negative_flag = not negative_flag
            num_s = num_s[1:]
            
        reversed_num = num_s[::-1]

        if x == 0 or int(reversed_num) <= -limit or int(reversed_num) >= limit:
            return 0

        zero_pointer = 0
        # remove zeroes:
        if reversed_num[0] == '0':
            for i in range(len(reversed_num)):
                if reversed_num[i] != '0':
                    zero_pointer += 1
                else:
                    break
        
            reversed_num = reversed_num[zero_pointer + 1:]
        
        if negative_flag:
            return int(reversed_num) * -1
        else:
            return int(reversed_num)
            

def main():
    solver = Solution()
    
    print(solver.reverse(123))
    print(solver.reverse(-123))
    print(solver.reverse(120))

if __name__ == "__main__":
    main()