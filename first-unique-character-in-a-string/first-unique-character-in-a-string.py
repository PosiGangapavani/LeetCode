class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = {}
        for i in s:
            if i not in ans:
                ans[i] = 1
            else:
                ans[i] += 1
        for i in range(len(s)):
            if ans[s[i]] == 1:
                return i 
        return -1
        