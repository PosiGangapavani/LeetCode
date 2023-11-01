class Solution:
    def helper(self,idx,s,ans):
        if idx >= len(s) or len(s) == 0:
            return 
        self.helper(idx + 1 , s,ans)
        ans.append(s[idx])
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ans = []
        self.helper(0,s,ans)
        for i in range(len(ans)):
            s[i] = ans[i]
        
        