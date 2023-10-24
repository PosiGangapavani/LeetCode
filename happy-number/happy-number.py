class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True 
        
        else:
            while n > 4 and n != 1:
                ans = [int(x) * int(x) for x in str(n)]
                print(ans)
                n = sum(ans)
            if n == 1:
                return True 
            else:
                return False