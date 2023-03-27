class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        s = s[::-1]
        ans = ''
        for i in range(len(s)):
            if s[i] != '' :
                ans += s[i]
                ans += ' '
        #ans += ' '
        return ans[:-1]
       