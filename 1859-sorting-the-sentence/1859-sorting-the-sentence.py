class Solution:
    def sortSentence(self, s: str) -> str:
        ans = s.split(" ")
        out = []
        for i in range(1 ,10):
            for j in ans:
                if j[-1] == str(i):
                    out.append(j[:-1])
        return " ".join(out)
                    
       
        
            
            
        