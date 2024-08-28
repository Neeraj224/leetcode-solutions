class Selector:
    def __init__(self) -> None:
        pass
    
    def getN(self, n):
        return n - 1
    
    def checker(self, n):
        while True:
            n = self.getN(n = n)
            print(n, end = " ")
            
            if n == 1:
                break
        
        print("haha, outside")
    
    def try_catch_ex(self):
        x = "not a number 10"
        
        try:
            f = float(x)
        except ValueError:
            # you can do something about it:
            NUMDICT = "0123456789"      
            getNum = ''
            
            for i in range(len(x)):
                if x[i] in NUMDICT:
                    getNum += x[i]

            return int(getNum)
    
    def foo(self, x, y):
        return 8 * x + y
    
    def drawSquare(self, n):
        for i in range(n):
            print("")
            for j in range(n):
                print("#", end = " ")
        print("")
    
    def drawTriangle(self, n):
        for i in range(n + 1):
            print("")
            for j in range(i):
                print("#", end = " ")
    
    def numTriangle(self, n):
        for i in range(1, n + 2):
            print("")
            for j in range(1, i):
                print(j, end = " ")
        print("")
        
    def modNumTriangle(self, n):
        for i in range(1, n + 1):
            print("")
            for j in range(i):
                print(i, end = " ")
        print("")
    
    def upsideDownTriangle(self, n):
        for i in range(n, -1, -1):
            print("")
            for j in range(i):
                print("#", end = " ")
    
    def upsideDownNumTriangle(self, n):
        for i in range(n + 1, -1, -1):
            print("")
            for j in range(1, i):
                print(j, end = " ")
        print("")
    
    def righAngledTriangle(self, n):
        elements = []
        for i in range(1, n + 1):
            level = ""
            for j in range(i):
                level += "# "
            elements.append(level)
        
        idx = 0
        for i in range(n, -1, -1):
            for j in range(i):
                print(" ", end = " ")
            if idx < len(elements):
                print(elements[idx])
                idx += 1
        print("")
        
    def pyramid(self, n):
        elements = []
        num = 0
        for i in range(1, n + 1):
            level = ""
            for j in range(i + num):
                level += "# "
            elements.append(level)
            num += 1
        
        idx = 0
        for i in range(n, -1, -1):
            for j in range(i):
                print(" ", end = " ")
            if idx < len(elements):
                print(elements[idx])
                idx += 1
        
    def reversePyramid(self, n):
        elements = []
        num = 0
        for i in range(1, n + 1):
            level = ""
            for j in range(i + num):
                level += "# "
            elements.append(level)
            num += 1
        
        idx = len(elements) - 1
        
        for i in range(1, n + 1):
            for j in range(i):
                print(" ", end = " ")
            if idx >= 0:
                print(elements[idx])
                idx -= 1
    
    def diamond(self, n):
        self.pyramid(n)
        self.reversePyramid(n)
        print("")
    
    def cutDiamond(self, n):
        self.drawTriangle(n)
        self.upsideDownTriangle(n - 1)
        print("")
        
    def bitsamid(self, n):
        BIT1 = '1'
        BIT0 = '0'
        bit_flag = True
        
        for i in range(1, n + 1):
            print("")
            if i % 2 == 1:
                bit_flag = True
            else:
                bit_flag = False
                
            for j in range(i):
                if bit_flag:
                    print(BIT1, end = " ")
                    bit_flag = False
                else:
                    print(BIT0, end = " ")
                    bit_flag = True
                        
        print("")
        
    def numCrown(self, n):
        print("")
        SPACE = ""
        NUMSPACES = 2
        sequence = "1"
        num = 1
        
        for i in range(n):
            print(sequence, end = " ")
            for j in range(n * 2 - NUMSPACES):
                print(SPACE, end = " ") 
            print(sequence[::-1])
            
            NUMSPACES += 2
            num += 1
            sequence += str(num)
        print("")
    
    def numsPyramid(self, n):
        num = 1
        
        for i in range(n + 1):
            print("")
            for j in range(i):
                print(num, end = " ")
                num += 1
        print("")
    
    def alphabetPyramid(self, n):
        letter = 'A'
        for i in range(n + 1):
            print("")
            for j in range(i):
                print(letter, end = " ")
                letter = chr(ord(letter) + 1)
        print("")
    
    def multiAlphabetPyramid(self, n):
        letter = 'A'
        for i in range(1, n + 1):
            print("")
            for j in range(i):
                print(letter, end = " ")
            letter = chr(ord(letter) + 1)
        print("")
    
    def alphabetPyramidMod(self, n):
        letter = 'A'
        sequence = letter + " "
        
        for i in range(1, n + 1):
            print("")
            print(sequence, end = " ")
            letter = chr(ord(letter) + 1)
            sequence += letter + " "
        print("")
    
    def box(self, n):
        SYMBOL = "#"
        for k in range(n):
            print(SYMBOL, end = "")
            
        for i in range(2, (n + 1) - 1):
            print("")
            
            print(SYMBOL, end = "")
            
            for j in range(n - 2):
                print(" ", end = "")
            
            print(SYMBOL, end = "")
        
        print("")              
        
        for k in range(n):
            print(SYMBOL, end = "")
        
    def numbox(self, n):
        sequences = []
        num_seq = str(n)
        next_n = n
        steps = 2
        
        for i in range(((n * 2 - 1) // 2) + 1):
            print("")
            
            print(num_seq, end = " ")
            
            for j in range((n * 2 - 1) - steps):
                print(next_n, end = " ")
            
            if num_seq[-1] == '1':
                print(num_seq[len(num_seq) - 3::-1], end = "")
            else:
                print(num_seq[::-1], end = " ")
                
            steps += 2
            next_n -= 1
            num_seq = num_seq + " " + str(next_n)
                    
        
    def foo2(self, x):
        return x + 2

    def bar(self, action, element):
        return action(element)
            
            
def main():
    s1 = Selector()
    s1.checker(10)
    print(s1.try_catch_ex())
    print(s1.foo(2, 1))
    print(s1.foo("Na", " Batman!"))
    
    print("\n\n------a2zlogic--------")
    # a2z logic:
    s1.drawSquare(8)
    s1.drawTriangle(10)
    print("")
    s1.numTriangle(15)
    s1.modNumTriangle(9)
    s1.upsideDownTriangle(7)
    print("")
    s1.upsideDownNumTriangle(7)
    s1.righAngledTriangle(10)
    s1.pyramid(5)
    print("")
    s1.reversePyramid(5)
    print("")
    s1.diamond(5)
    s1.cutDiamond(5)
    s1.bitsamid(8)
    s1.numCrown(9)
    s1.numsPyramid(7)
    s1.alphabetPyramid(5)
    s1.multiAlphabetPyramid(5)
    s1.alphabetPyramidMod(5)
    print("")
    s1.box(10)
    print("")
    s1.numbox(7)
    
    
    print("\n\n------a2zlogic--------\n\n")
    
    print(s1.bar(s1.foo2, 4))
    
if __name__ == "__main__":
    main()
    
