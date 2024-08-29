class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ans1 = {}
        ans2 = {}
        for i in range(len(s)):
            if s[i] not in ans1 and t[i] not in ans2:
                ans1[s[i]] = t[i]
                ans2[t[i]] = s[i]
            elif s[i] in ans1 and ans1[s[i]] != t[i]:
                return False
            elif t[i] in ans2 and ans2[t[i]] != s[i]:
                return False
           
        return True
        # ans1 = {}
        # ans2 = {}
        # for i in range(len(s)):
        #     if s[i] not in ans1 and t[i] not in ans2:
        #         ans1[s[i]] = 1
        #         ans2[t[i]] = 1
        #     elif s[i] in ans1 and t[i] not in ans2:
        #         return False
        #     elif t[i] in ans2 and s[i] not in ans1:
        #         return False
        #     elif s[i] in ans1 and t[i] in ans2:
        #         ans1[s[i]] += 1
        #         ans2[t[i]] += 1
        # return True
    
    
            