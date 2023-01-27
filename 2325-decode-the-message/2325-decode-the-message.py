class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        ans = []
        for i in key:
            if i not in ans and i != " ":
                ans.append(i)
        res = ""
        for i in message:
            if i != " ":
                res += chr(ans.index(i) + 97)
            else:
                res += " "
        return res
                
            
        