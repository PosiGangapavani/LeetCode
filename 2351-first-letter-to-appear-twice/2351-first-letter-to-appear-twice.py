class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ans = {}
        for i in range(len(s)):
            if s[i] not in ans:
                ans[s[i]] = 1
            else:
                ans[s[i]] += 1
                return s[i]
                break
                    
        